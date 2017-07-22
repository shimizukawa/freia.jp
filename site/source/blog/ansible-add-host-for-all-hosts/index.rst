:date: 2015-6-25 23:50
:categories: ['Ansible', 'aws']
:body type: text/x-rst

====================================================
2015/06/25 ansibleのadd_hostを全てのhostで実行する
====================================================

Ansible_ を使って、これまで手動で行っていた作業を自動化しました。
その際に、 `Ansible公式のec2モジュールのドキュメント`_ のサンプルをまねて行うとうまくいかなかったので、うまく行く方法を考えました。

要件
=====

やりたいことは、以下の通りです。

* 複数のEC2インスタンスのパッケージを更新する
* パッケージ更新前と後にAMIバックアップを取る
* いくつかは普段停止状態なので、作業前に起動させて作業後に停止させる

実行手順
==========

1. インスタンスのアップデート前バックアップを取る
2. インスタンスを起動する
3. apt-get update & dist-upgrade & autoremove を行う
4. インスタンスのアップデート後バックアプを取る
5. インスタンスを停止する


これまで - awscli
==================

元々は手動でAWSのコンソールを操作していましたが、awscli を使って以下の手順に置き換えました。この手順でも、起動待ちなどを人間が見て次の手順に進めるなどが必要だったので、後述するAnsibleに乗り換えることにしました。

インストール::

   $ pip install awscli
   $ aws configure
   AWS Access Key ID []: xxxxxxxxxxx
   AWS Secret Access Key []: yyyyyyyyyyyyy
   Default region name []: ap-northeast-1
   Default output format [None]:

AMIバックアップ::

   $ aws ec2 create-image --instance-id i-xxxxxxxx --name "srv-dev 20150625-before" --description "srv dev (ubuntu14.04)” --reboot | grep ImageId
   "ImageId": "ami-01234567"
   $ aws ec2 describe-images --image-ids ami-01234567 | grep State 
   "State": "available",
   $ #availableになるまで何度か実行する

インスタンス起動::

   $ aws ec2 start-instances --instance-id i-xxxxxxxx
   $ aws ec2 describe-instances --instance-ids i-xxxxxxxx | grep PublicIpAddress
   "PublicIpAddress": "54.168.251.239",
   $ aws ec2 describe-instance-status --instance-ids i-xxxxxxxx | grep Status
   "Status": "ok",
   $ #okになるまで何度か実行する

パッケージ更新::

   $ ssh foo@54.168.251.239 sudo apt-get update
   $ ssh foo@54.168.251.239 sudo apt-get -y dist-upgrade
   $ ssh foo@54.168.251.239 sudo apt-get -y autoremove

AMIバックアップ::

   $ aws ec2 create-image --instance-id i-xxxxxxxx --name "srv-dev 20150625-after" --description "srv dev (ubuntu14.04)” --reboot | grep ImageId
   $ aws ec2 describe-images --image-ids ami-98765432 | grep State
   "State": "available",
   $ #availableになるまで何度か実行する

インスタンス停止::

   $ aws ec2 stop-instances --instance-ids i-xxxxxxxx


この手順ではすべてシェルコマンドで済みますが、待ち時間があったり、AMIのIDやIPアドレスを次のコマンドに渡したりと手間がかかっていました。


これから - Ansible
====================

最終的には以下のようにplaybookを作成しました。

インストール::

   $ pip install ansible boto

group_vars/all:

.. code-block:: yaml

   ---
   # file: group_vars/all

   ansible_ssh_user: foo
   region: ap-northeast-1
   yyyymmdd: '{{ansible_date_time.year}}{{ansible_date_time.month}}{{ansible_date_time.day}}'
   cold_standby: false

hosts:

.. code-block:: yaml

   [internal]
   localhost ansible_python_interpreter=/usr/local/bin/python

   [dev]
   srv-dev       instance_id=i-xxxxxxxx cold_standby=true
   srv-www-stage instance_id=i-wwwwwwww

update.yml:

.. code-block:: yaml

   ---
   - name: Backup and launch
     hosts: dev
     connection: local
     gather_facts: true
     tasks:
       - name: Create image
         local_action:
           module: ec2_ami
           instance_id: '{{ instance_id }}'
           region: '{{ region }}'
           wait: yes
           name: '{{inventory_hostname}} {{yyyymmdd}}-before'
           description: '{{inventory_hostname}} (ubuntu14.04)'

       - name: Start instances
         local_action:
           module: ec2
           instance_ids: '{{ instance_id }}'
           region: '{{ region }}'
           state: running
           wait: yes
         register: ec2

       # 実行中のhostをwithで回してdeployグループにIPを登録
       - name: Add new instances to host group
         local_action: add_host hostname={{hostvars[item].ec2.instances[0].public_ip}} groupname=deploy
         with_inventory_hostnames: play_hosts

       - name: Wait for the instances to boot by checking the ssh port
         local_action: wait_for host={{item.public_dns_name}} port=22 timeout=60 state=started
         with_items: ec2.instances


   - name: udpate packages
     hosts: deploy  #must match groupname in "add_host" above
     gather_facts: true
     tasks:
       - name: apt-get update
         apt: upgrade=dist update_cache=yes
         sudo: yes

       - name: Autoremove unused packages
         command: apt-get -y autoremove
         sudo: yes


   - name: Backup and shutdown
     hosts: dev
     connection: local
     gather_facts: true
     tasks:
       - name: Create image
         local_action:
           module: ec2_ami
           instance_id: '{{ instance_id }}'
           region: '{{ region }}'
           wait: yes
           name: '{{inventory_hostname}} {{yyyymmdd}}-after'
           description: '{{inventory_hostname}} (ubuntu14.04)'

       - name: Stop instances
         local_action:
           module: ec2
           instance_ids: '{{ instance_id }}'
           region: '{{ region }}'
           state: stopped
           wait: yes
         when: cold_standby


add_host の "bypass host loop" 問題
=====================================

上記のplaybookのadd_hostを使っているところでは、 ``srv-dev`` と ``srv-www-stage`` の2つのホストのIPアドレスを取得して ``deploy`` グループに登録することを期待しています。でも、実際には ``srv-dev`` のIPしか登録されません。

これは、 "bypass host loop" と呼ばれる挙動で、add_hostのような一部のモジュールはホストの数だけ実行するのでは無く、1回だけ実行するということのようです。 `Ansible公式のec2モジュールのドキュメント`_ に書いてあるadd_hostの使い方では、インスタンスを1つしか指定していません。でも、これを読んだら複数インスタンスで使いたいと思いますよね。

というあたりのIssueがいくつも見つかりました。

* https://github.com/ansible/ansible/issues/5145
* https://github.com/ansible/ansible/issues/6912
* https://github.com/ansible/ansible/issues/9931
* https://github.com/ansible/ansible/issues/10700

`Ansibleのadd_hostモジュール`_ のページには注意書きとして、「1回しか実行されないから、必要なら ``with_`` 系のループを使ってくれ」と書かれているので、以下のようにして回避しました。

.. code-block:: yaml

   # 実行中のhostをwithで回してdeployグループにIPを登録
   - name: Add new instances to host group
     local_action: add_host hostname={{hostvars[item].ec2.instances[0].public_ip}} groupname=deploy
     with_inventory_hostnames: play_hosts

``hostvars[item].ec2.instances[0].public_ip`` のあたりが苦し紛れな感じです。

hostvarsはホスト別の変数を全部もっている変数です。 ``with_inventory_hostnames: play_hosts`` で現在の実行対象ホスト一覧を回して、直前のアクションで ``register: ec2`` した変数を取り出しています。

この例では起動されるインスタンスはホスト毎に確実に1つなので、 ``instances[0]`` としてしまっています。今回調べて良く目にした ``with_items: ec2.instances`` という例は、AMIからインスタンスを起こしているため複数のインスタンスがありえますが、自分の使い方では0決め打ちでOKでしょう。本当はループしたかったのですが、 ``with_`` loopは複数同時に使えないみたいです。

期待する動作になっているのでいいかな、と思いつつ、もっと良い書き方があればお知らせ下さい。


参考
=========

* `Ansibleのlookup pluginについて調べてみた`_
* `Ansible マジック変数の一覧と内容`_



.. _Ansible: http://www.ansible.com/
.. _Ansible公式のec2モジュールのドキュメント: http://docs.ansible.com/ec2_module.html
.. _Ansibleのadd_hostモジュール: http://docs.ansible.com/add_host_module.html
.. _Ansibleのlookup pluginについて調べてみた:  http://qiita.com/yunano/items/4325935b8567572cc172
.. _Ansible マジック変数の一覧と内容: http://qiita.com/h2suzuki/items/15609e0de4a2402803e9

:date: 2013-02-10 20:10
:categories: ['Vagrant', 'Chef', 'Ubuntu']
:body type: text/x-rst

=========================================
2013/02/10 Vagrantで作るUbuntu-12.04環境
=========================================

*category: 'Vagrant', 'Chef', 'Ubuntu'*

Vagrantを使うための環境構築
============================

* step 1: 読む
  http://www.ryuzee.com/contents/blog/4292

* step 2: VirtualBoxインストール
  https://www.virtualbox.org/ で最新版(今は4.2.6)をインストール

* step 3: Vagrantインストール
  http://vagrantup.com/ から最新版(今は1.0.6)をインストール

* step 4: 有志で提供されているVagrant Box (OSテンプレート)の一覧を確認
  http://www.vagrantbox.es/

* step 5: Ubuntu 12.04.1 をVagrantに追加::

     $ vagrant box add ubuntu-12.04-amd64 http://goo.gl/8kWkm

  この追加でローカルにboxファイルが ``ubuntu-12.04-amd64`` という名前で
  インストールされる。

ここまでで事前準備完了。

.. note::

   2/14追記: boxにはVirtualBoxのGuest Additionsがインストール済みですが、
   VirtualBoxのバージョンが高くなると古いboxのGuest Additionsの互換性が
   無くなる場合があります。

   その場合は適宜vagrantbox.esから新しいboxを入手して読み替えて下さい。

Ubuntuのインスタンスを作る
============================

ここからはインスタンス作る度に行う。

* step 6: Vagrantのインスタンス置き場を作成して初期化::

     $ mkdir /path/to/vagrant_work/ubuntu1204
     $ cd /path/to/vagrant_work/ubuntu1204
     $ vagrant init ubuntu-12.04-amd64

  これでインスタンスの設定ファイル ``Vagrantfile`` が作成される。

* step 7: VirtualBoxインスタンスを起動::

     $ vagrant up

  VirtualBoxインスタンスが無ければ作成し、起動。あれば作成はスキップして起動。

* step 8 母艦からsshでログイン::

     $ vagrant ssh

  .. note::

     MacOS Xでlucid32の場合、Networkが起動しなかった場合の対処

     * 起動したOSにVirtualBoxのコンソールを使って ``vagrant`` / ``vagrant``
       でログインする

     * 設定を変更::

          $ vi /etc/network/interfaces
          #pre-up sleep 2

     * ネットワークの自動設定を行う::

          $ sudo apt-get install sysv-rc-conf
          $ sysv-rc-conf networking on
          $ /etc/init.d/networking restart
          $ exit

     * 母艦側でVMを再起動::

          $ vagrant reload

* step 9 使い終わったらゲストOSを終了::

     $ vagrant halt

* step 10 不要になった仮想環境を削除::

     $ sudo vagrant destroy


おまけ: VirtualBoxのsnapshotを作成するプラグインをVagrantに追加
=================================================================

vagrantのプラグインはgemで提供されているので、例えばsnapshotを作るためのコマンドが以下の設定で使えるようになります。

vagrantにsandbox機能を追加する::

   $ vagrant gem install sahara

使い方::

   $ vagrant sandbox on        #sandboxモードon
   $ vagrant sandbox commit    #on以降の変更を確定する
   $ vagrant sandbox rollback  #on時点に戻す
   $ vagrant sandbox off       #sandboxモードoff


感想
=====

使えるようになってみて思ったこと

* VirtualBoxは普通の使い方だとGUI画面が表示されるけどVagrantで起動するとGUIが無いのでスッキリ
* VirtualBoxのコントローラとしてだけ使うのもあり
* VirtualBoxのスナップショット機能を簡単に使いたくてsahara入れたけどchefと組み合わせて使っているとあまり使わなかった
* ChefやPuppetなどのprovisioning機能と組み合わせるとVMインスタンスは気軽に壊したり使い捨てたり出来るようになる

次のエントリでchefを使った例を紹介します。


:date: 2013-02-10 21:20
:categories: ['Vagrant', 'Chef', 'Python', 'Sphinx']
:body type: text/x-rst

====================================================================
2013/02/10 Vagrant+Chefで作るSphinx開発環境
====================================================================

*category: 'Vagrant', 'Chef', 'Python', 'Sphinx'*

一つ前のエントリ :doc:`../create-ubuntu-12.04-by-using-vagrant/index`
でVirtualBox+Vagrantを使えるようになったので、次にVagrantの
プロビジョニング環境を作ります。

ここでは例としてSphinxの開発環境を作ります。Sphinxのテストのために、
おおまかに以下を整えます。

* Python2.5, 2.6, 2.7, 3.1, 3.2, 3.3, pypy をインストール
* tex関連の動作確認をするためにtexlive をインストール
* bitbucketにリポジトリを置いているのでhgといくつかの拡張をインストール
* ついでに.vimrcと.screenrcを配置


Vagrant+Chefを使うための環境構築
=================================

* step 1: 母艦側で :command:`librarian-chef` コマンドを使えるようにする::

     $ gem install librarian --no-ri --no-rdoc
     ...
     22 gems installed

  .. note::

     インストールの途中でコンパイラを要求されます。Windows/Macの場合
     コンパイラが無いと面倒ですが、Vagrant自体がruby+gemで動作しているので
     ここにインストールする手もあります::

        $ vagrant gem install librarian  --no-ri --no-rdoc

     インストールしたlibrarianを実行するには以下のように設定します
     (Windowsの場合)。

     1. vagrantのインストール先の ``vagrant\bin`` に
        ``%HOME%\.vagrant.d\gems\bin\librarian-chef*`` をコピー
     2. コピーしたlibrarian-chef.batのrubyインタプリタをvagrant.batと
        同じにする::

          ``@"ruby.exe"`` -> ``@"%~dp1\..\embedded\bin\ruby.exe"``

     3. ``set GEM_HOME=%HOME%\.vagrant.d\gems``
     4. :command:`librarian-chef` 実行 -> OK

     できたけど無理矢理感あるｗ

     2の部分は他にRubyをインストールしてなければ、vagrantがインストールした
     ruby.exeの場所をPATHに設定しておけば不要。


librarianとvagrantで環境構築
================================

* step 2: vagrant-sphinx-testing を展開

  gitを使う場合::

     $ git clone git://github.com/shimizukawa/vagrant-sphinx-testing.git

  zipを取ってきて展開してもOK::

     $ curl -O https://github.com/shimizukawa/vagrant-sphinx-testing/archive/master.zip

  ここにはCheffileとVagrantfileが含まれています。

  .. note::

     2013/2/14 追記: Vagrantfileに記載されているconfig.vm.boxの値は環境に合わせて変更してください。
     現時点ではUbuntu-12.04でのみ動作確認済みです。


* step 3: chef cookbook をインストール::

     $ cd vagrant-sphinx-testing
     $ librarian-chef install

  :command:`librarian-chef` はCheffileの内容から必要なchef cookbook
  を取ってきて、cookbookディレクトリに保存します。

* step 4: インスタンスを起動::

     $ vagrant up

* step 5: ログイン::

     $ vagrant ssh

  ログインすると、 ``.hgrc``, ``.hgext``, ``.screenrc``, ``.vim`` などが
  HOMEディレクトリ以下に設定済みです。

  .. note::

     Windowsの場合はputty等でログインした方が良いかも。
     sshの設定は以下のコマンドで確認出来ます::

        $ vagrant ssh-config
        Host default
          HostName 127.0.0.1
          User vagrant
          Port 2222
          UserKnownHostsFile /dev/null
          StrictHostKeyChecking no
          PasswordAuthentication no
          IdentityFile /path/to/user/.vagrant.d/insecure_private_key
          IdentitiesOnly yes

* step 6: Sphinxのソースを配置::

     $ hg clone bb://birkenfeld/sphinx

  hgbb拡張がインストール済みなので ``bb://`` が使えます。

* step 7: Sphinxのテスト::

     $ cd sphinx
     $ tox
     ...
     py25: commands succeeded
     py26: commands succeeded
     py27: commands succeeded
     py31: commands succeeded
     py32: commands succeeded
     py33: commands succeeded
     ERROR:   pypy: commands failed
     du10: commands succeeded
     du09: commands succeeded
     du08: commands succeeded
     du07: commands succeeded
     congratulations :)

  pypyだけエラーが出ますね。後で直します :(


まとめ
=======

最後の手順6,7が人力なのが気にくわないですが、「これはchefの仕事じゃないだろう？」という話をchefの師匠 `@tk0miya <https://twitter.com/tk0miya>`_ と話したりしてました。このあたりは開発環境なのかデプロイターゲットなのかでまた変わってきそう。

なお、ここで使ったchefのcookbookは以下の通り。

apt:
   aptのupdate等してくれます。起動毎に最新になるはず。

git:
   gitコマンド使えるようにします。

python-build:
   https://github.com/shimizukawa/chef-python-build
   Pythonの複数バージョンをビルドしてインストール。
   zlib等の依存ライブラリは先に自動的にインストールします。
   cookbook ``build-essential`` に依存しています。

mercurial-env:
   https://github.com/shimizukawa/chef-mercurial-env
   mercurialの.hgrcを設定していくつかのmercurial pluginをインストール。
   cookbook ``mercurial`` に依存しています。

texlive:
   https://github.com/tk0miya/chef-texlive
   texliveをインストールします。
   インストールDVDをダウンロードしてくる。

shimizukawa-env:
   https://github.com/shimizukawa/chef-shimizukawa-env
   .vimrcや.screenrcを設定します。俺向け環境設定ファイル群置き場。


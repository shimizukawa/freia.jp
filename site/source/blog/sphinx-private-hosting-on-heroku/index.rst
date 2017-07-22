:date: 2017-06-17 23:55
:categories: ['Sphinx', 'Heroku', 'Hosting']
:body type: text/x-rst

=======================================================================
2017/06/17 SphinxドキュメントをHerokuにBasic認証付きでホスティングする
=======================================================================

実現したいこと
==============

* 非公開のSphinxドキュメントを自動ビルドしてアクセス制限付きのどこかにホスティングしたい

モチベーション
==============

1. SphinxでビルドしたHTMLをホスティングしたい
2. 対象ドキュメントは非公開（執筆中の本等）
3. リポジトリにPushしたら自動ビルドしてホスティング先にデプロイされてほしい
4. できれば無料で（安ければ有料でもOK）
5. あまり複雑な仕組みは使いたくない


今回は、某書籍のビルド&閲覧をしたかったので、この方法を使いました。

ソリューション
===============

Herokuで、make htmlを実行し、簡易的なWebアプリケーションでビルドしたHTMLを参照させることで、Sphinxドキュメントをホスティングします。Webアプリケーションが必要なところが不便ですが、代わりにBASIC認証をかけられます。

ただし、Herokuのgitに直接pushするには、pushしたい人全員がHerokuのアカウントを持っている必要がありますが、正直めんどくさいです。また、Herokuのgitを使った場合、コードリポジトリに欲しい機能（IssueやPull Request）などはありません。そこで、コード管理をGitLabで行い、GitLabにpushされたコードを自動的にHerokuにPushする機能を設定します。

メリット

* Herokuの無料プランで始められる
* Webアプリを使うので、BASIC認証を設定できる
* GitLabではプライベートリポジトリも無料
* コード管理はGitLabで行えるため、IssueやPRが使える

デメリット

* Herokuの設定と、Heroku用設定ファイルが必要
* Webアプリのコードが必要
* GitLabの設定が必要

設定
======

必要なもの
----------

* Herokuのアカウント
* GitLabのアカウント
* git


手順
---------------

1. Herokuにプロジェクトを作ります。例として、hellosphinx-herokuというプロジェクトを作ります。

2. GitLabにプロジェクトを作ります

   - 例: https://gitlab.com/shimizukawa/hellosphinx-heroku

3. Heroku API key を取得:

   - Herokuで: ``Account Settings`` -> ``Account`` -> ``API Key`` -> Reveal

4. GitLabのリモートリポジトリ同期機能を設定:

   - GitLab: ``settings`` -> ``Repository`` -> ``Push to a remote repository``
   - チェック: ``Remote mirror repository``
   - 設定: ``Git repository URL`` as ``https://heroku:<API-TOKEN-OF-HEROKU>@git.heroku.com/<HEROKU-APP-NAME>.git``

   .. figure:: gitlab-gitsync.*
      :width: 100%


5. SphinxのプロジェクトとWebアプリのコードを用意（後述）

6. GitLabにコードをPush

7. Done!


リポジトリに以下のファイルを用意します。

.. note::

   ここで紹介するコードは以下のリポジトリにあります
   https://gitlab.com/shimizukawa/hellosphinx-heroku

:doc/:
   Sphinxドキュメントのソースディレクトリ。index.rstやconf.pyを置きます。

:Procfile:
   Herokuのプロセス定義。
   Webアプリとしてrun.shを実行します::

      web: sh run.sh

:runtime.txt:
   Herokuで実行するランタイムを指定します::

      python-3.6.1

:run.sh:
   起動時にSphinxドキュメントをビルドして、ビルドしたHTMLを表示するWebアプリケーション ``main.py`` を起動します。
   環境変数は ``main.py`` で使います。
   ::

      export HTML_PATH=_build/html
      export BASIC_AUTH=hello:sphinx

      sphinx-build -M html doc _build
      python main.py

:requirements.txt:
   Herokuが起動時に環境にインストールするパッケージを指定しておきます。
   ::

      sphinx
      bottle

:main.py:

   指定ディレクトリにある静的ファイルを返すWebアプリの実装です。
   ``HTML_PATH`` 環境変数でSphinxのビルド済みHTMLのパスを指定します。
   ``BASIC_AUTH`` 環境変数にIDとパスワードを指定するとBASIC認証も設定できます（無指定なら無認証）。
   ::

      import os
      import bottle

      ROOT = os.path.join(os.environ.get('HTML_PATH', '.'))
      AUTH = os.environ.get('BASIC_AUTH', None)
      PORT = int(os.environ.get('PORT', '8080'))


      def check(username, password):
          return ':'.join([username, password]) == AUTH


      def server_static(path):
          if path.endswith('/'):
              path += 'index.html'
          return bottle.static_file(path, root=ROOT)

      if AUTH is not None:
          server_static = bottle.auth_basic(check)(server_static)

      server_static = bottle.route('<path:path>')(server_static)

      if __name__ == '__main__':
          bottle.run(host='0.0.0.0', port=PORT)

閲覧
------

- http://hellosphinx-heroku.herokuapp.com/
- ID / PW = hello / sphinx

無事、BASIC認証付きで、Heroku上で閲覧できるようになりました。


感想
=====

* Herokuの管理者はやっぱり2人以上欲しいかも。そうするとHerokuのことを教えないといけない
* GitLabのリポジトリ同期設定に、API Keyを貼り付けるので、GitLabプロジェクトに他の管理者を追加したら見られちゃう
* ときどきGitLabのリポジトリ同期が動作してない気がするので、Syncボタンを押してみたりした
* Bottle便利。

概ね、良好です。


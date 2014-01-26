:date: 2014-01-26 17:00
:categories: ['Sphinx', 'Translation', 'drone.io', 'AWS', 'S3', 'boto', 'Route53', 'IAM']
:body type: text/x-rst

================================================================================
2014/01/26 Sphinx翻訳ドキュメントのビルドと公開の自動化(transifex, drone.io, S3)
================================================================================

*categories 'Sphinx', 'Translation', 'drone.io', 'AWS', 'S3', 'boto', 'Route53', 'IAM'*


`Sphinx+翻訳 Hack-a-thon 2014.1`_ に参加しています。その成果です。

.. _Sphinx+翻訳 Hack-a-thon 2014.1: http://connpass.com/event/4397/

以前から `@shkumagai`_ が取り組んでいたdocutilsの翻訳をTransifexに乗せてhtmlページ生成まで自動化しました。

.. _@shkumagai: https://twitter.com/shkumagai


* 参考: :doc:`../sphinx-i18n-translation-procedure-with-transifex-amazon-s3/index`


.. contents::
   :local:


全体の構成
==========

* 自動ビルドは drone.io_ で行います
* docutilsのソースは http://svn.code.sf.net/p/docutils/code/trunk にあり、読み取りのみ可能です
* 自動化のための追加のファイルをbitbucketに置きます
* 翻訳は Transifex_ で行います
* Web公開はAWSのS3で行い、DNS登録はRoute53で行います。


.. _Transifex: https://www.transifex.com/
.. _drone.io: https://drone.io/


AWS
---

* AWSアカウントを開設（既存アカウントでやると支払いが混ざるので別アカウントで）
* S3でbucketを作る: ``docutils.sphinx-users.jp``
* bucketのStatic Website HostingをEnableにする: Index Document: ``index.html``
* IAMでboto接続用アカウントを作成し、Access Keyを生成しておく: ``sphinxjp-web-bucket``
* IAMのsphinxjp-web-bucketアカウントのポリシーでS3への書き込み権限をあたえる::

   {
     "Statement": [
       {
         "Sid": "Stmt1210121092112",
         "Action": [
           "s3:DeleteObject",
           "s3:GetObject",
           "s3:GetObjectAcl",
           "s3:ListBucket",
           "s3:PutObject",
           "s3:PutObjectAcl"
         ],
         "Effect": "Allow",
         "Resource": [
           "arn:aws:s3:::docutils.sphinx-users.jp",
           "arn:aws:s3:::docutils.sphinx-users.jp/*"
         ]
       }
     ]
   }

* Route53でdocutils.sphinx-users.jpをDNS登録する:

  :Name: docutils.sphinx-users.jp
  :Type: A - IPv4 address
  :Alias: Yes
  :Alias Target: S3 Website Endpoint の docutils.sphinx-users.jp


Transifex
---------

* アカウントを開設する: 既存アカウントを使っても良いが、drone.ioにパスワードを書くので専用がお勧め
* プロジェクトを作る https://www.transifex.com/projects/p/docutils/
* 作成したプロジェクトに翻訳元データと翻訳済みデータをアップロード

  * tx push -s でpotファイルをアップロード
  * tx push -t -l ja で既存のpoファイルをアップロード
  * 参考: :doc:`../sphinx-i18n-translation-procedure-with-transifex-amazon-s3/index`

Bitbucket
---------

docutilsはSphinxドキュメントではないのでconf.pyや追加のindexを用意します。

* https://bitbucket.org/sphinxjp/docutils-translation リポジトリを作り、以下のファイルを追加:

  * .tx/config: potやpoファイルとtransifex上のリソースとの対応付けファイル
  * index.txt: docutilsの各ドキュメントへのリンクを書いたSphinx用トップページ
  * conf.py: 必要最小限のSphinx設定、gettext設定を含む
  * droneio.sh: 翻訳を適用してドキュメントをビルドする手順::

      ##################################
      # get docutils source
      svn export --force http://svn.code.sf.net/p/docutils/code/trunk .

      ################################
      # setup sphinx and others
      pip install sphinx boto_rsync babel sphinx-intl transifex-client

      ################################
      # setup transifex setting files
      sphinx-intl create-transifexrc        #create ~/.transifexrc

      ###########################
      # make translated document
      tx pull --all                         #pull po files from transifex
      sphinx-intl build                     #compile po -> mo
      sphinx-build -b html -d _build/doctrees -Dlanguage=ja . _build/html

      ##################################
      # deploy to s3
      boto-rsync --delete -g public-read _build/html s3://docutils.sphinx-users.jp/


Drone.io
--------

https://drone.io/bitbucket.org/sphinxjp/docutils-translation/admin

* アカウントを開設する（既存があれば利用）
* New Project で bitbucket.org/sphinxjp/docutils-translation を選択して作成
* Environment Variables にsphinx-intlとAWSの鍵などを設定::

     PIP_USE_WHEEL=true
     SPHINXINTL_TRANSIFEX_USERNAME=<YOUR-TRANSIFEX-ID>
     SPHINXINTL_TRANSIFEX_PASSWORD=<YOUR-TRANSIFEX-PW>
     SPHINXINTL_LOCALE_DIRS=locale
     AWS_ACCESS_KEY_ID=<YOUR-AWS-ACCESS-KEY>
     AWS_SECRET_ACCESS_KEY=<YOUR-AWS-SECRET-ACCESS-KEY>

  環境変数の内容は管理権限のあるひとしか見れないので鍵設定に便利。

* Commandsに ``sh -x droneio.sh``


droneio.shの内容をCommandsに書いておいてもいいですが、差分管理出来なくなるので、リポジトリに入れています。


まとめ
======

docutilsドキュメントの翻訳を http://docutils.sphinx-users.jp/ で見れるようになりました。 `@shkumagai`_ ++

でもまだまだ訳されていない部分が多いので、 https://www.transifex.com/projects/p/docutils/language/ja/ に参加して、みんなで翻訳しましょう！


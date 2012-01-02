:date: 2006-01-15 20:16:24
:categories: ['Unix']
:body type: text/x-rst

==============================
2006/01/15 apache2.2にしてみる
==============================

先日 `ZopeをApacheのSSLで動かすメモ`_ を書いた後で、一部のファイル(PNGフォーマットの画像)をSSL経由でアップロードできなくなると言う問題が発覚。色々いじってみたものの原因が分からず syd.jp の中の人に相談したところ「ApacheのSSLが腐ってるんじゃない？」というありがたいお言葉をいただいたので、2.0.54から2.2.0にアップデートしてみたら問題が解消した。

ところで、apache2.2にしたらmod_auth_pamが動作しなくなった。ウチでは認証は全部LDAPにやらせているので、これが使えないとsubversionのcommitが出来なくなってしまう。現状ではまだapache2.2についてのドキュメントは多くなく、apache本家やmod_auth_pamのサイトにも有力な情報がなかった。エラーログを見てみたところ::

  [Sun Jan 15 19:23:34 2006] [error] [client x.x.x.x] (9)Bad file descriptor: Could not open password file: (null)

上記のように記録されていたので、どうやらPAM認証せずにパスワードファイル認証を行おうとしているらしい。それなら、と、以下のようにmod_auth_pamのロードをLoadModuleの先頭に持って行ったらうまくいった::

  LoadModule auth_pam_module    libexec/apache22/mod_auth_pam.so
  LoadModule authn_file_module libexec/apache22/mod_authn_file.so
  LoadModule authn_dbm_module libexec/apache22/mod_authn_dbm.so
  LoadModule authn_anon_module libexec/apache22/mod_authn_anon.so

ロード順が今回の原因だった、というのはおいといて、2.0→2.2の変更内容には特にそれらしい記述は見あたらないんだけどなぁ‥‥。


.. _`ZopeをApacheのSSLで動かすメモ`: http://www.freia.jp/taka/blog/zope3092apache306essl52d5304b305930e130e2


.. :extend type: text/x-rst
.. :extend:


.. :comments:
.. :comment id: 2006-01-16.9433770488
.. :title: Re:apache2.2にしてみる
.. :author: masaru
.. :date: 2006-01-16 07:25:50
.. :email: 
.. :url: 
.. :body:
.. syd.jpの中の人は優秀ですね
.. 

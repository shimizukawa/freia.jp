:date: 2008-06-26 00:39:46
:tags: Plone

====================================================================
2008/06/26 PloneとIE7でMSXMLアドオンの実行警告メッセージが表示される
====================================================================

via `ngi644の日記 » Blog Archive » IE7でKupuによる画像がアップロードできない`_

Ploneの特定のバージョンのサイトを、特定の環境のIE7で閲覧すると、添付画像のようなMSXMLアドオンの実行警告メッセージが表示されます。この問題の原因については前述のサイトの、さらに引用元で語られていて、この情報を元に検証してみたところ以下の条件で発生する模様。

- Office2003,2007等をインストールするとMSXML5.0もインストールされる
- IE7はMSXML5.0を標準では許可しない
- sarissa.jsを使っているkupuとかPloneのLiveSearchで問題が発現する（KSSも?）

解決方法としては、 sarissa.js に以下の文字列::

  Msxml2.XMLHTTP.5.0
  MSXML2.FreeThreadedDOMDocument.5.0
  Msxml2.XSLTemplate.5.0

があったら、これらを削除すればOK（プログラム的に正しくね）。
ちなみに、MSXML5.0はOS標準ではない（Win95～Vista,Server全て！）ようです。Vistaでは3.0と6.0が標準で入っているらしい。


参考
-----
- `ngi644の日記 » Blog Archive » IE7でKupuによる画像がアップロードできない`_
- `IE7弹出MSXML 5.0支持的问题 — 中国Zope/Plone用户组`_
- `Microsoft XML パーサー (MSXML) のバージョン一覧`_
- `Microsoft XML Parser および Microsoft XML Core Services (MSXML) をインストールする方法`_
- `Windows Vista ベースのコンピュータで Microsoft XML Core Services 4.0 Service Pack 2 の互換性と信頼性を向上させる更新プログラムについて`_


.. _`ngi644の日記 » Blog Archive » IE7でKupuによる画像がアップロードできない`: http://ngi644.net/blog/archives/161

.. _`IE7弹出MSXML 5.0支持的问题 — 中国Zope/Plone用户组`: http://czug.org/blog/zhangbingkai/ie7danchumsxml-5-0zhichidewenti

.. _`Microsoft XML パーサー (MSXML) のバージョン一覧`: http://support.microsoft.com/kb/269238/ja

.. _`Microsoft XML Parser および Microsoft XML Core Services (MSXML) をインストールする方法`: http://support.microsoft.com/kb/324460/ja

.. _`Windows Vista ベースのコンピュータで Microsoft XML Core Services 4.0 Service Pack 2 の互換性と信頼性を向上させる更新プログラムについて`: http://support.microsoft.com/kb/941833/ja


.. :extend type: text/html
.. :extend:


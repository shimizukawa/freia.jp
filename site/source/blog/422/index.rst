:date: 2007-03-21 21:03:29
:categories: ['Zope']
:body type: text/x-rst

=======================
2007/03/21 ZopeのHotfix
=======================

*Category: 'Zope'*

Zope2.8以降に脆弱性が発見され、Hotfixがリリースされました。
内容はGETメソッドで権限昇格できてしまう、というもので対策としてセキュリティー関連メソッドにはPOSTでのみアクセス出来るようにしたようです。

- http://zope.jp/download/ZopeHotfix/releases/Hotfix-20070320
- http://www.zope.org/Products/Zope/Hotfix-2007-03-20/announcement

HTTP GET での certain types of misuse なんだからそっちを修正するパッチかと思いきや、POSTでのみアクセスできるようにするという対策が施されたHotfixでした。GETの処理が影響を受けないように対策したのかな？


.. :extend type: text/html
.. :extend:

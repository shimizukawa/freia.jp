:date: 2009-09-05 17:47:22
:categories: ['web']
:body type: text/x-rst

=================================================================
2009/09/05 DeliveranceでOSWDのデザインをTwitter.comに適用してみた
=================================================================

*Category: 'web'*

`Zope/Plone勉強会3`_ でDeliveranceを使ってデザイン適用をちょっと練習してみた。

デザインは `Open Source Web Design`_ から取得した `SilverGlow`_ 。適用サイトは今回はTwitterにしてみました。
ルールファイルとなるdeliverance.xmlに書いたルール部分は6行です。

deliverance.xml::

  <ruleset>
  
    <server-settings>
      <server>localhost:8000</server>
      <execute-pyref>true</execute-pyref>
      <dev-allow>127.0.0.1</dev-allow>
      <dev-user username="admin" password="admin" />
    </server-settings>
  
    <proxy path="/_theme">
      <dest href="{here}/../theme" />
    </proxy>
  
    <proxy path="/" >
      <response rewrite-links="1" />
      <dest href="http://twitter.com" />
    </proxy>
  
    <theme href="/_theme/theme.html" />
  
    <rule>
      <append content="ul.about" theme="children:#about" />
      <append content="div.stats" theme="children:#stats" />
      <append content="#following" theme="children:#following" />
      <replace content="div.section || div#content" theme=".right_content" />
      <append content="h2.thumb img" theme="#about h4" />
      <replace content="children:h2.thumb" theme="children:.block_right" />
    </rule>
  
  </ruleset>


あとはthemeのcss/htmlを数行書き換えて完成。1ページくらいなら簡単にできました。

DeliveranceとSphinx生成ドキュメントってとっても親和性が高い気がする。SphinxやPloneに独自Skinを適用しようとがんばるよりもDeliveranceのルールを覚える方が楽ではある。実際の運用まで考えるとまだ色々ひっかかるケドね。


- `Deliverance v0.3 documentation`_
- `Deliverance Configuration`_

.. _`Deliverance v0.3 documentation`: http://deliverance.openplans.org/index.html
.. _`Deliverance Configuration`: http://deliverance.openplans.org/configuration.html
.. _`Zope/Plone勉強会3`: http://zope.jp/events/zope-plone-sprint-tokyo-3/
.. _`Open Source Web Design`: http://www.oswd.org/
.. _`SilverGlow`: http://www.oswd.org/design/preview/id/3194


.. :extend type: text/html
.. :extend:


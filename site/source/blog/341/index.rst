:date: 2006-05-09 01:51:21
:tags: Zope, Plone

============================================
ATCTSmallSampleの英語版をリリース
============================================

4月末までに作業する予定だった英訳作業をようやく完了しました。変な英文を大量に生産した気がします。

- `ATCTSmallSample 0.3`_

英語を日本語に翻訳するときには、 ``You`` を訳すときに消してしまうとかすればそれっぽい日本語が出来るのですが、逆に、日本語の文章って主語がない場合が多いので、英語にするときにどうしていいのか分からない場合があって困りました。

::

  # ここでportal_skinを取得します
  skins_tool = getToolByName(self, 'portal_skins')

とかいうコード説明の日本語をexcite君に食わせると ``portal_skin is acquired here.`` とか訳されますが、これでいいのかなあ‥‥まあいいか。みたいな。こういうのの勉強するには、教科書を読むよりも、海外産ソースの英語コメントを読んで練習するしかないかな。


.. _`ATCTSmallSample 0.3`: http://plone.org/products/atctsmallsample/releases/0.3



.. :extend type: text/x-rst
.. :extend:


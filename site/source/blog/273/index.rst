:date: 2005-11-24 02:22:57
:categories: ['Programming', 'Plone']
:body type: text/x-rst

================================
2005/11/24 ATBookshelf実装な一日
================================

`先日のCOREBlogオフ会`_ の時から少し機能が増えていて、Amazonサイト表示中にブックマークレットで登録する機能とか、画像データの内部保持とか、COREBlog2のIInlineObjectのサイズ指定表示とかに対応しました。

あとAmazonから取得した画像をタイル表示できるようにしてみました。タイル表示だとタイトルがぱっと見てわからないのと、画像が無いアイテムの場合にどうしようか？という感じです。

野望としては、インクリメンタル絞り込みを実装したり、AjaxなD&D並び替えに対応したりしたいところですが、iTunesのユーザーインターフェースを参考にしてしまうと並び替えの意味は無いか・・と思ったり。どちらかというとカテゴリとか★ソートとかが重要か。。

- `ATBookshelf概要ページ`_
- `ATBookshelfデモページ`_


.. _`先日のCOREBlogオフ会`: http://www.freia.jp/taka/blog/271
.. _`ATBookshelf概要ページ`: http://www.freia.jp/taka/memo/plone/atbookshelf
.. _`ATBookshelfデモページ`: http://www.freia.jp/taka2/shelf



.. :extend type: text/html
.. :extend:

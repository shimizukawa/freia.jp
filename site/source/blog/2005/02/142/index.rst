:date: 2005-02-22 00:54:01
:tags: Zope

============================================================
PloneのDiscussion設定をOnにしたら権限を失った！？
============================================================

タイトルのまんまだが、Anonymousだろうが、Manageだろうが、トップページを表示しようとすると権限不足ですと言われてしまう。何事！？？

とりあえず、エラーメッセージから、getReplies関数へのアクセス権が無いらしいことが分かったので、これから調べることに‥‥大阪の夜はplone調査‥‥

エラーメッセージ抜粋::

  You are not allowed to access 'getReplies' in this context
  portal.sort_modified_ascending( portal_discussion.getDiscussionFor(here).getReplies())


追記


.. :extend type: text/plain
.. :extend:


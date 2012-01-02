:date: 2005-05-25 00:03:54
:categories: ['Plone', 'python']
:body type: text/x-rst

================================================
2005/05/25 COREBlogページだけportletを切り替える
================================================

COREBlog(plonified)のページが表示された場合に、左slotのportletを一部変更するようにしてみました。

簡単にやるためには、COREBlogフォルダのプロパティーにleft_slotsという名前のlines型のフィールドを用意して、表示したいportletマクロを羅列すれば良いのですが、それだと親フォルダで設定したものと別で管理しないといけないので、今回はleft_slotsという名前のScript(Python)を置いて代用しています。

.. code-block:: python

  path = container.getPhysicalPath()
  path = '/'.join(path[:-1])
  parent = container.restrictedTraverse(path)
  slots = parent.left_slots
  slots = [x for x in slots if 'blog' not in x]
  slots[:0] = ['here/portlets/archives/macros/portlet',
               'here/portlets/categories/macros/portlet',
              ]
  
  return slots

上記のマクロは自分より上位パスから ```left_slots``` を取得して ```blog``` という文字を含むportletを除外してから、 ```archives``` と ```categories``` のportletを追加しています。 ( *parentを一発で手に入れるコードとかありそうな気がするけど...* )

うーん、見ているページによってportletが変わってしまうのはどうなんだろう？違和感ありますが、とりあえずこれでしばらく様子を見てみます。



.. :extend type: text/plain
.. :extend:

:date: 2004-09-09 00:59:32
:tags: python, Programming
:body type: text/x-rst

=====================
2004/09/09 pyuiの練習
=====================

今日はpyuiのmenuをいじってみました::

 import pyui
 pyui.init(800,600)
 def onCreate(item):
  pyui.widgets.Frame(50,50,100,100,item.text)
 menu=pyui.widgets.Menu("create")
 menu.addItem("Green", onCreate)
 menu.addItem("White", onCreate)
 menubar = pyui.widgets.MenuBar()
 menubar.addMenu(menu)
 pyui.run()



.. :extend type: text/x-rst
.. :extend:

しかし、これではつまらないので、Menuの選択毎に違う挙動をさせてみたいと思います。本来であれば挙動を定義した関数(上記の例ではonCreate)を複数用意してそれぞれのMenuItemに登録するところですが、ここではlambdaを使って1行で書いてみたいと思います::

  import pyui
  pyui.init(800,600)
  menu=pyui.widgets.Menu("create")
  menu.addItem("Window" ,lambda item: pyui.widgets.Frame(50,50,100,100,item.text))
  menu.addItem("Console",lambda item: pyui.dialogs.Console(100,100,200,100))
  pyui.widgets.MenuBar().addMenu(menu)
  pyui.run()


なかなかすっきりしました。

実際の所、lambdaの乱用はしない方が賢明なのですが、とりあえずlambdaの練習ということで、もう一歩踏み込んでlambdaを使ってみました::

  import pyui
  pyui.init(800,600)
  pyui.widgets.MenuBar().addMenu((lambda menu=pyui.widgets.Menu("create"): menu.addItem("Window",lambda item: pyui.widgets.Frame(50,50,100,100,item.text)) and menu.addItem("Console",lambda item: pyui.dialogs.Console(100,100,200,100)) and menu)())
  pyui.run()

もう読めません（笑）

途中からpyuiは関係なくなってしまいましたが、こんな事も出来る、というのを体験してみたかったと言うことで。
おかげで、既存のpythonのコードを読んでいて時々出てくる and と or を使用したif文の短絡表記方法が理解できました。

やはり習うより慣れろ、という事で、実際にコードを書かないと文法とか表現って身に付かないですね。


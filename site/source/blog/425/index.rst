:date: 2007-03-24 11:43:07
:categories: ['turbogears']
:body type: text/x-rst

==================================
2007/03/24 kidのpy:extendsにはまる
==================================

*Category: 'turbogears'*

たとえば

.. code-block:: python

   @expose(template="proj.templates.foo")
   def index(self):
       return dict(master="proj.templates.master")

などとしてmasterという変数にtemplateのパスを渡す。それをkidがわで

.. code-block:: xml

   <html xmlns="http://www.w3.org/1999/xhtml"
         xmlns:py="http://purl.org/kid/ns#"
         py:extends="master">

と書くと、masterというnameは定義されていない！と怒られる。でも

.. code-block:: xml

   <html xmlns="http://www.w3.org/1999/xhtml"
         xmlns:py="http://purl.org/kid/ns#"
         py:attrs="{'foo':master}">

これは期待通りに動作する。つまりextendsの評価がindex関数から渡された変数の展開よりも先ということだろう。
ということで、index関数からextendsするテンプレートを渡しても、単純にextendsすることは出来ないということか。

ちなみに<html>タグの前だと${master}もNameErrorになる。<html>タグの後だとエラーにならない。

この辺の理由はkidcでkidをコンパイルしてpyファイルを生成するとわかる。わかるけど、どうすれば上記のextendsをうまくできるようになるかはまだよく分からない。。。


.. :extend type: text/html
.. :extend:


:date: 2011-06-16 00:00:00
:categories: ['python', 'django']
:body type: text/x-rst

=======================================================================
Djangoのモデルオブジェクトの値を自動表示する__repr__のデｨスクリプタ実装
=======================================================================

`@podhmo がDjangoのモデルクラスで__unicode__を書き換える方法について、継承かdecoratorかという話をしていた`__ ので、別解を考えてみた。

.. __: http://twitter.com/#!/podhmo/status/80999729193959424

Djangoは__unicode__が実装されていればその結果を使って__repr__を整形表示してくれるのだけど、__repr__はPython2系ではASCII文字列を返すべきという話もあり、悩ましいところ。とりあえずその点は置いておく。

Djangoのモデルで__unicode__を実装せずに実装してshellで表示すると以下のようになる。

.. code-block:: python

    >>> class Project(models.Model):
    ...     name = models.CharField(u'プロジェクト名', max_length=255)
    ...
    >>> p = Project(name="Foo")
    >>> p.save()
    >>> p
    <Project: Project object>

これをデバッグしやすいように表示するには__unicode__を実装するか、以下のように__repr__を実装する。

.. code-block:: python

    >>> class Project(models.Model):
    ...     name = models.CharField(u'プロジェクト名', max_length=255)
    ...     def __repr__(self):
    ...         return '<Project: id=%d, name=%r>' % (self.pk, self.name)
    ...
    >>> p = Project(name="Foo")
    >>> p.save()
    >>> p
    <Project: id=1, name=u'Foo'>


しかしこの方法だとモデル毎に実装していかなければいけないし、クラス実装にべったりくっついてしまうので論理的に分解して理解しづらい。

__repr__ が自動的にModelのフィールド値を集めて返してくれれば良いし、継承したモデル毎に再実装するのはいやだし、デバッグ中以外は不要なので付け外しがあるいていどしやすい形式になっていれば良いということなので、ディスクリプタを使って実装してみる。

.. code-block:: python

    class AutoFieldsRepr(object):
        def __get__(self, instance, cls):
            def __repr__():
                attrs = ((f.name, getattr(instance, f.name))
                         for f in cls._meta.fields)

                # formatting
                formatted = ', '.join("%s=%r" % x for x in attrs)
                return "<%s %s>" % (cls.__name__, formatted)

            return __repr__

これを以下のようにモデルクラスに差し込んで使う。

.. code-block:: python

    class Project(models.Model):
        name = models.CharField(u'プロジェクト名', max_length=255)

        __repr__ = AutoFieldsRepr()

これをshellで使うと以下のように表示される。

::

    >>> Project.objects.all()[0]
    <Project: id=1, name=u'Foo'>

この方法なら、仮にProjectを継承したモデルがあっても自動的に継承したモデルのフィールドも表示してくれるので、あちこちに実装を差し込む必要は無い。

さらに、DjangoのModelクラスに__repr__を差し込んでしまえば、上記のようにProjectクラスに ``__repr__ = AutoFieldsRepr()`` を書く必要も無くなるので、たとえば auto_fields_repr.py を以下の内容で用意しておく。

auto_fields_repr.py:

.. code-block:: python

    class AutoFieldsRepr(object):
        def __get__(self, instance, cls):
            def __repr__():
                attrs = ((f.name, getattr(instance, f.name))
                         for f in cls._meta.fields)

                # formatting
                formatted = ', '.join("%s=%r" % x for x in attrs)
                return "<%s %s>" % (cls.__name__, formatted)

            return __repr__

    from django.db import models
    models.Model.__repr__ = AutoFieldsRepr()

これを使いたいシーンでのみ（shellなどで） ``import auto_fields_repr`` すれば全てのモデルのオブジェクトが見やすく整形されて表示されるようになる。はず。

.. code-block:: python

    >>> from django.contrib.auth.models import User
    >>> u = User.objects.all()[0]

    >>> u
    <User: admin@test.test>

    >>> import auto_fields_repr

    >>> u
    <User id=1, username=u'admin@test.test', first_name=u'', last_name=u'', .......


長くなりすぎたので上記例では末尾を省略したけど、期待通り動作しているみたい。
あとは__repr__のUnicode処理やエラー処理をちゃんと実装するとか、改行を入れてきれいに表示するとか、欲しいフィールドだけを表示するとか、もうちょっと手を入れればけっこう使えそうな気がする。

ディスクリプタについては清水川も翻訳に参加した `エキスパートPythonプログラミング`_ のP108, `3.3.1 ディスクリプタ` で、仕組みや便利な使い方などが紹介されているので、ぜひぜひご参照ください。 `エキPy読書会もやってます！`_

.. note::

  当初、__unicode__ を差し替える実装例で書いていましたが、Django以外では__repr__書き換えないと期待した動作にならないのと、django.db.models.Model.__unicode__差し替えでは期待した動作にならないため、__repr__差し替えの方針で書き直しました。

.. _`エキスパートPythonプログラミング`: http://www.amazon.co.jp/dp/4048686291/freiaweb-22
.. _`エキPy読書会もやってます！`: http://www.freia.jp/taka/docs/expertpython/reading/


.. :extend type: text/x-rst
.. :extend:

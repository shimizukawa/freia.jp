:date: 2009-09-14 02:06:59
:tags: Zope, python
:body type: text/x-rst

=====================================================================
2009/09/14 Railsのbefore_filterっぽい仕組みをPythonのデコレータで実装
=====================================================================

以前Railsで作った某アプリをPythonに移植中です。出来るだけPythonの流儀に組み直してるんですが、Railsのbefore_filterを分かりやすく組み替えるのが思いつかなかったので、Pythonで同じようなことをする仕組みを作ってみました。と言ってもzope.formlibのActionsから8割くらいコードをパクってきてます。

目的は以下のようなにコードを用意すれば、indexアクションやcreateアクションが呼ばれる前に２つの事前処理関数が実行されるようにすること。

Rubyだとこう。

.. code-block:: ruby

  class FooController < ApplicatoinController
    before_filter :setup1, :setup2

    def index
      render ...
    end

    def create
      user = User.new(params[:user])
      user.save()
      render ...
    end

    def setup1
      ...
    end

    def setup2
      ...
    end
  end

Pythonでこうしたい。

.. code-block:: python

  class FooController(ApplicationController):
      def index(self):
          self.render(...)

      def create(self)
          user = User(self.request.get(user))
          user.put()
          render ...
      end

      @hook('before')
      def setup1(self):
          ...

      @hook('before')
      def setup2(self):
          ...

これで、呼び出したい関数にhookデコレータでマーキング出来たので、親クラスApplicationControllerに、@hook('before')で登録した関数を呼び出すための仕組みを仕込めば完成！

ってことで、hookデコレータを実装している ``hooks.py`` のソースコード。


.. code-block:: python

    import sys

    __all__ = ['hook', 'Hooks']

    class Hook(object):
        def __init__(self, timing, func):
            self.timing = timing
            self.func = func

        def __call__(self, *args, **kw):
            return self.func(self.inst, *args, **kw)

        def __get__(self, inst, class_=None):
            if inst is None:
                return self
            result = self.__class__.__new__(self.__class__)
            result.__dict__.update(self.__dict__)
            result.inst = inst
            return result


    class hook:
        def __init__(self, timing=None, hooks=None):
            caller_locals = sys._getframe(1).f_locals
            if hooks is None:
                hooks = caller_locals.get('hooks')
            if hooks is None:
                hooks = caller_locals['hooks'] = Hooks()
            self.hooks = hooks
            self.timing = timing

        def __call__(self, func):
            hook = Hook(self.timing, func)
            self.hooks.append(hook)
            return hook


    class Hooks(object):
        def __init__(self, *hooks):
            self._hooks = hooks

        def __iter__(self):
            return iter(self._hooks)

        def __len__(self):
            return len(self._hooks)

        def append(self, hook):
            self._hooks += (hook,)

        @classmethod
        def exec_hooks(klass, obj, timing=None):
            [x() for x in obj.hooks if timing in [None, x.timing]]

        # TODO need test
        def __add__(self, other):
            return self.__class__(*(self._hooks + other._hooks))

        def copy(self):
            return self.__class__(*self._hooks)

        def __get__(self, inst, class_):
            if inst is None:
                return self
            return self.__class__(*[a.__get__(inst) for a in self._hooks])



使い方、兼、テストコード。

.. code-block:: python

    import unittest
    from hooks import hook, Hooks

    class HooksTest(unittest.TestCase):
        def test_register_hook(self):
            class Base(object):
                @hook()
                def func1(self):
                    pass
            obj = Base()
            self.assertEqual(1, len(obj.hooks))

        def test_call_func(self):
            class Base(object):
                value = 0
                @hook()
                def func1(self):
                    self.value = 1
            obj = Base()
            Hooks.exec_hooks(obj)
            self.assertEqual(1, obj.value)

        def test_hooks_does_not_inherit(self):
            class Base(object):
                value1 = 0
                @hook()
                def func1(self):
                    self.value1 = 1
            class Derive(Base):
                value2 = 0
                @hook()
                def func2(self):
                    self.value2 = 2
            obj = Derive()
            Hooks.exec_hooks(obj)
            self.assertEqual(0, obj.value1) # value1 was inherited, but not hooked
            self.assertEqual(2, obj.value2)

        def test_hooks_can_inherit(self):
            class Base(object):
                value1 = 0
                @hook()
                def func1(self):
                    self.value1 = 1
            class Derive(Base):
                hooks = Base.hooks.copy()
                value2 = 0
                @hook()
                def func2(self):
                    self.value2 = 2
            obj = Derive()
            Hooks.exec_hooks(obj)
            self.assertEqual(1, obj.value1)
            self.assertEqual(2, obj.value2)

            obj = Base()
            Hooks.exec_hooks(obj)
            self.assertEqual(1, obj.value1)
            self.assert_(not hasattr(obj, 'value2'))


        def test_inherited_brother_hooks_must_not_pollution(self):
            class Base(object):
                value1 = 0
                @hook()
                def func1(self):
                    self.value1 = 1
            class DeriveA(Base):
                value2 = 0
                @hook()
                def func2(self):
                    self.value2 = 2
            class DeriveB(Base):
                value3 = 0
                @hook()
                def func3(self):
                    self.value3 = 3
        
            obj = Base()
            Hooks.exec_hooks(obj)
            self.assertEqual(1, obj.value1)
            self.assert_(not hasattr(obj, 'value2'))
            self.assert_(not hasattr(obj, 'value3'))

            obj = DeriveA()
            Hooks.exec_hooks(obj)
            self.assertEqual(0, obj.value1) # value1 was inherited, but not hooked
            self.assertEqual(2, obj.value2)
            self.assert_(not hasattr(obj, 'value3'))

            obj = DeriveB()
            Hooks.exec_hooks(obj)
            self.assertEqual(0, obj.value1) # value1 was inherited, but not hooked
            self.assert_(not hasattr(obj, 'value2'))
            self.assertEqual(3, obj.value3)

        def test_inherit_hooks_must_not_pollution(self):
            class Base(object):
                value1 = 0
                @hook()
                def func1(self):
                    self.value1 = 1
            class DeriveA(Base):
                hooks = Base.hooks.copy()
                value2 = 0
                @hook()
                def func2(self):
                    self.value2 = 2
            class DeriveB(Base):
                value3 = 0
                @hook()
                def func3(self):
                    self.value3 = 3
        
            obj = DeriveB()
            Hooks.exec_hooks(obj)
            self.assertEqual(0, obj.value1) # value1 was inherited, but not hooked
            self.assertEqual(3, obj.value3)
            self.assert_(not hasattr(obj, 'value2'))

        def test_register_named_hooks(self):
            class Base(object):
                value1 = 0
                value2 = 0
                value3 = 0
                @hook()
                def func1(self):
                    self.value1 = 1
                @hook('foo')
                def func2(self):
                    self.value2 = 2
                @hook('bar')
                def func3(self):
                    self.value3 = 3
        
            obj = Base()
            Hooks.exec_hooks(obj)
            self.assertEqual(1, obj.value1)
            self.assertEqual(2, obj.value2)
            self.assertEqual(3, obj.value3)

            obj = Base()
            Hooks.exec_hooks(obj, 'foo')
            self.assertEqual(0, obj.value1)
            self.assertEqual(2, obj.value2)
            self.assertEqual(0, obj.value3)

            obj = Base()
            Hooks.exec_hooks(obj, 'bar')
            self.assertEqual(0, obj.value1)
            self.assertEqual(0, obj.value2)
            self.assertEqual(3, obj.value3)

            obj = Base()
            Hooks.exec_hooks(obj, 'baz')
            self.assertEqual(0, obj.value1)
            self.assertEqual(0, obj.value2)
            self.assertEqual(0, obj.value3)


    def test_suite():
        return unittest.TestSuite((
            TestSuite(HooksTest),
        ))

    if __name__ == '__main__':
        unittest.main()

``@hook`` デコレータを使うと、使ったクラスのクラス変数に勝手にhooksを追加します。あしからず。

今回、このコードを理解するために、frameと__get__の仕組みを勉強しました。先人のコード(今回はzope.formlib)は勉強になるね。


.. :extend type: text/html
.. :extend:


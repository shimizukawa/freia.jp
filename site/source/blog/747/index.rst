:date: 2011-01-23 17:20:00
:categories: ['python']
:body type: text/x-rst

=====================================================================
2011/01/23 PyPIアップロードでありがちなreSTがHTMLにならない問題の対策
=====================================================================

*Category: 'python'*

昨日の `(第4回)Python mini hack-a-thon`_ で@t2yが `多言語翻訳サポートツール ikazuchi`_ でPyPIデビューを果たしたんですが、そのときにlong_descriptionに記載したreStrucutredTextのちょっとしたsyntaxエラーのせいでHTMLに変換されないままドキュメントがPyPIにアップロードされてしまいました。そこでreSTのエラーを事前にチェック方法が `PyPIデビュー — Python Hack-a-thon 4: ハンズオン v1.0 documentation`_ に書いてあると良いよね、という指摘をもらったので以下の文面をそのページに追加してみました。

.. note::

   (2011/1/23 `@t2yからの指摘 <http://twitter.com/t2y/status/28845059566731265>`_ で追加. ありがとう!)

   実際にアップロードしてPyPIのページを確認したときに、long_description
   の内容がHTMLに変換されずにそのままreSTのテキストで表示されてしまう場合、
   reSTの記述にエラーがある可能性があります。この場合、upload前にエラーが
   あるかどうかを確認しておくのがよいでしょう。

   docutils付属の `rst2html` コマンドを使って以下のように実行して
   エラーが出るかどうか確認する方法があります。

   ::

      $ python setup.py --long-description | rst2html > output.html

   または、Python2.7以降でdocutilsがインストールされている環境であれば、
   以下のコマンドのようにエラーを確認することも出来ます。問題がなければ
   *running check* だけ表示されますが、問題があれば以下のように表示されます。

   ::

      $ python setup.py check -r
      running check
      warning: check: No directive entry for "foo" in module "docutils.parsers.rst.languages.en".
      Trying "foo" as canonical directive name. (line 19)

      warning: check: Could not finish the parsing.

   もう一つの方法として、 `haufe.releaser`_  をインストールして `python setup.py check_description` のように実行する方法もありそうです(未確認)。


.. _`(第4回)Python mini hack-a-thon`: http://atnd.org/events/10194
.. _`多言語翻訳サポートツール ikazuchi`: http://pypi.python.org/pypi/ikazuchi/
.. _`PyPIデビュー — Python Hack-a-thon 4: ハンズオン v1.0 documentation`: http://www.freia.jp/taka/docs/pyhack4/pypi/index.html#check
.. _`haufe.releaser`: http://pypi.python.org/pypi/haufe.releaser/


ところで、  `多言語翻訳サポートツール ikazuchi`_ 、poファイルを半自動でGoogle/Microsoft/Yahooの翻訳APIで翻訳してくれたり、vimからその機能を呼び出してインラインで翻訳実行したりと、かなり便利なツールでした。これはvimで翻訳する人にはかなり重宝しそう。いちどお試しあれ！


.. :extend type: text/x-rst
.. :extend:


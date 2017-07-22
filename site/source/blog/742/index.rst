:date: 2010-11-24 23:55:00
:tags: Agile(XP), python, testing
:body type: text/x-rst

===============================================================
2010/11/24 Pythonでデータ定義行のファイル名と行番号を手に入れる
===============================================================

iPhone 3GS のマルチタスク切れませんか？とiOS4にしてからずっと思っている清水川です。ここのところなぜかメタなコードを作ることが多いんですが、今回、Pythonでデータ定義行のファイル名と行番号を手に入れたいと思ったのは以下のような理由からでした。

  データ定義に従ってテストするコードを書いて、テストが失敗したらそのデータ定義の行を表示したい。

たとえば以下のようなコード。

.. code-block:: python

  class FooURLTest(unittest.TestCase):

      # LINE 10
      url_test = [
          ('/search',
           {'method': 'GET', 'query': 'q=python', 'status': 200}),
          ('/login',
           {'method': 'GET', 'query': '', 'status': 200}),
          ('/login',
           {'method': 'POST', 'query': 'login=user&passwd=user',
            'status': 302}),
          ...
          ...
          ...
      ]

      ...
      ...

      def test_url(self):
          for ut in url_test:
              url, data = ut
              res = urllib.urlopen(url...)
              self.assertEqual(data['status'], res.getcode()) # LINE 200


上記のコードはURLにアクセスしてHTTPのステータスコードをチェックするよう動作します。しかし、例えば ``/login`` へのアクセスでエラーになったときに、テスト結果に表示されるのは最後のassertEqualを実行している行で、おそらく以下のような感じで表示されます::

    ======================================================================
    FAIL: test_url (tests.FooURLTest)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "tests.py", line 200, in test_url
        self.assertEqual(data['status'], res.getcode())
    AssertionError: 200 != 404

    ----------------------------------------------------------------------
    Ran 15 test in 6.131s

    FAILED (failures=1)
    

一応、test_url関数内の200行目のところで、エラーになった事は分かりますが、 ``url_test`` のどのデータ行でエラーになったかを知るには情報が足りません。url_testの各データに ``'name': '/login access with no param',`` といった感じに名前を利用者が付けておいて、assertEqualの引数に渡しておけば、とりあえず大丈夫ですが、名前付けるのが面倒だし行番号が表示された方が分かりやすいと思うわけです。（話の展開上、そう思ってくだせえ）

ところが、上記のコードのような場合に、あるデータがどの行で定義されたかを知るスマートな方法は、残念ながらPythonでは提供されていないようでした（あれば知りたい！）。そこで色々試行錯誤した結果、以下の方法で解決出来ました。


.. code-block:: python

  def factory(url, data):
      frame = sys._getframe().f_back
      data['filename'] = frame.f_code.co_filename
      data['lineno'] = frame.f_lineno
      return (url, data)

  class FooURLTest(unittest.TestCase):

      # LINE 10
      url_test = [
          factory('/search',
           {'method': 'GET', 'query': 'q=python', 'status': 200}),
          factory('/login',
           {'method': 'GET', 'query': '', 'status': 200}),
          ...
          ...

新たにfactoryという関数を導入して、その中でコールスタックをチェックして呼出元のファイル名と行番号を取得してデータに書き足しています。返値の形式は変えていないので、ある意味デコレータのように透過的に動作しつつ、辞書データにファイル名と行番号を仕込むことが出来ました。

あとはassertEqualを以下のように書けば、エラーの原因となったデータのファイル名と行番号が分かります。

.. code-block:: python

    data['actual'] = res.getcode()
    msg = "Expect=%(status)r but Actual=%(actual)r at %(filename)r line %(lineno)d" % data
    self.assertEqual(data['status'], data['actual'], msg)

テストに失敗するとこんな感じになるはず::

    ======================================================================
    FAIL: test_url (tests.FooURLTest)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "tests.py", line 200, in test_url
        self.assertEqual(data['status'], data['actual'], msg)
    AssertionError: Expect=200 but Actual=404 at 'tests.py' line 15

    ----------------------------------------------------------------------
    Ran 15 test in 6.131s

    FAILED (failures=1)
    

これでURLテストパターンがたくさんあってテスト失敗したときにも、原因となるURLテスト定義がどれかすぐに分かるようになるので、エラーのたびにイライラすることが無くなりますね！ヒャッホウ！


.. :extend type: text/x-rst
.. :extend:



.. :trackbacks:
.. :trackback id: 2010-12-01.8663231772
.. :title: [Python]Pythonでデータ定義行のファイル名と行番号を手に入れる
.. :blog name: atsuoishimotoの日記
.. :url: http://d.hatena.ne.jp/atsuoishimoto/20101130/1291130861
.. :date: 2010-12-01 00:27:47
.. :body:
..  ふと思いついたので書いておく。 Pythonでデータ定義行のファイル名と行番号を手に入れる - 清水川Web では、Pythonでデータの定義位置を記録する方法として、データ生成用の関数を作ってその中でデータの定義位置を記録する方式が提案されている。 このようにデータの定義
.. 
.. :trackbacks:
.. :trackback id: 2010-12-02.2326312907
.. :title: [python]pythonで__line__を使う
.. :blog name: yanolabの日記
.. :url: http://d.hatena.ne.jp/yanolab/20101202/1291261115
.. :date: 2010-12-02 12:40:34
.. :body:
..  データの定義位置を取得したいみたいなことを清水川さんのページで見た。pythonにはC言語のマクロみたいに__line__がないので、frameオブジェクトからファイル行数取ってとかを関数でやるのが一般的みたい。また、atsuoishimotoの日記の記事では、簡易DSLみたいな感じで実装
.. 

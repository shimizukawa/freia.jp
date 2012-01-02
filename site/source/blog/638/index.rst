:date: 2009-05-27 10:00:08
:categories: ['Zope']
:body type: text/x-rst

=====================================================================
2009/05/27 Zope-2.12.0b2 がWindowsでは壊れたrunzope.batを生成する問題
=====================================================================

*Category: 'Zope'*

Zope-2.12.0b2 のバグレポを出してみました。

 * `Bug #380780 in Zope 2: “Zope2.12.0b2 generate broken runzope.bat on Windows.”`_

問題の詳細はさておき、原因はWindowsのcmd.exeが以下の書式でエラーになってしまうところにあります。

.. topic:: 失敗する
  :class: dos

  | C:\> cmd.exe /C "python" -c "print 'foo'"

``os.popen`` とか ``os.system`` とかで os.system('''"python" -c "print 'foo'"''') としたときに上記の失敗パターンになってしまうようで、cmd.exeで直接以下のように実行しても再現しません。

.. topic:: 成功する
  :class: dos

  | C:\> "python" -c "print 'foo'"
  | foo

この問題、1ヶ月くらい前から気づいていたんですが再現方法が分からなくて、今日ようやくレポートできました（変な英語書いてないか、いっつも心配ですが...）。

で、肝心の解決方法が思いつかない訳ですが‥‥。cmd.exeに渡す文字列に""が複数セット出てくるのが問題なんだろうとは想像してますが、どうすればいいんだろ？出来ればunix上のpopenと互換性のある修正方法があるといいなぁ。

.. _`Bug #380780 in Zope 2: “Zope2.12.0b2 generate broken runzope.bat on Windows.”`: https://bugs.launchpad.net/zope2/+bug/380780

追記
----

``cmd.exe /?`` に書いてあった。

::
    1.  次のすべての条件に一致する場合、コマンド ラインの引用符が有効になり
        ます:

        - /S スイッチがない
        - 引用符が 1 組ある
        - 引用符の中に特殊文字がない
          (特殊文字は &<>()@^| です)
        - 引用符の中に 1 つ以上のスペースがある
        - 引用符の中の文字列が、実行可能ファイルの名前である

    2.  最初の文字が引用符であるにも関わらず上の条件に一致しない場合は、最初
        の引用符とコマンド ラインの最後の引用符が削除され、最後の引用符の後
        のテキストが有効になります。


やってみた。

.. topic:: 成功しちゃった
  :class: dos

  | C:\> cmd.exe /C ""python" -c "print 'foo'""
  | foo

えぇー？


.. :extend type: text/html
.. :extend:

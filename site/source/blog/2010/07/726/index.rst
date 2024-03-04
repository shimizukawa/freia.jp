:date: 2010-07-18 12:51:53
:tags: python, Windows

==================================================================================
Windowsでpyreadline-1.6を使うとCtrl+H押下で文字削除出来ない問題のパッチ
==================================================================================

Windows上のPythonでreadlineを使えるようにするパッケージ pyreadline_ 1.6 が2010/7/15にリリースされました。pyreadline-1.5ではCtrl+H押下時に以下の問題がありました。

* `Windowsでpyreadlineを使うとCtrl+H押下時にカーソルが進む`_
* `pyreadlineのパッチを修正`_

これが1.6で修正されたという通知がバグトラッカーから来たので確認してみましたが、今度はCtrl+H押下時に、文字削除もカーソル移動も何も起きなくなりました。うーん、問題は修正されたかも知れないですが、機能も減っちゃってますね。

ということで、さっそく1.6に対する修正パッチを作成してバグトラッカーに登録しておきました。 https://bugs.launchpad.net/pyreadline/+bug/491941

以下がそのパッチです::

    --- pyreadline-1.6/keysyms/keysyms.py.orig
    +++ pyreadline-1.6/keysyms/keysyms.py
    @@ -117,7 +117,12 @@
         meta = (state & (1+2)) != 0
         shift = (state & 0x10) != 0
         if control and not meta:#Matches ctrl- chords should pass keycode as char
    -        char = chr(keycode)
    +        if keycode in (0x48, 0x4d, 0x68, 0x6d):
    +            keycode = ord(char)
    +            control = False
    +            shift = False
    +        else:
    +            char = chr(keycode)
         elif control and meta:  #Matches alt gr and should just pass on char
             control = False
             meta = False

さて、これはいつになったら直るかなー。


.. _pyreadline: http://pypi.python.org/pypi/pyreadline
.. _`Windowsでpyreadlineを使うとCtrl+H押下時にカーソルが進む`: http://www.freia.jp/taka/blog/690
.. _`pyreadlineのパッチを修正`: http://www.freia.jp/taka/blog/706


.. :extend type: text/x-rst
.. :extend:


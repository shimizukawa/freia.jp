:date: 2008-05-20 00:27:15
:tags: python
:body type: text/x-rst

==================================================================
2008/05/20 文字コード判定して一括でuft-8に変換するPythonスクリプト
==================================================================

utf-8でのHTML作成を依頼したらEUC-JPで送られてきたので自分で変換してしまう。findとnkfを組み合わせれば良いんだろうけど、とりあえず手元にWindowsしか無かったんでPythonで作ってしまった。

カレントディレクトリ以下のテキストと思われるファイルを全てutf-8に変換する。文字コード判定というかトライ＆エラー方式。
バイナリファイルは変換に失敗したらskipするという手法。画像ファイルなんかはまあ大丈夫だろうけど、誤変換しない保証はない。・・・怖。

.. code-block:: python

    import os, sys
    
    def guess_charset(data):
        f = lambda d, enc: d.decode(enc) and enc
    
        try: return f(data, 'utf-8')
        except: pass
        try: return f(data, 'shift-jis')
        except: pass
        try: return f(data, 'euc-jp')
        except: pass
        try: return f(data, 'iso2022-jp')
        except: pass
        return None
    
    def conv(data):
        charset = guess_charset(data)
        u = data.decode(charset)
        return u.encode('utf-8')
    
    for dirpath, dirs, files in os.walk(os.getcwd()):
        for fn in files:
            path = os.path.join(dirpath, fn)
            fobj = file(path, 'rU')
            data = fobj.read()
            fobj.close()
            try:
                data = conv(data)
            except:
                print path, "-> skip"
                continue
            fobj = file(path, 'wU')
            fobj.write(data)
            fobj.close()
            print path, "-> converted"


.. :extend type: text/html
.. :extend:



.. :comments:
.. :comment id: 2008-05-20.8639529179
.. :title: Re:文字コード判定して一括でuft-8に変換するPythonスクリプト
.. :author: jack
.. :date: 2008-05-20 13:31:05
.. :email: 
.. :url: 
.. :body:
.. うぁ、.orig とか残さなくていいの？
.. まぁ、オリジナルのzip とかあるんでしょうけど。
.. 
.. :comments:
.. :comment id: 2008-05-20.6290743498
.. :title: Re:文字コード判定して一括でuft-8に変換するPythonスクリプト
.. :author: しみずかわ
.. :date: 2008-05-20 14:00:29
.. :email: 
.. :url: 
.. :body:
.. > うぁ、.orig とか残さなくていいの？
.. 
.. まあそれはフルコピーがある前提で。。
.. 
.. :trackbacks:
.. :trackback id: 2008-05-20.6678297840
.. :title: [Python][Mercurial]巡回
.. :blog name: 常山日記
.. :url: http://d.hatena.ne.jp/johzan/20080520/1211274627
.. :date: 2008-05-20 18:11:09
.. :body:
..  GoogleのソースレビューシステムMondrianのオープンソース版「Rietveld」 CherryPy 3.1.0rc1 PyFileMaker 2.5 pyRuby-Python-Bridge 1.5 bzr 1.5 文字コード判定して一括でuft-8に変換するPythonスクリプト [python] sitecustomize.pyを設定しない運動その１(Pythonで日本語
.. 

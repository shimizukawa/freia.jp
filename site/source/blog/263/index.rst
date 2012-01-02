:date: 2005-10-24 10:14:52
:categories: ['Zope', 'python']
:body type: text/x-rst

==============================================
2005/10/24 「IBMのPCではZopeが動かない」を回避
==============================================

*Category: 'Zope', 'python'*

先日買ったIBMのノート(X40)でZope2.7と2.8が動かなかった。lib/python/DateTime が datetime をimportしようとしてはまっているらしい。

そうか、Windowsだから大文字小文字が判別できないのか。とか思いつつ環境変数とかを調べていたら、 PYTHONCASEOK なるものを発見。これが定義されているとPythonはモジュールのインポート時に大文字小文字を区別しなくなるらしい。そしてIBMノートには最初からPython(2.2)が入っている関係か、PYTHONCASEOK=1という環境変数が入っていた。

システム設定から、PYTHONCASEOKと、ついでにPython2.2へのパス設定を削除したらちゃんとZope動いてくれた。よかったよかった。

１時間も悩んじゃったよ‥‥。

# http://zope.jp/download/ に書いてあるなぁ...


.. :extend type: text/plain
.. :extend:


.. :comments:
.. :comment id: 2005-11-28.5242515412
.. :title: Re: 「IBMのPCではZopeが動かない」を回避
.. :author: Terapyon
.. :date: 2005-10-24 16:35:00
.. :email: 
.. :url: 
.. :body:
.. 知人のマシンで、この現象でした。何で「datetime」で引っかかるのだ・・と思っていました。さっそくやってみたいと思います。
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.5243656551
.. :title: Re: 「IBMのPCではZopeが動かない」を回避
.. :author: 清水川
.. :date: 2005-10-25 10:23:56
.. :email: 
.. :url: 
.. :body:
.. 
.. 
.. 
.. :comments:
.. :comment id: 2005-12-20.0654861680
.. :title: Re:「IBMのPCではZopeが動かない」を回避
.. :author: mashu
.. :date: 2005-12-20 12:24:26
.. :email: mashu9000@gmail.com
.. :url: 
.. :body:
.. ThinkPadなのですが、動きません。runzope.batには以下のように追加しましたが
.. だめです。どうしてなんでしょう？？
.. 
.. C:\Zope-Instance\bin>type runzope.bat
.. @set PYTHON=C:\Program Files\Zope-2.8.4-final\bin\python.exe
.. @set ZOPE_HOME=C:\Program Files\Zope-2.8.4-final
.. @set INSTANCE_HOME=C:\Zope-Instance
.. @set SOFTWARE_HOME=C:\Program Files\Zope-2.8.4-final\lib\python
.. @set CONFIG_FILE=C:\Zope-Instance\etc\zope.conf
.. @set PYTHONPATH=%SOFTWARE_HOME%
.. @set ZOPE_RUN=%SOFTWARE_HOME%\Zope2\Startup\run.py
.. @set PYTHONCASEOK=
.. "%PYTHON%" "%ZOPE_RUN%" -C "%CONFIG_FILE%" %1 %2 %3 %4 %5 %6 %7
.. 
.. C:\Zope-Instance\bin>"C:\Program Files\Zope-2.8.4-final\bin\python.exe" "C:\Prog
.. ram Files\Zope-2.8.4-final\lib\python\Zope2\Startup\run.py" -C "C:\Zope-Instance
.. \etc\zope.conf"
.. Traceback (most recent call last):
..   File "C:\Program Files\Zope-2.8.4-final\lib\python\Zope2\Startup\run.py", line
..  56, in ?
..     run()
..   File "C:\Program Files\Zope-2.8.4-final\lib\python\Zope2\Startup\run.py", line
..  21, in run
..     starter.prepare()
..   File "C:\Program Files\Zope-2.8.4-final\lib\python\Zope2\Startup\__init__.py",
..  line 95, in prepare
..     self.makeLockFile()
..   File "C:\Program Files\Zope-2.8.4-final\lib\python\Zope2\Startup\__init__.py",
..  line 276, in makeLockFile
..     os.unlink(lock_filename)
.. OSError: [Errno 13] Permission denied: 'C:\\Zope-Instance\\var\\Z2.lock'
.. 
.. C:\Zope-Instance\bin>
.. 
.. :comments:
.. :comment id: 2005-12-20.6391672078
.. :title: Re:「IBMのPCではZopeが動かない」を回避
.. :author: 清水川
.. :date: 2005-12-20 12:33:59
.. :email: 
.. :url: 
.. :body:
.. Z2.lockファイルに対するアクセス権が無いみたいですが‥‥。
.. 
.. １，実はもう起動している（インストーラから入れるとWindwosのサービスに登録されるので）
.. ２，C:\Zope-Instance\var に書き込み権限がない（Administratorで作って一般ユーザーで起動しようとしたとか）
.. 
.. 
.. :comments:
.. :comment id: 2005-12-20.4146599012
.. :title: Re:「IBMのPCではZopeが動かない」を回避
.. :author: mashu
.. :date: 2005-12-20 13:53:43
.. :email: 
.. :url: 
.. :body:
.. 一応、administrator権限ユーザーでインストールして、同じユーザーで実行してたんですよ。
.. でも、Z2.lockファイルのアクセス権がありませんでした。
.. python.exeが握ってたので、解除後、コピーしたら、OKでした。
.. お騒がせしました。でもおかしいよ～（　ｐｑ）
.. 
.. :comments:
.. :comment id: 2005-12-20.7349550794
.. :title: Re:「IBMのPCではZopeが動かない」を回避
.. :author: 清水川
.. :date: 2005-12-20 14:15:35
.. :email: 
.. :url: 
.. :body:
.. そうすると、やっぱり１の方じゃないかな？
.. 
.. :comments:
.. :comment id: 2005-12-20.0555275656
.. :title: Re:「IBMのPCではZopeが動かない」を回避
.. :author: mashu
.. :date: 2005-12-20 16:00:57
.. :email: 
.. :url: 
.. :body:
.. そうだったみたいです。
.. 勝手に起動されてたんだ。
.. 

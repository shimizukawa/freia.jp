:date: 2007-10-25 01:13:53
:categories: ['python', 'turbogears']
:body type: text/x-rst

================================================================
2007/10/25 ソースコード探訪：turbogears.toolbox.shell.WebConsole
================================================================

`turbogears.toolbox.shell.WebConsole`_ クラスのコードを読む。
Web画面上でPython対話コンソール(InteractiveShell)を実現するためのサーバー側実装コードは100行無かった！こんなに短いとは‥‥。全ては code.InteractiveConsole クラスのお力か。

で、このコードを発展させて、自分でソケットを開いてリモート対話シェルを作ってみる。

.. code-block:: python

    import sys
    import StringIO
    from code import InteractiveConsole
    import socket
    
    def init_ps():
        try:
            sys.ps1
        except AttributeError:
            sys.ps1 = '>>> '
        try:
            sys.ps2
        except AttributeError:
            sys.ps2 = '... '
    
    
    class RemoteConsole(object):
        """Remote Python interpreter"""
    
        def __init__(self):
            self.console = None
            init_ps()
    
        def process_request(self, line):
            more, output = self._process_request(line)
            return dict(more=more, output=output)
    
        def _process_request(self, line):
            myout = StringIO.StringIO()
            try:
                sys.stdout = myout
                sys.stderr = myout
                more = self.console.push(line)
            finally:
                sys.stdout = sys.__stdout__
                sys.stderr = sys.__stderr__
    
            output = myout.getvalue()
            return ( more, output.rstrip() )
    
        def new_console(self):
            locs = dict(__name__='RemoteConsole',
                        __doc__=None,
                        reload_console=self.new_console,
                        )
            self.console = InteractiveConsole(locals=locs)
    
        def connect(self):
            if not self.console:
                self.new_console()
    
        def disconnect(self):
            if self.console:
                self.console = None
    
    
    def server():
        rc = RemoteConsole()
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind(('',10000))
        s.listen(1)
        conn,addr=s.accept()
        rc.connect()
        while 1:
            data = conn.recv(1000000)
            #print 'r',len(data)
            ret = rc.process_request(data)
            ret = unicode(ret)
            #print 's',len(ret)
            conn.send(ret)
    
    
    def client():
        init_ps()
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('localhost',10000))
        more = False
        while 1:
            data = raw_input(more and sys.ps2 or sys.ps1)
            if len(data) == 0:
                data = '\n'
            s.send(data)
            ret = s.recv(1000000)
            ret = eval(ret)
            output = ret.get('output')
            more = ret.get('more', False)
            if output:
                print output
    
    
    if __name__ == '__main__':
        if len(sys.argv) == 1:
            print 'Run as server'
            server()
        else:
            print 'Run as client'
            client()
    

ちょー適当だけど、とりあえず動くだけなら出来た。97行。

このコードをtestconsole.pyとして保存して実行してみる。

.. topic:: server起動
  :class: dos

  | C:\\> python2.4 testconsole.py
  | Run as server


.. topic:: client起動
  :class: dos

  | C:\\> python2.4 testconsole.py client
  | Run as client
  | >>> a=1
  | >>> b=2
  | >>> a+b
  | 3
  | >>> def foo(n):
  | ...   return n*n
  | ...
  | >>> foo(2)
  | 4
  | >>>

見た目分かりづらいけど、ネットワーク越しにPython対話シェルもどきが動いている。この先にあるのは、パクり元のWebConsoleのネットワーク版。

Pythonで書かれたサーバーにモニタリング用ポートを開けて、好きなタイミングでサーバー稼働中のPythonプロセスで対話シェルを操作できるようになる‥‥といいなあ。モデルの状態を見たり、メモリ利用状態の調査をしたり色々できるんじゃなかろうか。

.. _`turbogears.toolbox.shell.WebConsole`: http://svn.turbogears.org/tags/1.0.3.2/turbogears/toolbox/shell.py


.. :extend type: text/html
.. :extend:



.. :comments:
.. :comment id: 2007-10-25.3756648588
.. :title: Re:ソースコード探訪：turbogears.toolbox.shell.WebConsole
.. :author: aihatena
.. :date: 2007-10-25 23:59:35
.. :email: 
.. :url: http://edocs.beasys.co.jp/e-docs/wls/docs92/config_scripting/using_WLST.html
.. :body:
.. WLS9.x以降のWLSTもそんな感じやね。
.. Jythonで動いてリモートからJMX叩いて
.. 値取り出したりメソッド実行したりできる。
.. 

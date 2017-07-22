:date: 2004-08-11 00:47:03
:categories: ['python']
:body type: text/x-rst

=======================================
2004/08/11 サーバー生存確認PythonScript
=======================================

先週からサーバーが頻繁に落ちるため、土日に新しいサーバーを構築しました。ところが新しいサーバーもなにやら調子が良くないらしく、会社から確認した感じでは朝8時～12時の間にWebやSSHの反応が無くなるようです。

そこで、cronで10分おきに記録をとり続けるScriptをPythonで書いてみました。何でもPythonで書いていればそのうち覚えるんじゃないかという目論見もあります。


.. :extend type: text/x-rst
.. :extend:

ということで、以下のコードを書いてみました::

  #!/usr/local/bin/python
  
  import os,time
  
  home = "/home/taka/log/ping/"
  
  cmd = "/usr/bin/touch " + home + time.strftime("%Y%m%d-%H%M")
  os.system(cmd)
  
  if time.localtime()[4] ということで、以下のコードを書いてみました::

  #!/usr/local/bin/python
  
  import os,time
  
  home = "/home/taka/log/ping/"
  
  cmd = "/usr/bin/touch " + home + time.strftime("%Y%m%d-%H%M")
  os.system(cmd)
  
  if time.localtime()[4] 


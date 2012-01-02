:date: 2004-08-13 00:19:26
:categories: ['Programming', 'python']
:body type: text/x-rst

================
アクセス隙間検出
================

アクセス隙間検出。悔しかったのでリベンジです。

datetimeモジュールとtimeモジュールの間でうまく連携する方法が分からなかったので、かなり泥臭い感じになってしまいました。あとprevtimeとbasetimeの初期化が‥‥。



.. :extend type: text/x-rst
.. :extend:
apacheのログから10分以上アクセスの無い時間帯を検出::

  #!/usr/local/bin/python
  
  import fileinput
  import re
  import time
  import datetime
  
  date = re.compile("(\d+/\w+/\d+:\d+:\d+:\d+)")
  prevtime = None
  basetime = None
  
  for line in fileinput.input("/var/log/httpd/freia-access.log"):
    logtime = date.search(line)
    if logtime:
      ttime = time.mktime(time.strptime(logtime.groups()[0], 
      "%d/%b/%Y:%H:%M:%S"))
      dtime = datetime.datetime.fromtimestamp(ttime)
      if not prevtime:
        prevtime = dtime
        basetime = dtime
  
      if dtime - prevtime ＜ datetime.timedelta(0,600):
        if basetime != prevtime:
          print "%s while %s" % (basetime, dtime - basetime)
        basetime = dtime

      prevtime = dtime

結果はこんな感じ::

  2004-08-12 00:31:07 while 0:32:59
  2004-08-12 01:18:19 while 0:12:00
  2004-08-12 03:17:27 while 0:42:16
  2004-08-12 04:24:20 while 0:25:58
  2004-08-12 04:50:22 while 0:19:45
  2004-08-12 05:12:41 while 0:19:16
  2004-08-12 05:46:56 while 0:13:45
  2004-08-12 06:27:23 while 0:11:36
  2004-08-12 06:46:56 while 0:25:55
  2004-08-12 07:22:50 while 0:14:44
  2004-08-12 07:48:35 while 0:14:38
  2004-08-12 08:56:30 while 1:07:35
  2004-08-12 10:28:47 while 0:23:49
  2004-08-12 12:12:04 while 0:48:02
  2004-08-12 13:15:28 while 0:44:42

やった！出来た！（笑）

結果を見ると、朝9時と正午前後あたりに外部からアクセスできていない時間帯があります。未だ原因は分かっていませんが、とりあえず定期的に外部に通信を行うようにして回避してみたいと思います。



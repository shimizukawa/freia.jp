:date: 2014-05-10 15:00
:tags:

========================================================================
Python全部入りDocker ImageのOpenSSL更新してPython3.4追加した
========================================================================

:doc:`DockerのPython全部入りコンテナを作ってました <../docker-python-image/index>` が、HeartBleed対策してPython3.4追加したものを4月12日に公開してました。


https://index.docker.io/u/shimizukawa/python-all/

* python2.4 (2.4.6-8+precise1)
* python2.5 (2.5.6-7+precise1)
* python2.6 (2.6.9-1+precise1)
* python2.7 (2.7.3-0ubuntu3.5)
* python3.1 (3.1.5-5+precise1)
* python3.2 (3.2.3-0ubuntu3.6)
* python3.3 (3.3.5-1+precise1)
* python3.4 (3.4.0-1+precise1)
* pypy (2.2.1+dfsg-1~ppa1)
* openssl 1.0.1-4ubuntu5.12


https://index.docker.io/u/shimizukawa/python-all-dev/

* python2.4 (2.4.6-8+precise1)
* python2.5 (2.5.6-7+precise1)
* python2.6 (2.6.9-1+precise1)
* python2.7 (2.7.3-0ubuntu3.5)
* python3.1 (3.1.5-5+precise1)
* python3.2 (3.2.3-0ubuntu3.6)
* python3.3 (3.3.5-1+precise1)
* python3.4 (3.4.0-1+precise1)
* pypy (2.2.1+dfsg-1~ppa1)
* python2.4-dev (2.4.6-8+precise1)
* python2.5-dev (2.5.6-7+precise1)
* python2.6-dev (2.6.9-1+precise1)
* python2.7-dev (2.7.3-0ubuntu3.5)
* python3.1-dev (3.1.5-5+precise1)
* python3.2-dev (3.2.3-0ubuntu3.6)
* python3.3-dev (3.3.5-1+precise1)
* python3.4-dev (3.4.0-1+precise1)
* pypy-dev (2.2.1+dfsg-1~ppa1)
* openssl 1.0.1-4ubuntu5.12


これ、Devの方はPillowのビルドができる程度はライブラリも入ってたほうが良いんだろうな。



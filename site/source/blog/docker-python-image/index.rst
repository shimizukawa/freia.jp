:date: 2014-01-20 21:00
:tags:
:body type: text/x-rst

==============================================
2014/01/20 Python7つ入りのDocker Imageを作った
==============================================

:doc:`../create-docker-trusted-build-image-on-the-docker-official-repository/index` で作った `shimizukawa/python-all`_ イメージは Python-2.5, 2.6, 2.7, 3.1, 3.2, 3.3, pypy を使えるようにするものでした。

しかし、gccやPythonのヘッダーファイルなどはインストールしていなかったため、バイナリビルドが必要な一部のPythonパッケージをインストールできませんでした。Dockerイメージ内でgccするのかとも思うけど、開発環境として使う場合は無いと手間ばかり増えてしまいます。


   @shimizukawa docker の python-all にそれぞれのバージョンの python-dev も入ってると嬉しい

   -- `@t2y: 9:27 - 2014年1月20日 <https://twitter.com/t2y/status/425061935810215937>`__

はい。

ということで、 `shimizukawa/python-all-dev`_ も作りました。


.. _shimizukawa/python-all: https://index.docker.io/u/shimizukawa/python-all/
.. _shimizukawa/python-all-dev: https://index.docker.io/u/shimizukawa/python-all-dev/


ちなみにDockerfileはこんな感じ::

   # Ubuntu 12.04 LTS and Python-dev package for 2.4, 2.5, 2.6, 2.7, 3.1, 3.2, 3.3, pypy
   FROM shimizukawa/python-all
   MAINTAINER Takayuki SHIMIZUKAWA "shimizukawa@gmail.com"
   RUN apt-get install -qq -y \
       python2.4-dev \
       python2.5-dev \
       python2.6-dev \
       python2.7-dev \
       python3.1-dev \
       python3.2-dev \
       python3.3-dev \
       pypy-dev


リポジトリは面倒だったので `shimizukawa/python-allと同じリポジトリ`_ のサブディレクトリにDockerfileを置きました。index.docker.ioでDockerfileの場所をリポジトリのサブディレクトリ指定が出来るので便利ですね。と思ったらどっちかのDockerfileを更新するだけで両方のイメージが作り直されちゃうので、docker pullしたときに手元にshimizukawa/python-allがあっても再度取得されちゃうんじゃないか、これ。今度から分けて置いた方が良さそうだなあ。


.. _shimizukawa/python-allと同じリポジトリ: https://github.com/shimizukawa/docker-python-all


docker-pullしてsetuptoolsインストールしてPillowビルドしたところ::

   vagrant@precise64:~$ docker pull shimizukawa/python-all-dev
   Pulling repository shimizukawa/python-all-dev
   01090c967cd6: Pulling image (latest) from shimizukawa/python-all-dev, endpoint: 01090c967cd6: Download complete
   8dbd9e392a96: Download complete
   bb43eda75d6a: Download complete
   a4f53d8ea1f7: Download complete
   b2baf39059ae: Download complete
   3aac06c352e4: Download complete
   ff8065126f78: Download complete
   9f1ead651237: Download complete
   6cd2abb1395d: Download complete
   vagrant@precise64:~$ docker run -i -t shimizukawa/python-all-dev /bin/bash
   root@8a83383f090f:/# apt-get install -y curl
   ...snip...
   root@8a83383f090f:/# curl https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py|python3.3
   ...snip...
   root@8a83383f090f:/# easy_install Pillow
   ...snip...
   Processing Pillow-2.3.0.zip
   ...snip...
   --------------------------------------------------------------------
   PIL SETUP SUMMARY
   --------------------------------------------------------------------
   version      Pillow 2.3.0
   platform     linux 3.3.3 (default, Dec 27 2013, 19:27:19)
                [GCC 4.6.3]
   --------------------------------------------------------------------
   *** TKINTER support not available
   *** JPEG support not available
   --- ZLIB (PNG/ZIP) support available
   *** LIBTIFF support not available
   *** FREETYPE2 support not available
   *** LITTLECMS2 support not available
   *** WEBP support not available
   *** WEBPMUX support not available
   --------------------------------------------------------------------
   ...snip...
   Finished processing dependencies for Pillow
   root@8a83383f090f:/#


次は、setuptools入りとかPillowの関連ライブラリ入りとか欲しくなるんだろうな。


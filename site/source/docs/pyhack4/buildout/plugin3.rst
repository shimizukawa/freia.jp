setuptoolsを使ったpluginサンプル buildout編
============================================

buildoutを使った開発の例を、setuptoolsのpluginサンプルを使って見ていきます。


前準備
------

`plugins_buildout.zip <../_static/plugins_buildout.zip>`_ を展開します::

   plugins_buildout
      +---p1/
      |   +-- setup.py
      |   +---src/
      |       +-- practice/
      |           +-- __init__.py
      |           +-- plugin1/
      |               +-- __init__.py
      +---p2/
      |   +-- setup.py
      |   +---src/
      |       +-- practice/
      |           +-- __init__.py
      |           +-- plugin2/
      |               +-- __init__.py
      |
      +---server/
          +-- bootstrap.py
          +-- buildout.cfg
          +-- setup.py
          +---src/
              +---practice
                  +-- __init__.py
                  +---server
                      +-- __init__.py

buildout環境を作成
-------------------

server/ 以下に bootstrap.py と buildout.cfg が予め用意されているので、
利用者は以下のコマンドを実行すると、環境作成が完了してしまいます::

   $ cd server
   $ python bootstrap.py
   $ bin/buildout


これで bin/run_all が作成されています。このrun_allの正体はsys.pathの調整
と実行関数の呼び出しを行う短いコードです。こういったスクリプト生成ルールは
server/setup.py の中で定義されています。

VirtualEnvを使わなくてもbuildout環境下に作成してくれるので、グローバルな
環境を汚染する心配はありません。


run_allの実行
--------------

::

   $ bin/run_all
   ## plugins call finished

plugin側の実行が行われずに終了してしまいました。
これは、buildout.cfgでpluginを含めないよう設定していたためです。

buildout.cfgを開いて、 `practice.plugin1` のコメントアウトを解除してから
もう一度 bin/buildout を実行し、run_allを実行してみて下さい。

::

   $ bin/run_all
   ## call plugin: practice.plugin1:plugin_name1
   Hello SERVER (by plugin1)

   ## plugins call finished

うまくplugin1が認識されているのが分かります。


buildoutの便利なところ
-----------------------

zc.recipe.egg の効用
~~~~~~~~~~~~~~~~~~~~
このサンプルでは buildout.cfg のdevelp行でソースコードの場所を指定
しましたが、公開しているパッケージであれば、eggsに指定するだけでPyPIから
取得してきて、pluginとして認識されるようになります。

eggキャッシュ
~~~~~~~~~~~~~~
また、パッケージとして見せたくなくなったらeggs行から取り除くかコメントアウト
すれば、pluginとして認識されなくなります。再度eggs行に追加すればまた見える
ようになりますが、このときダウンロードなどは行われず、eggsディレクトリ内
のものが再利用されます。

eggキャッシュの共有
~~~~~~~~~~~~~~~~~~~~
~/.buildout/default.cfg というファイルを作成して、以下のように記載します::

   [buildout]
   eggs-directory = /home/foo/.buildout/buildout-eggs
   download-cache = /home/foo/.buildout/buildout-downloads
   newest = false
   # index = http://pypi.python.jp/

上記の2つのフォルダは作成しておいて下さい。

この状態でbuildoutを実行するとバージョン更新をチェックせず、取得した
eggは共有のbuildout-eggsに置くようになります。これによって、繰り返し
buildoutコマンドを実行するような場合でもインターネット通信を行わないため、
高速に実行することが出来ます。また、複数のbuildout環境でeggを共有する
ため、良く使うeggはノータイムで実行することが出来るようになります。

buildout-eggsフォルダの中には、同じパッケージの別バージョンが必要に応じて
置かれていきますが、buildoutは適切なバージョンを選択してくれるので、
問題にはなりません。

複数バージョンの混在
~~~~~~~~~~~~~~~~~~~~~
プロジェクトによっては、ほとんど同じパッケージ群を使うけれども、
ごく一部だけ別バージョンを使う場合があります。テスト目的で1パッケージだけ
古いバージョンを使いたいこともあるし、あるプロジェクトでは twisted
の最新が必要だけれども他では最新だと困る場合、などです。

こうしたときに、Python標準のsite-packagesに複数バージョン入って
いるのはあまり好ましい状況ではありません。そしてたいていの場合うまく
動作しなくなります。

そこでVirtualEnvを使うわけですが、VirtualEnvでは全てのパッケージを
複製で持つ必要があるためDISK容量が大きくなってしまいますし、ちょっとした
実験のために環境を複製するのにも時間がかかってしまいます。
（2重仮想化という手もあるようですが...）

buildoutの場合、例えば以下の手順で新しい環境をforkできることになります::

   $ hg clone . ../test2
   $ cd ../test2
   $ python bootstrap.py
   $ bin/buildout

eggキャッシュを共有していてnewest=falseであれば、処理する必要があるのは
binフォルダ以下にスクリプトを生成することだけです。



plugins_buildout のその他の特徴
--------------------------------

このソースコードには他にも、名前空間パッケージの機能を使って、practiceという
1つの名前空間を3つのパッケージで扱うようにしています。




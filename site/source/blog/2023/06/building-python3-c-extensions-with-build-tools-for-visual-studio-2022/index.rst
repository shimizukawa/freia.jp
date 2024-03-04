:date: 2023-06-06 13:00:00
:tags: python, expertpython, windows

============================================================================
Python3のC拡張を Build Tools for Visual Studio 2022 でビルドする 
============================================================================

『エキスパートPythonプログラミング 改訂4版』11章「Pythonパッケージの作成と配布」では、Windows環境でPython 3のC拡張をビルドするにはVisual C++かMinGWを使う方法がある、と一言触れられています。2023年現在のお勧めツールと、インストールやビルド手順について検証を行いました。

TL;DR
============

- WindowsでPython3のC拡張をビルドするには `Build Tools for Visual Studio 2022`_ を使います
- 2023年現在ではおそらく一番良い選択肢でしょう
- このコマンドラインツールは無料で利用でき、生成したバイナリの利用や配布に制限はありません

11章「Pythonパッケージの作成と配布」の記述を検証
=====================================================

11章の原文（以下）では、「Windows環境でPython 3のC拡張をビルドするにはVisual C++かMinGWを使う方法がある」と一言触れられています。

   The C compiler used in the build process is the compiler that is the default for your operating system. For a Linux-based system or macOS, this would be ``gcc`` or ``clang`` respectively. For Windows, Microsoft Visual C++ can be used (there's a free command-line version available). The open-source project MinGW can be used as well. The compiler choice can also be configured through ``setuptools``.

しかし、2023年時点でMinGWはPython拡張ビルドのお勧めの方法とは言えません。確かに、 ``setuptools`` （というか ``distutils`` ）はMinGWをサポートしていますが、配布可能な、一般的なWindowsで動作するバイナリ配布物をMinGWで作成できないと思います。自分も2013年頃にトライしましたが、セグフォなどで安定せず諦めた記憶（ `記録`_ ）があります。（できた方は、ぜひ情報をご提供ください）。

2023年現在の一番良い選択肢は `Build Tools for Visual Studio 2022`_ です。有り難いことに、MicrosoftはVisual Studioのコマンドライン版を200x年以降ライセンスフリーで利用可能としてくれています。2014年には「Microsoft Visual C++ Compiler for Python 2.7」という、Pythonをツール名に冠したバージョンもありました。


- `[Distutils] Microsoft Visual C++ Compiler for Python 2.7 <https://mail.python.org/pipermail/distutils-sig/2014-September/024885.html>`_
- `Microsoft Visual C++ - Wikipedia <https://ja.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B>`_

それではインストールから検証していきます。

事前準備
=============

- Windows 11 (64bit)
- Python: 3.10 (amd64)
- ビルド対象コード: `Expert-Python-Programming-Fourth-Edition/Chapter 9/02 - Pure C extensions at main · PacktPublishing/Expert-Python-Programming-Fourth-Edition · GitHub`_



Pythonとコンパイラのバージョン整合性を確認
========================================================

`WindowsCompilers - Python Wiki`_ より

- Microsoft Visual C++ 14.x with Visual Studio 2022 (x86, x64, ARM, ARM64)
- Microsoft Visual C++ 14.2 standalone: Build Tools for Visual Studio 2019 (x86, x64, ARM, ARM64)
- Microsoft Visual C++ 14.2 with Visual Studio 2019 (x86, x64, ARM, ARM64)
- Microsoft Visual C++ 14.1 standalone: Build Tools for Visual Studio 2017 (x86, x64, ARM, ARM64)
- Microsoft Visual C++ 14.1 with Visual Studio 2017 (x86, x64, ARM, ARM64)
- Microsoft Visual C++ 14.0 standalone: Visual C++ Build Tools 2015 (x86, x64, ARM)
- Microsoft Visual C++ 14.0 with Visual Studio 2015 (x86, x64, ARM)

VC++ のメジャーバージョンは2015年以降ずっと14なんですね。

2023/03/04時点では、Build Tools for Visual Studio 2022 で Microsoft Visual C++ 14.3 をインストールすれば良さそうです。


Build Tools for Visual Studio 2022 のインストール
======================================================================

Build Tools for Visual Studio 2022 を入手します。

* https://visualstudio.microsoft.com/visual-cpp-build-tools/

.. figure:: step1.*
   :width: 80%

   Microsoft C++ Build Tools - Visual Studio

.. topic:: Visual Studio Tools のダウンロードサイト

   https://visualstudio.microsoft.com/ja/downloads/ からもダウンロードできますが、 ``Build Tools for Visual Studio 2022`` のダウンロードは、サイト上の微妙に見つけづらいところに隠れています。
   検索ボックスに ``Build Tools`` と入力して見つけてください。


.. figure:: step2.*
   :width: 80%

   Visual Studio Installer 起動

.. figure:: step3.*
   :width: 80%

   Visual Studio Installer 準備中

.. figure:: step4.*
   :width: 80%

   インストール対象の選択

インストール対象がたくさんあり、かつ、コンパイラも似たようなものがたくさんあります。必要最小限の選択をするために、 `WindowsCompilers - Python Wiki`_ を読んで試行錯誤しました。 `WindowsCompilers - Python Wiki`_ には以下の様に書かれています。

#. Install Microsoft Visual Studio 2022 (or later).
#. Install the Python development workload and the optional Python native development tools option.
#. Install the latest Windows SDK (under Native development in the installer).
#. Optional: Set $env:PlatformToolset to your toolset version before building, if it doesn't detect it.
#. Update to the latest setuptools Python package version.

このうち、1と3が必要でした。2はPython自体の開発に必要なオプションなので今回は不要です。
以下の様に選択しました。

.. figure:: step5.*
  :width: 80%

  個別のコンポーネントタブで個別選択

  - MSVC v143 - VS 2022 C++ x64/x86 ビルドツール（最新）
  - Windows 11 SDK (10.0.22000.0)

私は初め、 ``(最新)`` ではなく一番新しそうなバージョン番号が明記されている ``(v14.35-17.5)`` をインストールしましたが、これだと後で必要な ``vcvarsall.bat`` がインストールされていないことが分かり、NGでした。

構成ファイル ``.vsconfig`` は以下の様になりました。これを保存して、「構成ファイルのインポート」で読み込んでも良いと思います。

.. code-block:: json

   {
     "version": "1.0",
     "components": [
       "Microsoft.VisualStudio.Component.Roslyn.Compiler",
       "Microsoft.Component.MSBuild",
       "Microsoft.VisualStudio.Component.CoreBuildTools",
       "Microsoft.VisualStudio.Workload.MSBuildTools",
       "Microsoft.VisualStudio.Component.VC.Tools.x86.x64",
       "Microsoft.VisualStudio.Component.Windows11SDK.22000",
       "Microsoft.VisualStudio.Component.VC.14.35.17.5.ATL.Spectre",
       "Microsoft.VisualStudio.Component.VC.14.35.17.5.MFC.Spectre"
     ]
   }

インストールが完了したら、インストール先ディレクトリの ``C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build`` を確認します。

.. figure:: step6.*
   :width: 80%

   vcvarsall.bat インストールされている

ここに ``vcvarsall.bat`` がインストールされていればOKです。
``vcvarsall.bat`` は、PythonのC拡張をビルドする際に ``distutils`` から呼び出されます。

呼び出しているコードはこちら。
https://github.com/pypa/distutils/blob/4435cec31b8eb5712aa8bf993bea3f07051c24d8/distutils/msvc9compiler.py#L274-L276

インストールはこれで完了です。


Python3 C拡張のビルド
===================================

ビルドするためには、 ``x64 Native Tools Command Prompt for VS 2022`` でコマンドラインを起動する必要があります。

.. figure:: step7.*
  :width: 80%

  VC環境のコマンドラインを起動

キャプチャ画像にあるように、 ``Command Prompt for VS 2022`` はいくつか種類があります。今回はx64向けにビルドするため、 ``x64 Native`` を選択しました。

今回のサンプルコード `Expert-Python-Programming-Fourth-Edition/Chapter 9/02 - Pure C extensions at main · PacktPublishing/Expert-Python-Programming-Fourth-Edition · GitHub`_ には ``setup.py`` が用意されています。以下の様に実行します。

``python setup.py build``

.. figure:: step8.*
   :width: 80%

   ビルド成功

無事ビルドができました。

ここでエラーになる場合は、x64かx86かの違いかもしれません。
その場合は ``--plat-name`` を指定するか、最初に起動するVC環境のコマンドラインを変更する必要があります。
これについて `コラム`_ で後述します。

また、 ``setup.py build`` を使わない方法として ``python -m build`` があります。これも `コラム`_ にて紹介します。

Python3 C拡張の実行
===================================

ビルドされたpydのあるディレクトリに移動してimportして実行すると、 ``fibonacci`` 関数が無事動きました！

.. figure:: step9.*

  C拡張のfibonacciがうごいたぁぁーー！！


やりましたね！

参考情報
===========

- `BUG distutils.msvccompiler does not work with any currently available VS build tools · Issue #3329 · pypa/setuptools · GitHub`_

  - ``distutils.msvccompiler`` がVS build tools で動作しないよ、というバグ報告
  - 私（清水川）はこうやったらうまくいったよ、というコメントをしておきました

- `Windows での Python 2.7, 3.4, 3.5 の拡張モジュールビルド環境 - Qiita <https://qiita.com/methane/items/2210712763b91e75fdf0>`_

  - 2014年当時に、エキPy翻訳者でPythonのコミッターであるmethaneさんが書かれた記事があります。当時もWindowsでのバイナリビルドは情報が不足しており、こういった記事は有り難いものでした。

- `Build Tools for Visual Studio 2022 で Python3のC拡張をビルドする（失敗編）`_

  - 失敗の記録です

- `visualstudio-docs/workload-component-id-vs-professional.md at main · MicrosoftDocs/visualstudio-docs · GitHub`_ 

  - Python development 向けのコンパイラバージョンはこれ、みたいな情報？調べてる途中で見つけた資料だけど、役に立ったかどうかは忘れました。


コラム
===================================

.. topic:: ``--plat-name`` オプションについて。

   コマンドラインを起動する際に、 ``Developer Command Prompt for VS 2022`` や ``Developer PowerShell for VS 2022`` で起動すると32bit版と64bit版どちらもビルド可能な設定でコマンドラインが起動します。この環境では、Python拡張のビルド時に明示的にx86なのかx64なのかを指定する必要があります。
   
   Pythonが64bit版なら自動的に64bit版が選択される・・・、という実装にはなっていないようです。
   オプションを指定せず ``python setup.py build`` を実行すると、以下の様にエラーになりました。

   .. figure:: step8-error.*
      :width: 80%
   
      ビルド失敗
   
   コンパイルは問題なさそうですが、リンクで落ちています。今回は64bit版のPythonをインストールしていますが、x86 (32bit)をリンクしようとしてるようです。なるほどーー。

   オプション指定を忘れて困らないように、 ``setup.cfg`` にオプションを保存しておくこともできます。

   .. code-block:: doscon

      C:> python3.10 setup.py saveopts build --plat-name=win-amd64
      running saveopts
      Writing setup.cfg
      running build
      running build_ext
    
      C:> python3.10 setup.py saveopts bdist --plat-name=win-amd64
      running saveopts
      Writing setup.cfg
      running bdist
      running bdist_dumb
      running build
      running build_ext

   ``setup.cfg`` には以下の様に設定されます。

   .. code-block:: ini

      [build]
      plat_name = win-amd64
      
      [bdist]
      plat_name = win-amd64

   ``--plat-name`` オプションについて詳しくは、公式ドキュメントを参照してください。

   - `ビルド済み配布物を作成する — Python 3.11.2 ドキュメント <https://docs.python.org/ja/3/distutils/builtdist.html#cross-compiling-on-windows>`_

.. topic:: ``python -m build`` でのビルド

   :pep:`517` でのビルドも出来ました。

   .. code-block:: doscon

      C:> python3.10 -m pip install build
      C:> python3.10 -m build -n
      * Getting build dependencies for sdist...
      ...
      ライブラリ build\temp.win-amd64-cpython-310\Release\fibonacci.cp310-win_amd64.lib とオブジェクト build\temp.win-amd64-cpython-310\Release\fibonacci.cp310-win_amd64.exp を作成中
      コード生成しています。
      コード生成が終了しました。
      ...
      Successfully built fibonacci-0.0.0.tar.gz and fibonacci-0.0.0-cp310-cp310-win_amd64.whl
 
   （ログの詳細は scrapbox_ にまとめたのでそちらを参照ください）

.. topic:: 清水川とWindows向けバイナリビルド

   2000年代はバイナリ拡張モジュールを自分でビルドする時代でしたが、WindowsでのビルドはLinuxやUNIX系環境のように簡単ではありませんでした。自分は以前からWindows上でのコンパイルなどをしていたこともあり、当時PythonやRubyのWindowsバイナリ拡張をビルドして公開していました。

   - 2005年 :doc:`/blog/2005/09/250/index`
   - 2007年 :doc:`/blog/2007/01/392/index`
   - 2011年 :doc:`/blog/2011/05/758/index`
   - 2011年 :doc:`/blog/2011/05/759/index`
   - 2011年 :doc:`/blog/2011/09/762/index`
   - 2013年 :doc:`/blog/2013/02/python-win32-binary-building-and-x64-cross-compiling-on-32bit-platform/index`

   私（清水川）は2011年からの3年間ほど、Pillow （Pythonの画像処理ライブラリ）のWindows向けバイナリをビルドしてPyPIに上げる担当をしていたことがあります。以下は Pillow メンテナの Alex Clark のblog ``The Story of Pillow`` からの引用です（元サイトがなくなっており、Web Archiveから引用しました）。

   https://web.archive.org/web/20130424073236/http://blog.aclark.net/2013/03/15/the-story-of-pillow/

     A little over a year later on 2011-09-08, Takayuki Shimizukawa uploaded the first Windows (win32) eggs. Since then, every Pillow release included Windows eggs thanks to Takayuki. And on 2013-02-02, the first 64-bit Windows eggs (amd64) were uploaded to PyPI by Takayuki.

     DeepL翻訳: それから1年ちょっと経った2011-09-08に、清水川貴之が初めてWindows（win32）のeggをアップロードしました。それ以来、TakayukiのおかげでPillowのリリースには必ずWindowsのeggが含まれています。そして2013-02-02、Takayukiによって最初の64-bit Windows egg (amd64) がPyPIにアップロードされました。

   - 2011-09-08 のPillow配布物 https://pypi.org/project/Pillow/1.7.5/#files

   その後、 https://github.com/python-pillow/Pillow/issues/28 などで64bit版バイナリを作ろうという動きがあり、たしか PyCon US 2013 で64bit版ビルドができるように整備されたのだったと思います。

.. リンク

.. _scrapbox: https://scrapbox.io/shimizukawa/Build_Tools_for_Visual_Studio_2022_%E3%81%A7_Python3%E3%81%AEC%E6%8B%A1%E5%BC%B5%E3%82%92%E3%83%93%E3%83%AB%E3%83%89%E3%81%99%E3%82%8B

.. _Build Tools for Visual Studio 2022: https://visualstudio.microsoft.com/ja/downloads/

.. _Build Tools for Visual Studio 2022 で Python3のC拡張をビルドする（失敗編）: https://scrapbox.io/shimizukawa/Build_Tools_for_Visual_Studio_2022_%E3%81%A7_Python3%E3%81%AEC%E6%8B%A1%E5%BC%B5%E3%82%92%E3%83%93%E3%83%AB%E3%83%89%E3%81%99%E3%82%8B%EF%BC%88%E5%A4%B1%E6%95%97%E7%B7%A8%EF%BC%89

.. _visualstudio-docs/workload-component-id-vs-professional.md at main · MicrosoftDocs/visualstudio-docs · GitHub: https://github.com/MicrosoftDocs/visualstudio-docs/blob/main/docs/install/includes/vs-2022/workload-component-id-vs-professional.md

.. _BUG distutils.msvccompiler does not work with any currently available VS build tools · Issue #3329 · pypa/setuptools · GitHub: https://github.com/pypa/setuptools/issues/3329#issuecomment-1454935255

.. _WindowsCompilers - Python Wiki: https://wiki.python.org/moin/WindowsCompilers

.. _Expert-Python-Programming-Fourth-Edition/Chapter 9/02 - Pure C extensions at main · PacktPublishing/Expert-Python-Programming-Fourth-Edition · GitHub: https://github.com/PacktPublishing/Expert-Python-Programming-Fourth-Edition/tree/main/Chapter%209/02%20-%20Pure%20C%20extensions

.. _記録: https://github.com/python-pillow/Pillow/issues/28#issuecomment-12700551

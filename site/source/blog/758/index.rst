:date: 2011-05-04 15:40:00
:categories: ['Windows', 'ruby']
:body type: text/x-rst

============================================
MeCab-0.98 ruby binding for Windows のビルド
============================================

Rubyで MeCab_ を使用するには `MecCab-rubyバインディング`_ を使用しますが、バンディングはビルド済みのものが提供されていないので、自分でビルドする必要があります。Linuxや*BSDならそれほどはまらないですが(実際CentOSでは簡単に出来た)、Windowsではコンパイル環境があってもはまったので、バインディングビルド手順をメモしておきます(完成物はこちら:  `mecab-ruby-0.98-win32-binary-20110504.zip`_)。

.. _MeCab: http://mecab.sourceforge.net/
.. _`MecCab-rubyバインディング`: http://sourceforge.net/projects/mecab/files/mecab-ruby/0.98/


バインディングをビルドせずに何とかする代替案
----------------------------------------------
バインディングをビルドしようとして調べたら、代替案が色々あったのでまとめてみました。

bindingをビルドせずにプロセス呼び出しで使う例
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ビルドするのが(実施や維持などが)難しいということで、shell経由で外部呼び出しして結果を手に入れる方法もいくつかあります。shell経由はデータ長(2047文字?)の上限など問題がありそうですが、テンポラリファイル経由でデータを渡す事でなんとかしているパターンもありますね。

* http://d.hatena.ne.jp/kenkitii/20060705/p1
* http://kyow.cocolog-nifty.com/blog/2009/05/windows-mecab-r.html
* http://rubyegginer.blogspot.com/2010/08/mecabrubywindows.html


libmecab.dllを直接呼び出す
~~~~~~~~~~~~~~~~~~~~~~~~~~~
データ長(2047文字?)問題を回避するスマートな方法として、libmecab.dllを使う方法も提案されてました。libmecab.dllは `MeCab-0.98 for Windows (mecab-win32)`_ に同梱されています。

* http://nlp.sfc.keio.ac.jp/~aihara/nlp.html
* http://kyow.cocolog-nifty.com/blog/2009/05/windows-mecab-r.html
* http://kitykey.jugem.jp/?eid=21
* `http://chezou.wordpress.com/2010/10/13/mecabをruby-1-9-2-on-windows764bit版で使う方法/`_

.. _`MeCab-0.98 for Windows (mecab-win32)`: http://sourceforge.net/projects/mecab/files/mecab-win32/
.. _`http://chezou.wordpress.com/2010/10/13/mecabをruby-1-9-2-on-windows764bit版で使う方法/`: http://chezou.wordpress.com/2010/10/13/mecab%E3%82%92ruby-1-9-2-on-windows764bit%E7%89%88%E3%81%A7%E4%BD%BF%E3%81%86%E6%96%B9%E6%B3%95/


バインディングをビルドする手順
-------------------------------

この記事で対象にしているバージョン

* WindowsXP, 7 (95以降共通と思われる)
* ActiveRuby-1.8.7-p300
* MeCab-0.98
* mecab-ruby-0.98.tar.gz
* VisualStudio 6

環境の用意
~~~~~~~~~~~~
Windowsを用意します。そこにRuby-1.8.7(ActiveRuby), MeCab-0.98, VisualStudio6をインストールしておきます。


Ruby-1.8がVisualStudio6でビルドされているのでVS2008で動くようにする例
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ruby-1.8\lib\ruby\1.8\i386-mswin32\config.h を見ると ``_MSC_VER: 1200 is expected.`` と書かれていますね。VS6は無料で環境構築できないため、この時点でバインディングのビルドを断念する人も居そうです。この部分を書き換えて何とかしている例がいくつかありました。

* http://programming.jugglershu.net/programming/articles/rubyext.html
* http://ronspace.cocolog-nifty.com/blog/2009/02/ruby-pg-windows.html

‥いいのかな？動くならそれでもいいんでしょう。この記事ではVisualStudio6で話を進めます。

mecab-ruby-0.98.tar.gz を展開してextconf.rbを書き換え、Makefileを作成する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Step1**

mecab-ruby-0.98.tar.gz に同梱されているextconf.rbには以下のような行があります::

    `mecab-config --libs-only-l`.chomp.split.each { | lib |

しかしWindowsではMeCabをインストールしてもmecab-configが無いのでこのままでは動きません。そこで以下のように書き換えます。

`元のextconf.rb`::

    require 'mkmf'

    mecab_config = with_config('mecab-config', 'mecab-config')
    use_mecab_config = enable_config('mecab-config')

    `mecab-config --libs-only-l`.chomp.split.each { | lib |
      have_library(lib)
    }

    $CFLAGS += ' ' + `#{mecab_config} --cflags`.chomp

    have_header('mecab.h') && create_makefile('MeCab')


`書き換えたextconf.rb`::

    require 'mkmf'

    $CFLAGS += ' -IC:\Develop\Mecab\sdk'
    $LOCAL_LIBS += ' libmecab.lib'
    $LIBPATH << 'C:\Develop\Mecab\sdk'

    have_header('mecab.h') && create_makefile('MeCab')

上記は、MeCabが ``C:\Develop\Mecab\`` にインストールされている場合です。それ以外にインストールしている場合は適宜パスを書き換えて使用してください。

**Step2**

``ruby extconf.rb`` を実行してMakefileを生成します。

.. Topic:: ruby extconf.rb
    :class: dos

    | C:> ruby extconf.rb
    | checking for mecab.h... yes
    | creating Makefile


nmakeを実行するために環境をセットアップする
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VisualStudio6のnmakeを実行出来るように、vcvars32.batを実行してからnmakeします。

.. Topic:: ruby extconf.rb
    :class: dos

    | C:> "C:\Program Files\Microsoft Visual Studio\VC98\Bin\VCVARS32.BAT"
    | Setting environment for using Microsoft Visual C++ tools.

nmakeを実行するとビルドに失敗するのでコードを書き換える
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
nmakeを実行してMeCab.soをビルドします。

.. Topic:: ruby extconf.rb
    :class: dos

    | C:> nmake
    | Microsoft (R) Program Maintenance Utility   Version 6.00.8168.0
    | Copyright (C) Microsoft Corp 1988-1998. All rights reserved.
    |
    | ...
    |
    | MeCab_wrap.obj : error LNK2001: 外部シンボル ""__declspec(dllimport) char const * __cdecl MeCab::getTaggerError(void)" (__imp_?getTaggerError@MeCab@@YAPBDXZ)" は未解決です
    | MeCab_wrap.obj : error LNK2001: 外部シンボル ""__declspec(dllimport) class MeCab::Tagger * __cdecl MeCab::createTagger(char const \*)" (__imp_?createTagger@MeCab@@YAPAVTagger@1@PBD@Z)" は未解決です
    | MeCab_wrap.obj : error LNK2001: 外部シンボル ""public: static class MeCab::Tagger \*__cdecl MeCab::Tagger::create(int,char \* \*)" (?create@Tagger@MeCab@@SAPAV12@HPAPAD@Z)" は未解決です
    | MeCab_wrap.obj : error LNK2001: 外部シンボル ""public: static class MeCab::Tagger \*__cdecl MeCab::Tagger::create(char const \*)" (?create@Tagger@MeCab@@SAPAV12@PBD@Z)" は未解決です
    | MeCab_wrap.obj : error LNK2001: 外部シンボル ""public: static char const * __cdecl MeCab::Tagger::version(void)" (?version@Tagger@MeCab@@SAPBDXZ)" は未解決です
    | MeCab.so : fatal error LNK1120: 外部参照 5 が未解決です。
    | NMAKE : fatal error U1077: 'cl' : リターン コード '0x2'
    | Stop.

エラーになりました。上記にあるエラーメッセージでGoogleで検索しても解決策は見つかりませんでした（みんな同じところで引っかかってるというのは見つかりましたが）。そこで、エラーの原因を調べてみたところ、 ``MeCab::Tagger::create`` と ``MeCab::Tagger::version`` という2つのsingletonメソッドが原因っぽいので、ここはスッパリとこの2つのメソッドをあきらめる方向で対策してみます。

`MeCab_wrap.cpp` の以下の2行を削除します(4973行あたり)。singletonの定義部分::

  rb_define_singleton_method(SwigClassTagger.klass, "create", VALUEFUNC(_wrap_Tagger_create), -1);
  rb_define_singleton_method(SwigClassTagger.klass, "version", VALUEFUNC(_wrap_Tagger_version), -1);


これでビルドが通るはず。


改めてnmakeを実行してMeCab.soを作成する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

改めてnmakeを実行してMeCab.soをビルドします。

.. Topic:: ruby extconf.rb
    :class: dos

    | C:> nmake
    | Microsoft (R) Program Maintenance Utility   Version 6.00.8168.0
    | Copyright (C) Microsoft Corp 1988-1998. All rights reserved.
    | 
    |         cl -I. -IC:/ruby-1.8/lib/ruby/1.8/i386-mswin32 -IC:/ruby-1.8/lib/ruby/1.8/i386-mswin32 -I. -MD -Zi  -O2b2xg- -G6 -IC:\Develop\Mecab\sdk -DHAVE_MECAB_H -c -TpMeCab_wrap.cpp
    | Microsoft (R) 32-bit C/C++ Optimizing Compiler Version 12.00.8804 for 80x86
    | Copyright (C) Microsoft Corp 1984-1998. All rights reserved.
    | 
    | MeCab_wrap.cpp
    |         C:\Program Files\Microsoft Visual Studio\VC98\include\xstring(521): クラステンプレートのメンバ関数 'void __thiscall std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >::_Copy(unsigned int)' のコンパイル中
    |         cl -nologo -LD -FeMeCab.so MeCab_wrap.obj msvcrt-ruby18.lib  oldnames.lib user32.lib advapi32.lib shell32.lib ws2_32.lib   -link -incremental:no -debug -opt:ref -opt:icf -dll -libpath:"." -libpath:"C:/ruby-1.8/lib" -libpath:C:\Develop\Mecab\sdk  -implib:MeCab-i386-mswin32.lib -pdb:MeCab-i386-mswin32.pdb -def:MeCab-i386-mswin32.def
    |    ライブラリ MeCab-i386-mswin32.lib とオブジェクト MeCab-i386-mswin32.exp を作成中
    |
    | C:> dir MeCab.so
    | ...
    | 2011/05/04  14:51            57,399 MeCab.so

これでMeCab.soが作成出来ました。

完成物と変更を加えたファイルを公開しておきます。ライセンスなどは元のMeCabのものに従います。

* `mecab-ruby-0.98-win32-binary-20110504.zip`_

.. _`mecab-ruby-0.98-win32-binary-20110504.zip`: stuff/mecab-ruby-0.98-win32-binary-20110504.zip


.. :extend type: text/x-rst
.. :extend:

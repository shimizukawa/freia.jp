:date: 2014-3-21 16:50
:categories: ['Python', 'Sphinx']
:body type: text/x-rst

====================================================================
2014/03/21 Sphinxメンテナ日記: make gettextが超遅い話 (Issue #1426)
====================================================================

*Category: 'Python', 'Sphinx'*

前置き: Sphinxのメンテナになって1年以上たったけど、その間に実装したこととか気づいたこととかもう忘れてきてるので、都度メモしておこうと思い立ちました。ということで、Sphinxメンテナ日記をつけることにしました。前置き終わり。


Sphinxのmake gettextはどうして遅いの？
=========================================

元ネタ: `Issue #1426`_

:ref:`Sphinxのi18n機能 <sphinx:intl>` を使うために、 :command:`make gettext` コマンドでドキュメントからpot/poファイルを作成します。
このとき :command:`make gettext` の実行にかかる時間は、対象のドキュメント1ファイルあたりの大きさの2乗に比例します。
というのが `Issue #1426`_ の話。

:command:`make gettext` で生成されるpotファイルは以下のようになっています。

.. code-block:: po

   # a5600c3d2e3d48fc8c261ea0284db79b
   #: ../../builders.rst:4
   msgid "Available builders"
   msgstr "利用可能なビルダー"

ここについてる `# a5600c3d2e3d48fc8c261ea0284db79b` は、この文字列に対して付けられるUUIDなのですが、
2回目以降の :command:`make gettext` 実行時には前回のキャッシュ(_build/.doctrees)に保存されているrawsource(生文字列)
と、新しくビルドしようとしているドキュメントのrawsourceとを全ノード間でレーベンシュタイン距離を計算して
一致するノードには新しいUUIDを付けないようにしています。

potファイルの用語で言うと、前回のpotファイル内の全てのmsgidと、今回のpotファイルの全てのmsgidの組み合わせについて、
msgidの値の類似度をレーベンシュタイン距離という計算方法を使って誤差率を算出しています。誤差率なので、完全一致したら0%。
あるmsgidの文字列が100文字あって1文字だけ違ったら(typoを直したとか)、誤差率1%という結果になります。
ソースはここ: https://bitbucket.org/birkenfeld/sphinx/src/73418c51/sphinx/versioning.py#cl-102

この結果を使って、新旧msgidの誤差率65%未満のもっとも誤差の低いものを同一とみなし、前回と同じUUIDをmsgidの前の行に付けて
出力しています。誤差が65%以上なら不一致とみなし、新しいUUIDを付けて出力します。

現在の実装で残念なのは以下の点です

* 一度全てのmsgidの組について一致率を計算するので、O(n^2)の実装になっている。
  ある時点のPython公式ドキュメントの一番大きいpotファイルはmsgidを15,000以上持っているので、
  :command:`make gettext` すると225,000,000組以上の誤差計算を実行する。
* この誤差計算をOFFにするオプションが無い
* :command:`make clean` すると「前回の.doctrees」は消え、UUIDは失われ、全msgidについて新しいUUIDが生成されてしまう
* 実際のところ transifex などのサービスを使って翻訳するので誤差とかどうでもいい


ということで改善案を考えてみました。

1. 誤差率を計算しないオプションを追加する
2. 誤差計算する場合、完全一致をPythonの辞書とか使って先に取り除く
3. 誤差計算する場合、かつ.doctreesが無い場合、かつ出力先にpotがある場合、pot内のmsgidと突き合わせる

1をやれば大体の人が嬉しいはず。2をやれば互換性維持しつつ現実的な時間で終わる。3やればちゃんと運用もできるはず。

ということで、気が向いたらやります。


ちなみに
==========

gettextでUUIDを出力するかどうかを指定する `gettext_uuid` オプションが `pull request #217`_ で提案され取り込まれたので、
Sphinx-1.3から提供されます。しかし、これでOffにしても誤差率の計算自体は行うため、速度的なメリットはありません。



参考
=======

* `Issue #1426`_

* @knzm2011 14:57 - 2012年11月11日

    sphinx.versioning の merge_doctrees が遅すぎる！ #sphinxjp 

    -- https://twitter.com/knzm2011/status/267506303881072640

* @knzm2011 15:16 - 2012年11月11日

    調べて分かったこと: builder の versioning_method が 'none' 以外だと versioning 有効。  I18nBuilder の versioning_method は 'text' になっている。(続く) #sphinxjp

    --  https://twitter.com/knzm2011/status/267511221056569344

* @knzm2011 15:18 - 2012年11月11日

    (続き) I18nBuilder の versioning で使われるアルゴリズムは、最悪のケースでノードの全対を比較することになる（段落の数の2乗のオーダー）。 #sphinxjp

    -- https://twitter.com/knzm2011/status/267511674746060802

* @knzm2011 15:24 - 2012年11月11日

    今は versioning は必要ないので、とりあえずこれで https://gist.github.com/4053935  #sphinxjp

    -- https://twitter.com/knzm2011/status/267513170833321984

* @methane 22:06 - 2014年1月14日

    @shimizukawa sphinx の gettext で生成される pot に何かハッシュ値のようなものがついてくるのですが、これって何のためにあるのでしょう？
    https://bitbucket.org/pydocja/cpython-ja/src/34029e38de6fc08c6acc99e75c6c4453ef42fc41/Doc/locale/pot/about.pot?at=3.3#cl-20

    -- https://twitter.com/methane/status/423078545930219520


.. _Issue #1426: https://bitbucket.org/birkenfeld/sphinx/issue/1426/gettext-builder-is-very-slow-during-read
.. _pull request #217: https://bitbucket.org/birkenfeld/sphinx/pull-request/217/add-feature-to-suppress-uuid-location/diff

:date: 2018-02-11 23:00
:tags: Sphinx

===========================================
Sphinx + 翻訳 hack-a-thon 2018.02 #sphinxjp
===========================================

久しぶり？の通常Hack-a-thonイベントに参加してきました。

:イベント: `Sphinx+翻訳 hack-a-thon 2018.02`_
:参加者: @tk0miya, @shimizukawa, @crohaco, nskgch
:会場: タイムインターメディア社（曙橋）

.. _Sphinx+翻訳 hack-a-thon 2018.02: https://sphinxjp.connpass.com/event/77228/


みんながやったこと
=====================

* @tk0miya: 明日の1.7リリースに向けてやっていきました。方針を決めたいチケットについて @shimizukawa と相談しました。

  * `Issue #4583: RFE: Use a changelog tool instead of 'CHANGES' <https://github.com/sphinx-doc/sphinx/issues/4583>`__

  * `Issue #4576: slow running sphinx in large project <https://github.com/sphinx-doc/sphinx/issues/4576>`__

  * `Issue #4575: sphinx-build in parallel with -j N is slow <https://github.com/sphinx-doc/sphinx/issues/4575>`__

  * `Issue #4550: Tables should be centered by default <https://github.com/sphinx-doc/sphinx/issues/4550>`__

  * `Issue #4484: Proposal: Roadmap to Sphinx-2.0 <https://github.com/sphinx-doc/sphinx/issues/4484>`__

  * `Issue #4375: Sphinx not parallel installable for python2 and python3 <https://github.com/sphinx-doc/sphinx/issues/4375>`__

  * `Pull Request #4475: [RFC] Implement delayed resolution in TOC by mwoehlke <https://github.com/sphinx-doc/sphinx/pull/4475>`__

  * `Pull Request #4445: [RFC] Add ability to format :doc: by mwoehlke <https://github.com/sphinx-doc/sphinx/pull/4445>`__

  * `Pull Request #4444: Don't require numfig to use :numref: on sections by mwoehlke <https://github.com/sphinx-doc/sphinx/pull/4444>`__

  * `Pull Request #4392: Builder's interrupt event. Fix #1649 by jbking <https://github.com/sphinx-doc/sphinx/pull/4392>`__

  * `Issue #4520: Subpackage not in toc <https://github.com/sphinx-doc/sphinx/issues/4520>`__

* @shimizukawa: Sphinxのタグとブランチのルールを変えることになったので、 `#4586 <https://github.com/sphinx-doc/sphinx/issues/4586>`__ で実作業を進めました。あと、@tk0miyaリーダーの悩みを聞いてうなずく係をしました。

  * http://www.sphinx-doc.org/ のURL（ドキュメントのバージョン）が、 ``http://www.sphinx-doc.org/en/1.6.5/`` のようにバージョン3桁目まで含んでいたのが、新しいルールになったおかげで ``http://www.sphinx-doc.org/en/1.6/`` で維持されるようになりました。これでリンク切れされなくなる！

* crohaco: #pyhack 雪山合宿で、blogをSphinxにしようというのを始めたので、それを進めました。Sphinxだとblog向け機能がなくて困ってましたが、途中で miyadaiku_ に切り替えてほとんどの課題が解決しました。

  * blogエントリの一覧ページをページングしたい

  * 一覧ページで、各エントリの代表画像を表示したい

* nskgch: Sphinx公式ドキュメントの翻訳を進めました。 `ドメインの説明 <http://www.sphinx-doc.org/ja/master/domains.html>`__ にあるSphinxの歴史を読み解きました。

  * Python言語用として作られたSphinxを他の言語でも使えるようにした?

    * はい。
    * 元々SphinxはPython公式ドキュメントのために作られた
    * Sphinx 1.0でドメインという仕組みを用意して、他の言語でも使えるようにした
    * （SphinxがPython以外で動作するという意味ではない）

  * reSTはSphinxが作った？

    * reSTがあって、それをSphinxが採用して、拡張した


.. _miyadaiku: https://miyadaiku.github.io/ja/index.html


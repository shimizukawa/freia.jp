:date: 2009-10-11 00:04:25
:tags: Zope, python

=======================================================
Zope2 ドキュメントを Sphinx でビルドする手順
=======================================================

先週の日曜日に http://docs.zope.jp/ を公開しましたが、このサイトは http://docs.zope.org/ のソースコードを取得して翻訳したものを Sphinx でビルドして作っています。 Sphinx は reStructuredText で書かれたドキュメントをビルドして html や pdf, chm などを出力する仕組みで、詳しくは渋川さんが翻訳してくれた `Sphinxドキュメントの日本語訳`_ や `渋日記: Pythonって何？という人のためのSphinxチュートリアル`_ を参照してください。

.. _`Sphinxドキュメントの日本語訳`: http://sphinx.shibu.jp/
.. _`渋日記: Pythonって何？という人のためのSphinxチュートリアル`: http://blog.shibu.jp/article/32098239.html


以下、 http://docs.zope.jp/zope2/ を出力するための手順です。

.. topic:: docs.zope.jp ビルド
  :class: dos

  | $ svn co http://svn.freia.jp/open/zope2docs/branches/ja/zope2docs
  | $ cd zope2docs
  | $ python bootstrap.py
  | $ bin/buildout -v
  | $ bin/sphinx-build . html

上記の手順で、既存のPython環境に手を加えずにSphinxのインストールを行い、htmlのビルドが出来ました。出来上がったhtmlファイル群はhtmlというディレクトリ以下に作成されています。上記の例ではWindowsでも動作するように書きましたが、チェックアウトするとMakefileも付いてくるので、 ``make html`` としてもOKです。

また、英語版のビルドを行う場合は、一番最初のチェックアウトするソースコードの場所を http://svn.zope.org/repos/main/zope2docs/trunk/ にすれば良いはずです(2009/10/10時点)。

Sphinxのテンプレートカスタマイズ
--------------------------------

docs.zope.jp では、ちょっとだけテンプレートをカスタマイズしていて、本家と違うところがあります。ファイル的には `layout.html`_ を追加していて、Sphinxで生成したhtmlファイルにGoogleAnalyticsのトラッカーを埋め込んだり、問い合わせ先についてのリンクを設置したりしています。こんな感じです::

    {% extends "!layout.html" %}

    {%- block rootrellink %}
    <li><a target="_blank" href="http://docs.zope.org/zope2/" title="English(Original)">English(Original)</a></li>
    {{ reldelim2 }}
    <li><a target="_blank" href="http://zope.jp/" title="日本Zopeユーザー会 - JZUG">JZUG</a></li>
    {{ reldelim2 }}
    {{ super() }}
    {%- endblock %}


    {%- block sidebarsearch %}
    {{ super() }}
    <h3>お問い合わせ</h3>
    <div>
      <p>
        日本語訳についてのご意見などは
        <a target="_blank" href="http://zope.jp/contact-info">zope.jp の連絡フォーム</a>
        からお願いします。
      </p>
    </div>
    {%- endblock %}

    {% block footer %}
    {{ super() }}
    <script type="text/javascript">
    var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
    document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
    </script>
    <script type="text/javascript">
    try {
    var pageTracker = _gat._getTracker("UA-xxxxxxx-1");
    pageTracker._trackPageview();
    } catch(err) {}</script>
    {% endblock %}



GoogleAnalyticsの埋め込み部分については `Adding Google Analytics to Sphinx Docs | Surfing in Kansas`_ を参考にし、その他のカスタマイズについては `テンプレート - Sphinx v1.0 (hg) documentation`_ を読みながら作成しています。

.. _`Adding Google Analytics to Sphinx Docs | Surfing in Kansas`: http://ericholscher.com/blog/2009/apr/5/adding-google-analytics-sphinx-docs/

.. _`テンプレート - Sphinx v1.0 (hg) documentation`: http://sphinx.shibu.jp/templating.html

.. _`layout.html`: http://svn.freia.jp/open/zope2docs/branches/ja/zope2docs/.templates/layout.html 



.. :extend type: text/html
.. :extend:



.. :comments:
.. :comment id: 2010-09-03.0657923134
.. :title: Re:Zope2 ドキュメントを Sphinx でビルドする手順
.. :author: xiangxiang
.. :date: 2010-09-03 17:04:26
.. :email: xiangxiangputou@sina.com
.. :url: http://www.oxpdf.jp/ 
.. :body:
.. OX CHM PDF変換は仮プリンタを利用してCHMをPDFファイルに変換するソフトです。作成したPDFファイルはPDF1.2、PDF1.3やPDF1.4をサ ポートしCHMをPDFファイルに変換できて、任意な印刷できるファイルも変換できます。具体的に言えば、Txt、Word、Excel、 Powerpointや画像形式などです。そしてPDFファイルに作成するほかに、「Option]において画像形式（例えばPNG、JPEG、BMP、 PCX、TIFF)や言語編集形式（PS、EPS)などとしても保存できます。
.. 安全なシステムとしてOX CHM PDF変換 フリーはパスウードをつけることができます。またフリーダウンロードをサポートします。
.. http://www.oxpdf.jp/chm-to-pdf-converter.html

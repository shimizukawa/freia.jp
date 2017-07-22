:date: 2010-10-17 19:39:30
:categories: ['python']
:body type: text/x-rst

======================================================
2010/10/17 別解: lxmlを使ってXMLの要素をソートして返す
======================================================

はじめに
---------

こんにちは、NERDです。先日、 `lxmlを使ってXMLの要素をソートして返す - YAMAGUCHI::weblog`_ というエントリが上がっていたので、XMLの変換と言えばxsltでしょう！とか思ったので実際にやってみました。xsltの適用は元記事の方でも使っているlxmlで簡単にできるのが良いですね。

.. _`lxmlを使ってXMLの要素をソートして返す - YAMAGUCHI::weblog`: http://d.hatena.ne.jp/ymotongpoo/20101008/1286499332

参考
-----
* `lxml.etree._Element`_
* `たのしいXML: XSLT基礎編: xsl:sort`_

.. _`lxml.etree._Element`: http://codespeak.net/lxml/api/lxml.etree._Element-class.html
.. _`たのしいXML: XSLT基礎編: xsl:sort`: http://www6.airnet.ne.jp/manyo/xml/


サンプルコード
---------------

.. code-block:: python

    # -*- coding: utf-8 -*-
    from lxml import etree
    
    xml = """
    <statuses>
      <status>
        <id>5</id>
        <text>spam</text>
      </status>
      <status>
        <id>1</id>
        <text>egg</text>
      </status>
      <status>
        <id>100</id>
        <text>ham</text>
      </status>
      <status>
        <id>2</id>
        <text>bacon</text>
      </status>
    </statuses>
    """
    
    xslt = """
    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
      <xsl:template match="/statuses">
        <xsl:copy>
          <xsl:for-each select="status">
            <xsl:sort select="id" data-type="number" />
            <xsl:copy-of select="." />
          </xsl:for-each>
        </xsl:copy>
      </xsl:template>
    </xsl:stylesheet>
    """
    
    def sort_by_id(xml):
        try:
            tree = etree.fromstring(xml)
            transform = etree.XSLT(etree.fromstring(xslt))
            transformed = transform(tree)
            return etree.tostring(transformed, pretty_print=True)
    
        except Exception, e:
            """
            rescure here.
            """
            raise e
    
    
    if __name__ == '__main__':
        print xml
        print '--------------------'
        print sort_by_id(xml)


xsltの記述、けっこう長くなってしまってますね。もうちょっと短く書ける気がするんですが…。あと出来るだけタグ名に依存しないように書ければいいなあ。

実行結果
---------

.. code-block:: xml

    <statuses>
      <status>
        <id>5</id>
        <text>spam</text>
      </status>
      <status>
        <id>1</id>
        <text>egg</text>
      </status>
      <status>
        <id>100</id>
        <text>ham</text>
      </status>
      <status>
        <id>2</id>
        <text>bacon</text>
      </status>
    </statuses>
    
    --------------------
    <statuses>
      <status>
        <id>1</id>
        <text>egg</text>
      </status>
      <status>
        <id>2</id>
        <text>bacon</text>
      </status>
      <status>
        <id>5</id>
        <text>spam</text>
      </status>
      <status>
        <id>100</id>
        <text>ham</text>
      </status>
    </statuses>


.. :extend type: text/x-rst
.. :extend:



.. :comments:
.. :comment id: 2010-10-21.4151359945
.. :title: Re:別解: lxmlを使ってXMLの要素をソートして返す
.. :author: ymotongpoo
.. :date: 2010-10-21 18:13:36
.. :email: 
.. :url: http://d.hatena.ne.jp/ymotongpoo/20101008/1286499332
.. :body:
.. XSLTを使うのは逆に僕がやりたかったことなのでとても助かります！！ありがとうございます！！
.. 
.. :comments:
.. :comment id: 2010-10-21.0959510319
.. :title: Re:別解: lxmlを使ってXMLの要素をソートして返す
.. :author: しみずかわ
.. :date: 2010-10-21 21:31:08
.. :email: 
.. :url: 
.. :body:
.. statusesに属性が付いていてそれを維持する場合は、以下の記述が必要。 <xsl:copy> 直後に。
.. 
.. ::
.. 
..   <xsl:for-each select="@*">
..     <xsl:copy />
..   </xsl:for-each>
.. 

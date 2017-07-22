:date: 2007-07-20 03:13:05
:tags: python, turbogears

=============================================================
2007/07/20 TurboGearsとCherryPyのリダイレクトについてもう少し
=============================================================

いっこ前のエントリで謎な設定をしたらうまく動くようになった理由。

- CherryPy はコントローラオブジェクトへの末尾"/"無しアクセスは"/"ありにリダイレクトする

  - CherryPy-2.2.1-py2.4.egg/cherrypy/_cphttptools.py (297)

  .. code-block:: python

                    # We found the extra ".index". Check if the original path
                    # had a trailing slash (otherwise, do a redirect).
                    if not objectpath.endswith('/'):
                        atoms = self.browser_url.split("?", 1)
                        newUrl = atoms.pop(0) + '/'
                        if atoms:
                            newUrl += "?" + atoms[0]
                        raise cherrypy.HTTPRedirect(newUrl)

末尾に"/"が無い場合に、self.browser_urlなるものを使ってリダイレクト先URLを構成している。このbrowser_urlは以下のように作成されている。

- CherryPy-2.2.1-py2.4.egg/cherrypy/_cphttptools.py (208)

.. code-block:: python

    def _get_browser_url(self):
        url = self.base + self.path
        if self.query_string:
            url += '?' + self.query_string
        return url

で、self.base はmyappを含まない。self.pathも含んでいない。self.baseの生成は以下で行われている。

- CherryPy-2.2.1-py2.4.egg/cherrypy/filters/baseurlfilter.py

これは30行ほどの短いファイルなのですぐ読める。ここでbaseをhost名から生成しようとするので、cfgで自動生成をOffにして明示的に与えてやる。これで一応解決する。が、あくまでホスト名を生成するためのbase_url_filterを変な使い方して回避するのは腑に落ちない。

ここでvirtual_hostフィルターとかありそうだよなーと思ってcherrypy/filtersフォルダを眺めてみたらvirtualhostfilter.pyを発見。‥‥あれ？これでいけるんじゃないかな？


.. :extend type: text/html
.. :extend:


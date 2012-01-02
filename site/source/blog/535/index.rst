:date: 2008-02-04 13:36:29
:categories: ['python', 'Plone']
:body type: text/x-rst

==================================================
2008/02/04 easy_installでPILをインストールするhack
==================================================

*Category: 'python', 'Plone'*

- `setuptoolsでPILをインストール - 三次元日誌`_
- `Problems Installing (Easy_Install) Pil – martin-geber.com`_


上記２サイトで書かれている方法だと、 import PIL; できなくなってしまう。
この問題に直面しているのがPloneで、以下のような議論も発生している。

`#5883 (PIL not found by plone when installed as an egg) - Plone - Trac`_

"I agree with Martin that this is a bug in the PIL egg and not in Plone."

PILの問題であって、Ploneの問題ではないというMartinの主張に同意する。 というコメントともにチケットのステータスは **closed defect: wontfix** に変更されている。

Image-SIG MLでの反応。

`Re: [Image-SIG] cannot import from PIL when easy_installed`_

ということで、何とかならないかいじってみた。

.. _`setuptoolsでPILをインストール - 三次元日誌`: http://d.hatena.ne.jp/ousttrue/20071117/1195253720
.. _`Problems Installing (Easy_Install) Pil – martin-geber.com`: http://www.martin-geber.com/weblog/2007/08/22/problems-installing-easy_install-pil/
.. _`#5883 (PIL not found by plone when installed as an egg) - Plone - Trac`: http://dev.plone.org/plone/ticket/5883
.. _`Re: [Image-SIG] cannot import from PIL when easy_installed`: http://www.mail-archive.com/image-sig@python.org/msg01373.html


.. :extend type: text/html
.. :extend:


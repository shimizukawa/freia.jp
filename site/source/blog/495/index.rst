:date: 2007-12-01 22:37:00
:categories: ['javascript']
:body type: text/x-rst

===========================================
2007/12/01 AmazonのURLコピーするbookmarklet
===========================================

最近のAmazonはURLに日本語が含まれていて、IMで渡しにくいので、短いURLに変換するブックマークレットを作ってみた。

promptをpopupする版(URLのみ)::

  javascript:var%20p=prompt('URL%20is...',location.href.replace(/.*\/([A-Z\d]{10})\/.*/,'http://www.amazon.co.jp/dp/$1'))

promptをpopupする版(タイトルとURL)::

  javascript:var%20p=prompt('URL%20is...',document.title.replace(/^\s+(.*)\s+$/,'$1')+"  "+location.href.replace(/.*\/([A-Z\d]{10})\/.*/,'http://www.amazon.co.jp/dp/$1'))


Windowsのクリップボードに渡す版(URLのみ)::

  javascript:(function(text){var swf_data = "http://www.freia.jp/taka/setClipboard.swf";var tmp = document.createElement("div");tmp.innerHTML = '<embed src="'+swf_data+'" FlashVars="code='+encodeURI(text)+'" width="0" height="0"></embed>';with(tmp.style){position ="absolute";left = "-10px";top  = "-10px";visibility = "hidden";};document.body.appendChild(tmp);setTimeout(function(){document.body.removeChild(tmp)},1000);})(location.href.replace(/.*\/([A-Z\d]{10})\/.*/,'http://www.amazon.co.jp/dp/$1'))

Windowsのクリップボードに渡す版(タイトルとURL)::

  javascript:(function(text){var swf_data = "http://www.freia.jp/taka/setClipboard.swf";var tmp = document.createElement("div");tmp.innerHTML = '<embed src="'+swf_data+'" FlashVars="code='+encodeURI(text)+'" width="0" height="0"></embed>';with(tmp.style){position ="absolute";left = "-10px";top  = "-10px";visibility = "hidden";};document.body.appendChild(tmp);setTimeout(function(){document.body.removeChild(tmp)},1000);})(document.title.replace(/^\s+(.*)\s+$/,'$1')+"\n"+location.href.replace(/.*\/([A-Z\d]{10})\/.*/,'http://www.amazon.co.jp/dp/$1'))


参考にしたサイト:

- `AmazonのURL - Vox`_

.. _`AmazonのURL - Vox`: http://takeshi.vox.com/library/post/amazon%E3%81%AEurl.html


.. :extend type: text/html
.. :extend:



.. :comments:
.. :comment id: 2008-12-17.3934052472
.. :title: Re:AmazonのURLコピーするbookmarklet
.. :author: big fat gay
.. :date: 2008-12-17 08:49:54
.. :email: gay@iggy-pop-gay.com
.. :url: http://iggy-pop-gay.com/map-of-gay-world/
.. :body:
.. Gay line dancing
.. <url>http://iggy-pop-gay.com/map-of-gay-world/|Map of gay world</url>
.. 

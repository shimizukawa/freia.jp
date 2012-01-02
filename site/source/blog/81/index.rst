:date: 2004-11-20 16:26:35
:categories: ['Zope', 'python']
:body type: text/x-rst

====================
Zopeでナビゲーション
====================

#ですます調に疲れたので、だである調に変更しますです（笑

最近はナビゲーションに対応したブラウザも増えてきたので、自サイトもナビゲーション用のタグを導入してみようと思う。ナビゲーションタグは *<head></head>* 内に::

  <head>
    <link rel="home" href="...." /> 
    <link rel="up" href="...." /> 
    <link rel="index" href="...." /> 
  </head>

と言う感じに記述するらしい。

せっかくZopeを使っているので、各ページに埋め込まずにこれを実現する方法を考えてみた。今回思いついたのは、standard_html_headerの中からpythonスクリプトを呼び出して、 **獲得** を使って必要なナビゲーション(例えばup)を探し、見つかったらそれのURLを *<link rel...>* で埋め込む方法だ。

まずstandard_html_headerに以下の文を埋め込んでおく::

  <dtml-var "navigation('index')">
  <dtml-var "navigation('author')">
  <dtml-var "navigation('home')">
  <dtml-var "navigation('contents')">
  <dtml-var "navigation('search')">
  <dtml-var "navigation('help')">
  <dtml-var "navigation('copyright')">
  <dtml-var "navigation('alternate')">
  <dtml-var "navigation('parent')"><!--same as up-->
  <dtml-var "navigation('up')">
  <dtml-var "navigation('first')"><!--same as begin-->
  <dtml-var "navigation('begin')">
  <dtml-var "navigation('prev')">
  <dtml-var "navigation('next')">
  <dtml-var "navigation('last')"><!--same as end-->
  <dtml-var "navigation('end')">

次に、ここで呼び出されるnavigationというオブジェクトをPythonScriptでルートフォルダに用意。中身はこんな感じ::

  try:
    # targetはscriptの引数。"home"とか"up"とかが入ってくる
    # 今見ているページからtargetの獲得に挑戦。失敗するとexceptへ。
    attr = getattr(context,target)

    # targetと同じ名前のプロパティーとかを捕まえた場合、とりあえず失敗。
    if not hasattr(attr,"meta_type"):
      return '<!--find same name as %s-->' % target

    # みつけたtargetがscriptの場合は値をもらってそのまま返す
    if attr.meta_type == "Script (Python)":
      return attr()

    # script以外が見つかったら、見つけたtargetのurlを返す
    return '<link rel="%s" href="%s" />' % (target,attr.absolute_url())

  except:
    pass

  # 失敗したら一応コメントアウトした文字列だけ返す
  return '<!--link rel="%s"-->' % target

あとは獲得可能な場所に index とか copyright とかの名前でDTML Documentなどを置いておけば、ナビゲーションバーで対象ドキュメントに飛ぶことが出来るようになる、という寸法。ただ、特定のドキュメントを表示したくない場合、たとえば up(親階層) などの場合はDTML Documentでは面倒なので、Python Scriptを up という名前で置いておいて、スクリプトで親階層のURLを含む <link rel...> 文字列を返すように作ればいいようにしてある。

up のPython Scriptの中身は以下のような感じ::

  request = container.REQUEST

  url = request.URL1

  # 今のページが最上位であればコメント文字列を返して終了
  if url == request.BASE0:
    return '<!--link rel="up" href="/"-->'

  # 一つ親の区切りを探す
  col = url.rfind("/")

  # サーバー名まで浸食されたら失敗
  if col < url.find("//")+1:
    return '<!--link rel="up" href="/"-->'

  # 階層一つ分削って link タグを返す
  return '<link rel="up" href="%s">' % url[:col]

findしないでsplit("/")とjoinで構築しようと思ったのだが、なぜかjoin( s, "/")で失敗してしまうため、断念。pythonのヘルプ等には *第二引数で連結部分に入れる文字を指定* と書いてあるのに、なぜか::

  join() takes exactly one argument (2 given)

といって怒られる始末。不思議だ。

今回の方式のウリは、獲得を使っているので必要なところでオーバーライドすることが出来ること。というかこれが出来ないとWebサーバーという性質上話にならない。nextやprevのリンク先がWebサーバー上の前ページで固定でも誰も嬉しくない。

あとの問題は、今回の方式でナビゲーションのリンク先を用意すると、ルートフォルダ等にナビ用のオブジェクトが散乱すること。いちおう手元のはサブフォルダを指定できるようにしてみたけど、あんまり美しくない‥‥。この後の課題ということにしておこう。




.. :extend type: text/plain
.. :extend:

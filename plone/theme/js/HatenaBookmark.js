/*
 * <script type="text/javascript" src="js/HatenaBookmark.js"></script>
 * FIXME: parmanent_url is wrong (location.href include query, subpath, ..etc).
 */
$(function(){
	var parmanent_url = location.href;
	var hatena_url = 'http://b.hatena.ne.jp/entry/' + parmanent_url;
	var hatena_image_url = 'http://b.hatena.ne.jp/entry/image/' + parmanent_url;
	var page_title = $('head title')[0].text;
	var elem1 = '<a href="http://b.hatena.ne.jp/entry/add/' + parmanent_url + '"> <img src="/taka/theme/img/append.gif" width="16" height="12" style="border: none;" alt="このエントリーをはてなブックマークに追加" title="このエントリーをはてなブックマークに追加" /> </a> <a href="http://b.hatena.ne.jp/entry/' + parmanent_url + '"> <img src="/taka/theme/img/entry.gif" width="16" height="12" style="border: none;" alt="このエントリーを含むはてなブックマーク" title="このエントリーを含むはてなブックマーク" /> </a>'
	var elem2 = '<a href="' + hatena_url + '"><img src="' + hatena_image_url + '" alt="はてなブックマーク - ' + page_title + '" title="はてなブックマーク - ' + page_title + '"></a>';

	$('h1').append(elem1 + elem2);
});


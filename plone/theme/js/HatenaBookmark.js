/*
 * Hatena Bookmark count annotation
 *
 * <script type="text/javascript" src="js/HatenaBookmark.js"></script>
 * <script type="text/javascript">
 * Hatena.Bookmark.SiteConfig = {
 *   'div.documentbody h1 a.headerlink': {},
 *   'div.documentbody .toctree-wrapper a': {}
 * };
 * </script>
 *
 * url as:
 * - link to: http://b.hatena.ne.jp/entry/[target-url]
 * - add for: http://b.hatena.ne.jp/entry/add/[target-url]
 * - counts :http://b.hatena.ne.jp/entry/image/[target-url]
 */

if (typeof(Hatena) == 'undefined') {
	Hatena = {};
}
if (typeof(Hatena.Bookmark) == 'undefined') {
    Hatena.Bookmark = {};
}
if (typeof(Hatena.Bookmark.SiteConfig) == 'undefined') {
    Hatena.Bookmark.SiteConfig = {};
}

$(function(){
	var hatena_base_url = 'http://b.hatena.ne.jp/entry/';
	var hatena_bookmark_count_class = 'hatena-bookmark-count';
	var elements = Hatena.Bookmark.SiteConfig;

	for(area in elements) {
		var e = elements[area];
		$(area).after(function(){
			var permanent_url = this.href.match(/^[^#\?]*/);
			if(permanent_url) {
				permanent_url = permanent_url[0];
				var link_elem = document.createElement('a');
				var img_elem = document.createElement('img');
				link_elem.href = hatena_base_url + permanent_url;
				link_elem.class = hatena_bookmark_count_class;
				img_elem.src = hatena_base_url + 'image/' + permanent_url;
				return $(link_elem).append(img_elem);
			} else {
				return null;
			}
		});
	};
});


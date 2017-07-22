:date: 2007-10-01 00:09:56
:tags: Programming, Windows
:body type: text/x-rst

====================================================
2007/10/01 Puttyごった煮版のpfwdを改造して自動再接続
====================================================

「pfwd.exeを改造してダイアログ出さずにリトライする」ように改造してみた。

1. Putty-0.58 ごった煮版を取得
2. ごった煮版のマニュアルに従って本家の0.58のソースを取得
3. ごった煮版同梱のpatchを本家0.58に適用
4. とりあえずbuildしてみる。

とりあえずここまでは成功。patch適用はFreeBSD上でやった。buildは `WindowsでFreeなCモジュールビルド環境`_ という環境。Python関係なくWindowsアプリのビルドが出来ますよ。

最後に以下の修正を行ってビルド。

.. code-block:: cpp

	--- putty58/windows/pfwd.c.orig	Sun Sep 30 23:50:28 2007
	+++ putty58/windows/pfwd.c	Sun Sep 30 23:46:45 2007
	@@ -762,11 +761,9 @@
	 	break;
	     case WM_DISCONNECTED:
	 	ChangeTrayIcon(hwnd, IDI_ICOND);
	-	if (DialogBox(m_hInst, MAKEINTRESOURCE(IDD_DISCONNECT), hwnd, DisconnectedProc) == IDOK) {
	-	    PostMessage(hwnd, WM_CONNECTING, 0, 0);
	-	}else{
	-	    SendMessage(hwnd, WM_CLOSE, 0, 0);
	-	}
	+	auto_connect_count++;
	+	Sleep(1000);
	+	PostMessage(hwnd, WM_CONNECTING, 0, 0);
	 	break;
	     case WM_CONNECTING:
	 	if (m_hThread == NULL) {

WindowMessage処理の中でSleepして大丈夫だったっけ...？ま、いっか。

これでネットワーク切断後も1秒間隔で延々と黙々と接続チャレンジするように
なった。

ついでに、切断時と接続時にバルーン表示するようにしてみたところ、激しく目障りだったのでバルーンは使わないようにしよう...。

.. code-block:: cpp

	--- putty58/windows/pfwd.c.orig	Sun Sep 30 23:50:28 2007
	+++ putty58/windows/pfwd.c	Sun Sep 30 23:56:39 2007
	@@ -1,6 +1,7 @@
	 /*
	  * PLink - a command-line (stdin/stdout) variant of PuTTY.
	  */
	+#define _WIN32_IE 0x0500
	 
	 #include <stdio.h>
	 #include <stdlib.h>
	@@ -644,6 +645,26 @@
	 	Shell_NotifyIcon(NIM_ADD, &nid);
	 }
	 
	+
	+static void UpdateBalloon( HWND hwnd, const char* pszTitle, const char *pszText, DWORD dwFlag, unsigned int uTimeout )
	+{
	+	static NOTIFYICONDATA nid = {
	+		sizeof nid,
	+		NULL,
	+		IDI_ICON,
	+	};
	+	return;
	+	nid.hWnd = hwnd;
	+
	+	nid.uFlags |= NIF_INFO;
	+	strncpy( nid.szInfo, pszText, 255 ); // 255 is specify by MSDN document.
	+	nid.uTimeout = uTimeout;
	+	strcpy( nid.szInfoTitle, pszTitle );
	+	nid.dwInfoFlags = dwFlag;
	+
	+	Shell_NotifyIcon( NIM_MODIFY, &nid );
	+}
	+
	 static void DelTrayIcon(HWND hwnd)
	 {
	     NOTIFYICONDATA nid = {
	@@ -758,15 +779,17 @@
	 	break;
	     case WM_CONNECTED:
	 	ChangeTrayIcon(hwnd, IDI_ICON);
	+	UpdateBalloon(hwnd, "pfwd", "Connected", NIIF_INFO, 1 );
	 	auto_connect_count = 0;
	 	break;
	     case WM_DISCONNECTED:
	 	ChangeTrayIcon(hwnd, IDI_ICOND);
	-	if (DialogBox(m_hInst, MAKEINTRESOURCE(IDD_DISCONNECT), hwnd, DisconnectedProc) == IDOK) {
	-	    PostMessage(hwnd, WM_CONNECTING, 0, 0);
	-	}else{
	-	    SendMessage(hwnd, WM_CLOSE, 0, 0);
	+	if (auto_connect_count == 0) {
	+	    UpdateBalloon(hwnd, "pfwd", "Disconnected", NIIF_WARNING, 1 );
	 	}
	+	auto_connect_count++;
	+	Sleep(1000);
	+	PostMessage(hwnd, WM_CONNECTING, 0, 0);
	 	break;
	     case WM_CONNECTING:
	 	if (m_hThread == NULL) {



.. _`WindowsでFreeなCモジュールビルド環境`: http://www.freia.jp/taka/memo/freevcbuild/


.. :extend type: text/html
.. :extend:



.. :comments:
.. :comment id: 2007-10-11.2421208264
.. :title: Re:Puttyごった煮版のpfwdを改造して自動再接続
.. :author: しみずかわ
.. :date: 2007-10-11 02:10:42
.. :email: 
.. :url: 
.. :body:
.. 再接続を一定回数以上繰り返すとpfwdが落ちます。やっぱり手抜きは良くない。
.. 
.. :trackbacks:
.. :trackback id: 2007-10-01.9813608809
.. :title: [Django][Python][jQuery][CSS][その他]巡回
.. :blog name: 常山日記
.. :url: http://d.hatena.ne.jp/johzan/20071001/1191208935
.. :date: 2007-10-01 12:23:02
.. :body:
..  Google Code: New: idjango これからに期待! :) videosoft Update: django-pantheon django-evolution deseb django-cms komercha clapton djangobrasil spini-portal django-generics Blog: [Django][django-registration] ユーザー認証をやってみる さくらインターネット
.. 

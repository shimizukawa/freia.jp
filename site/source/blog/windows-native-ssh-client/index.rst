:date: 2018-03-28 15:00
:tags: Windows, ssh

===============================================================
PuTTYを卒業してWindows 10標準のssh client（ベータ）に切り替えた
===============================================================

Windows 10 Fall Creator Update から、WindowsにはOpenSSHのクライアントとサーバーが同梱されています。2018年3月頭にGitHubへのssh経由の接続がPyCharm（2017.3.3）PuTTY（0.67）でできなくなった(`Weak cryptographic standards removal notice | GitHub Engineering`_)のをきっかけに、乗り換えてみました。

.. figure:: git-pull-with-windows-ssh-client.*
   :width: 80%

   Windows標準のsshを使ってgit pullしたところ

.. _Weak cryptographic standards removal notice | GitHub Engineering: https://githubengineering.com/crypto-removal-notice/

モチベーション
==============

* PuTTY（0.68）以降（現在は0.70推奨）であれば繋がるけど、Windowsのsshクライアントを試してみたかった

* PuTTYだと、OpenSSHと鍵の形式が違うので公開鍵の管理が面倒だった

* PuTTYの設定とOpenSSHの設定を両方覚えるのに疲れた

* pagent.exe をタスクトレイに常駐させるのに飽きてきた

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">PyCharmの内蔵sshクライアントが更新されてGitHubと正常に通信できるようになったっぽい（自分はこの機会にputty(plink)もやめてWindowsネイティブのsshに切り替えてしまった）: &quot;PyCharm 2016.3 and later updated for GitHub compatibility&quot; <a href="https://t.co/jKH5cSzlFy">https://t.co/jKH5cSzlFy</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/971547007100731393?ref_src=twsrc%5Etfw">2018年3月8日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Windows標準のOpenSSHクライアント
================================

Windows 10 Fall Cretor Update (2017/秋）から同梱されているOpenSSHのWindows向けバイナリで、まだベータ版だそうです。
詳細は以下のblogに書かれています。

* `Using the OpenSSH Beta in Windows 10 Fall Creators Update and Windows Server 1709 | PowerShell Team Blog`_

自分が行った手順を抜粋します。

とりあえず SSH Clientをインストール。Winキーを押して「スタート」メニューを開いたら "オプション機能の管理" と入力して開く。そして "機能の追加" で "OpenSSH クライアント" をインストール。

.. figure:: win10-install-option-feature.*
   :width: 80%

   "OpenSSH クライアント" をインストール

``C:\Windows\System32\OpenSSH\`` 以下に ``ssh.exe`` などがインストールされる。

.. code-block:: ps1con
   :caption: インストールされるsshコマンド

   [taka] > dir C:\Windows\System32\OpenSSH\


       ディレクトリ: C:\Windows\System32\OpenSSH


   Mode                LastWriteTime         Length Name
   ----                -------------         ------ ----
   -a----       2018/03/12      1:15         343552 scp.exe
   -a----       2018/03/25      1:05         355840 sftp-server.exe
   -a----       2018/03/12      1:15         408064 sftp.exe
   -a----       2018/03/12      1:15         531968 ssh-add.exe
   -a----       2018/03/12      1:15         495616 ssh-agent.exe
   -a----       2018/03/12      1:15         657920 ssh-keygen.exe
   -a----       2018/03/12      1:15         594944 ssh-keyscan.exe
   -a----       2018/03/25      1:05         154624 ssh-shellhost.exe
   -a----       2018/03/12      1:15         894464 ssh.exe
   -a----       2018/03/25      1:05         970752 sshd.exe
   -a----       2018/03/25      1:05           2143 sshd_config_default

   [taka] > ssh.exe -V
   OpenSSH_for_Windows_7.6p1, LibreSSL 2.6.4

次に、ssh-agentサービスを自動起動させます。Unix/Linux系OSのssh-agentと違って、ssh-agentプロセスをシェル上で起動して環境変数を設定して・・という操作は不要です（サービスだと分からずにちょっとハマりました）。あとでここに鍵を登録します。

.. figure:: win10-ssh-agent-service.*
   :width: 80%

   ss-agent サービスを自動起動


ホームディレクトリ以下に ``.ssh`` ディレクトリを作って(``C:\Users\<username>\.ssh``)、 ``config`` ファイルと鍵を置きます。鍵は ``ssh-keygen.exe`` で作れます。自分は、PuTTYの鍵からOpenSSH形式に変換したものを置きました。

.. code-block:: ps1con
   :caption: .ssh ディレクトリにconfigと鍵を置く

   [.ssh] > dir


       ディレクトリ: C:\Users\taka\.ssh


   Mode                LastWriteTime         Length Name
   ----                -------------         ------ ----
   -a----       2018/02/26      9:05            180 config
   -a----       2018/02/26     13:47           3311 id_rsa
   -a----       2018/02/26     17:54            750 id_rsa.pub

``.ssh/config`` にはOpenSSHの設定を書いておけます。

.. code-block:: none
   :caption: .ssh/config

   TCPKeepAlive yes

   Host gateway
       HostName gateway.example.com
       User shimizukawa
       IdentityFile C:\Users\taka\.ssh\id_rsa
       DynamicForward localhost:1080

そして、普段使う秘密鍵をssh-agentに登録しておきます。

.. code-block:: ps1con
   :caption: .ssh ディレクトリにconfigと鍵を置く

   [.ssh] > ssh-add id_rsa
   Enter passphrase for id_rsa:
   Identity added: id_rsa (id_rsa)
   [.ssh] > ssh-add -l
   4096 SHA256:RTUy9YdxQzN7NwuSMa9DMepVko5sRUXPHGXlHlZHv4c id_rsa (RSA)

パスフレーズを入力して鍵登録が完了すると、上記のように登録済み鍵一覧が確認できます。これ以降、ssh-agentサービスが起動していれば、OSを再起動してもパスフレーズの入力は必要ありません。

なお、登録した鍵の削除は ``ssh-ad -d <filename>`` らしいけど、 ``No such file or directory`` と言われてうまくいかないので、 ``ssh-add -D`` で全削除している。


.. _Using the OpenSSH Beta in Windows 10 Fall Creators Update and Windows Server 1709 | PowerShell Team Blog: https://blogs.msdn.microsoft.com/powershell/2017/12/15/using-the-openssh-beta-in-windows-10-fall-creators-update-and-windows-server-1709/

GitHubとの接続に使う
====================

以前は ``GIT_SSH=plink.exe`` と指定して、pagentを常駐して鍵の解決などをやっていました。これをOpenSSHに切り替えます。

まず、sshコマンドでGitHubへの接続が可能か確認します。
GitHubに登録してある公開鍵に対応する秘密鍵が ``ssh-add`` してあれば繋がるはず。

.. code-block:: ps1con
   :caption: GitHub ssh 接続確認

   [taka] > ssh git@github.com
   PTY allocation request failed on channel 0
   Hi shimizukawa! You've successfully authenticated, but GitHub does not provide shell access.
   Connection to github.com closed.

はい。

gitコマンドからこのsshを使うように、 ``GIT_SSH`` 環境変数に明示的に設定しておきます。

.. figure:: git-ssh.*
   :width: 80%

   GIT_SSH C:\Windows\System32\OpenSSH\ssh.exe

これで、 ``git clone ssh://github.com/...`` のような操作が実行できました。


WSL (Windows Servie for Linux)からの利用
=========================================

WSLのUbuntuにもsshはインストールされていますが、せっかくWindows上でssh-agentサービスが動作しているので別途鍵を管理するのは避けたい感じです。そこで、 ``ssh`` ではなく ``ssh.exe`` を実行することで、Windows側のsshを使ってみます。

.. code-block:: bash
   :caption: wsl ubuntu

   [taka ~]$ which ssh
   /usr/bin/ssh
   [taka ~]$ which ssh.exe
   /mnt/c/Windows/System32/OpenSSH/ssh.exe

ssh.exeでGitHubに接続すると、以下のような警告メッセージが表示されます。

.. code-block:: bash
   :caption: wsl ssh.exe

   [taka ~]$ ssh.exe git@github.com
   Pseudo-terminal will not be allocated because stdin is not a terminal.

stdinを仮想ターミナルに割り当てられない、というメッセージが。
この問題があるために、WSL環境では ``GIT_SSH=ssh.exe`` では通信がうまくいきませんでした。 ``GIT_SSH=ssh`` ならUbuntuのsshが使われるので、鍵の設定をWSL専用に用意すればちゃんとGitHubと通信できました。

どうにか動作させられないかと、 "wsl ssh.exe" あたりのキーワードで検索したところ、以下のIssueが見つかりました。

* `Using ssh.exe from WSL does not work properly · Issue #990 · PowerShell/Win32-OpenSSH`_
* `TTY issue when running Win32 process from WSL · Issue #2406 · Microsoft/WSL`_

このあたりが解決すれば、WSLからssh.exeを使えるようになりそうです。

残念ながら、しばらく直らなそうなので、WSLのUbuntuにも鍵を置いて運用するしかないかな。

.. _Using ssh.exe from WSL does not work properly · Issue #990 · PowerShell/Win32-OpenSSH: https://github.com/PowerShell/Win32-OpenSSH/issues/990
.. _TTY issue when running Win32 process from WSL · Issue #2406 · Microsoft/WSL: https://github.com/Microsoft/WSL/issues/2406


よくなったこと、わるくなったこと
================================

* PowerShell等のWindowsのコマンドラインからsshできるようになった
* OpenSSHの ``.ssh/config`` で設定書けるようになった
* pagent.exe をタスクトレイに常駐させなくてよくなった
* 秘密鍵のパスフレーズを入力しなくてよくなった（良いのか？まあいいか）
* 多段SSH Proxyするのが超楽になった（PuTTYの設定が難しい）
* PuTTYの豊富すぎる設定からの卒業
* ssh通信ログを保存できなくなった（たまに必要）

関連リンク
==========

* 2018/2/23: RubyMine（または他のJetBrains社製IDE）でgit pushやgit pullでエラーが出るようになった場合の対処方法
  https://qiita.com/jnchito/items/9d07f34244b340394cb1

* 2018/2/27: IntelliJベースのIDE（PyCharmとか）でGitHubにSSH接続できなくなった
  https://blog.jetbrains.com/jp/2018/02/27/920

* 2018/3/7: PyCharm 2016.3以降の更新版でGitHubに繋がるようになった
  https://blog.jetbrains.com/pycharm/2018/03/pycharm-2016-3-and-later-updated-for-github-compatibility/

* WSLからssh.exeを使いたい
  `TTY issue when running Win32 process from WSL · Issue #2406 · Microsoft/WSL`_


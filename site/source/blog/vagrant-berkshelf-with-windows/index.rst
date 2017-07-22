:date: 2013-10-23 00:30:00
:categories: ['vagrant', 'berkshelf', 'Ruby']
:body type: text/x-rst

===============================================================
2013/10/23 vagrant-berkshelf プラグインがWindowsでエラーになる
===============================================================

バージョン
============

* vagrant-1.2.4, 1.3.3, 1.3.5 どれでも
* vagrant-berkshelf-1.3.4
* berkshelf-2.0.10
* buff-shell_out-0.1.1

やろうとしたこと
=================

``vagrant-berkshelf`` プラグインをインストールしておくと、Berksfileに外部依存のcookbookを書いておくだけで、 ``vagrant up`` 時に自動的にcookbookを取得してきて、VM環境のchefで使えるようにしてくれます。

今までは ``librarian-chef`` を使っていたんですが、librarian-chefはもうメンテされてないし、berkshelfがvagrant界のデファクトスタンダードだろう、ということで、手元でlibrarian-chefを使っていたプロジェクトをberkshelfに移行しました。以前はvagrant-berkshelfの使い勝手が悪く、vagrant-berkshelfプラグインを入れた状態だとBerksfileが無いとvagrantが使えない問題がりましたが、今のバージョン(1.3.4)ではそういった問題も無くなっていました。

で、vagrant-berkshelf、Macでは問題なかったんですが、Windowsではうまく動作しませんでした。


起きたこと
==============

``vagrant up`` したらエラーになった。

Berksfile::

   site :opscode
   cookbook 'git'
   cookbook 'python-build',
     :git => 'https://github.com/shimizukawa/chef-python-build'


実行結果::

   $ vagrant up
   ...
   [Berkshelf] Using git (2.7.0)
   [Berkshelf] Failed to download 'python-build' from git: 'https://github.com/shimizukawa/chef-python-build' with branch: 'master' at ref: '772317acb4ea0524ad350b93edf46230c8f2e6ba'
   Berkshelf::CookbookNotFound: Cookbook 'python-build' not found in any of the default locations


調査
=======

実はMacでも同じようなエラーが出ていて、Vagrant-1.3.3で問題のある変更が入っていて、vagrant-berkshelfにgitリポジトリ指定したBerksfileを使うと上記の内容のエラーが出る、というものでした。

これ: https://github.com/RiotGames/vagrant-berkshelf/issues/93

この問題はVagrant-1.3.4で解消されたようです。

しかし、自分のWindows環境ではバージョンの組み合わせが異なるので、このチケットに載っていたデバッグ情報を元にコードを追ってみたところ、問題の場所を見つけました。berkshelfが依存しているbuff-shell_out-0.1.0で想定していない動作をしているようです。

こんなコード。 `buff-shell_out-0.1.0/lib/buff/shell_out.rb(L32)`__::

   pid         = Process.spawn(command, out: out.to_i, err: err.to_i)
   pid, status = Process.waitpid2(pid)
   exitstatus  = status.exitstatus

.. __: https://github.com/RiotGames/buff-shell_out/blob/v0.1.0/lib/buff/shell_out.rb#L32

ここで ``<NoMethodError: undefined method `exitstatus' for 0:Fixnum>`` という例外が出ていて、どうもstatusが ``Process.waitpid2`` の返値として想定される ``Process::Status`` クラスでは無いっぽい。

とりあえずパッチ当ててみたら直りました::

   exitstatus  = (status.kind_of? Fixnum)? status : status.exitstatus


報告
========

直してもらおうと思ってgithubで報告しようとしたところ、既に4ヶ月前に直ってました。オープンソースあるあるですね。
https://github.com/RiotGames/buff-shell_out/pull/1#issuecomment-26811039

直したけどリリースしてなかったようなので、はよリリースしておくれ、とコメントして、とりあえず手パッチした状態で使ってればいいかなと思ったところ、10分くらいで返事が来ました。

  | shimizukawa commented 18 minutes ago
  | +1, please release 0.1.1. I have faced with this issue.

  | ivey commented 8 minutes ago
  | 0.1.1 released - apologies, I didn’t realize this hadn’t gotten pushed out

  | shimizukawa commented 2 minutes ago
  | Thanks! It worked!

はや！ http://rubygems.org/gems/buff-shell_out/versions/0.1.1 これだ。更新します::

   $ vagrant plugin install buff-shell_out
   Installing the 'buff-shell_out' plugin. This can take a few minutes...
   Installed the plugin 'buff-shell_out (0.1.1)'!

これで ``vagrant up`` でchef cookbook取得などが無事動きました。便利すぎ。直ってよかった。

ということで、vagrant使うならberkshelfとvagrant-berkshelfを使いましょう。


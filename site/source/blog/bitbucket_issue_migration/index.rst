:date: 2015-01-18 23:00
:categories: ['Python', 'bitbucket', 'github']
:body type: text/x-rst

==========================================================
2015/01/18 BitbucketのIssueをGithubにマイグレーションする
==========================================================

先日、某プロジェクト(Sphinx)をBitbucketからGithubに移行しました。

その際 https://import.github.com/ を使いました。
これは、Github外のリポジトリをgitに変換しつつ取り込んでくれるGithubのサービスです。
これのおかげで、リポジトリ自体の移行は難しくありませんでした。

問題はIssueの移行でした。

https://import.github.com/ はIssueを移行してくれないので、やりたければ自前で行う必要が有ります。調べてみると、 bitbucket_issue_migration__ がよさそうな気がしましたが、調べてみると色々機能的に不足もありました。

.. __: https://github.com/haysclark/bitbucket_issue_migration


元のbitbucket_issue_migrationで出来ること
==========================================

出来ること
----------

* Bitbucketからissueを全件読み込み、GithubにIssueを1件ずつ登録
* GithubにIssueを登録するとき、各IssueのコメントをBitbucketから読み込み、それをGithubにコメント追加
* Issueやコメントの文面はそのままGithubに登録

問題
-----

GithubのIssue番号は、BitbucketのIssue番号に合わせたいところです。しかし登録順に自動採番されるので、BitbucketのIssueが途中1件削除されていると登録するIssueの番号ズレが発生します。また、途中で失敗したらやり直しはできません。
IssueをBitbucketから取得するときは、BitbucketのREST APIで取得します。デフォルトの取得順は更新日順ソートです。APIの仕様で、IDでソートして取得することが出来ません。このため、全件取得してIDでソートする必要があります。

Issueのコメントにコミット番号やソースコードへのリンクが書かれている場合があります。コミット番号はGithub移行時にすべてhash値が変わっているためリンクされません。また、URLはすべてBitbucketを指してしまいます。

SphinxのIssue移行ではこういった問題を解決する必要がありました。

そこでコードを改造しようと思ったのですが、処理は全てオンメモリで行われるため、試す度にネット接続が必要でした。これはちょっとストレスでした。


fork版 bitbucket_issue_migration
=================================

出来るようにしたこと
--------------------

* Bitbucketから取得したデータをDISKにキャッシュ
* コメントが増えたりIssue更新された場合はキャッシュを更新
* Bitbucketから取得したデータを一旦issues.jsonに書き出すオプションを追加
* BitbucketのIssue番号飛びを検知してダミーIssueを挿入するようにした
* 書き出したissues.jsonからGithubへIssue投稿するオプションを追加
* issues.jsonの文面(URL, コミットhash, 投稿者名)を変換するツールを実装
* コミットhash変換のデータ用意のためにgitのログをjson出力するツールを実装
* コミットhash変換のデータ用意のためにhgのログをjson出力するツールを実装
* ID/PW認証ではGithubに100投稿/hまでしか実行出来ない。API Token利用なら5000投稿/hまで許可されているのでToken指定オプションを追加
* マイルストーン、コンポーネント、などを移行する実装forkがあったのでそれをマージ

これで大体やりたいことが出来ました。

ソースコード: https://github.com/sphinx-doc/bitbucket_issue_migration

また、SphinxのIssue移動時に使った手順はこれです:
https://github.com/sphinx-doc/bitbucket_issue_migration/blob/master/EXAMPLES.md

約1600件のIssueとそのコメントを移行するのに、6時間くらいかかりました。

出来ないこと
-------------

* @username のBitbucket/Githubでのマッピング。偶然同じIDの人もありえるので全てBitbucketのユーザーのURLに変換しました。
* Bitbucketでステータス変更しただけの、コメント本文が空のコメントの移行。BitbucketのAPIが出力してくれないので無理でした。
* Pull-Requestの移行。これは移行してもしょうがないので。
* 文中の ``pull request #123`` のリンク先変換。忘れてました。実装してません。


問題
-----

Githubへの投稿に自分のアカウントを使ったため、移行した全てのIssueの作成者が自分になってしましました。どのIssueを見ても自分のアイコンが表示されるというのはちょっと困りものです。本当に自分が作成したIssueを探せないし。

もう一度やり直せるなら、Issue移行用のアカウントを作成してそれを使って投稿したいところです。


まとめ
=======

BitbucketからGithubへのIssue移行ツール、けっこうがんばって作ったけど、自分が使う機会はもうなさそう。



:date: 2012-07-09 17:30:00
:tags: python, celery
:body type: text/x-rst

==========================================================
2012/07/09 Celery 3.0 リリースノートてきとう和訳
==========================================================

*'python', 'celery'*


2012/7/7にcelery3.0がリリースされたようなので、 `What's new in Celery 3.0 (Chiastic Slide)`_ のHighlights Overviewを把握がてらてきとうに和訳してみました。

.. _`What's new in Celery 3.0 (Chiastic Slide)`: http://docs.celeryproject.org/en/latest/whatsnew-3.0.html


Overview
==============

* 新しいAPIを追加して既存のAPIも改善したので、シンプルでパワフルになったよ。みんなチュートリアルから読み直してね(必須)
* workerがスレッド使わなくなってパフォーマンスがチョー良くなったよ
* 新しい "Canvas" っていうやつを使うと複雑なtaskのワークフロー制御を簡単に定義できるよ。
* 全てのCeleryのコマンドラインは1つのcleeryコマンドのサブコマンドになったよ::

     celeryd -> celery worker
     celerybeat -> celery beat
     camqadm -> celery amqp

* CeleryがPython 2.5をサポートするのはこれで最後だよ。Celery3.1からはPython2.6以上必須だよ
* librabbitmqが入っていればamqplibより優先的に使うよ。librabbitmqは超速くてメモリも最適化されてるよ。
* Redisがどうとか(Redis support is more reliable with improved ack emulation.)
* Celeryは完全UTC化したよ
* Over 600 commits, 30k additions/36k deletions.


感想
======

Canvas使ってみたい。どこまでTaskの順番や状態による実行を制御出来るか知りたいな。


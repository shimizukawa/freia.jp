===========================================
Python Hack-a-thon 5 ハンズオン 中級コース
===========================================

DocTestで覚えるTDDのリズム
============================

担当: 清水川


このハンズオンでは、以下の内容について体験していきます。

1. PythonのDocTestを使ってみよう
2. TDDをDocTestでやってみよう

環境
-----

* WindowsでもMacでもUnix系でも。
* Pytohn2.6～3.x ただしこの資料は2.6しか動作保証しません

Test Driven Development について
---------------------------------
Test Driven Development = TDD, 日本語で言うと ``テスト駆動開発`` です。
TDDはその名の通り、テストで開発を駆動する手法で、簡単に言うと以下の
ステップで実装を進めていきます。

1. テストコードを書く
2. テストを実行する（実装前なのでエラーになる = RED）
3. テストコードを通す実装をする（fake it）
4. テストを実行する（とりあえずテストはパスする = GREEN）

このステップをRED, GREEN, RED, GREEN, ... と繰り返していくことによって、
余計な実装をせずに確実に動作するシンプルな実装を手に入れることが出来ます。

TDDの手法で開発を行うにはテストツールが必須ですが、そのためのツールとして
xUnitと言われるツールが一般的に知られています。Java向けの実装ならJUnit,
C言語向けならCUnit, C++向けならCppUnitなどがあり、Pythonにも標準ライブラリで
unittest モジュールが提供されています。

本ハンズオンでは、unittestは使わずにDocTestを使ってTDDを身につけていきます。


コンテンツ
----------

.. toctree::
    :maxdepth: 3

    quickstart
    exercise
    results



.. :date: 2018-04-07 22:00
.. :tags: Python, Django, Redshift

==========================================
Django Redshift Backend プロジェクトの移譲
==========================================

.. contents::
   :local:

動機
====

* 自分が使わなくなってしまったのと、生活が変わって時間がとれなくなってしまったため、プロジェクト存続の道を模索しました
* `How to become a hacker`_ か何かにも、OSSプロジェクトの引き継ぎの話があった気がする

.. _How to become a hacker: https://cruel.org/freeware/hacker.html


移譲先の検討
============

* Djangoのプロジェクトを多人数でメンテナンスする仕組み
* Ploneには Collective_ というのがある
* Djangoには Jazzband_ というのがある

  - Jazzband is a collaborative community to share the responsibility of maintaining Python-based projects.
  - Jazzband は、Pythonベースのプロジェクトの保守更新についての責務を共有する共同コミュニティです。

  JazzbandはDjangoに特化したコミュニティ、ではないっぽいですね（コミュニティ名はジャンゴ・ラインハルト Django Reinhardt にちなんでそうなのでDjango用かと思ってた）。

.. _Collective: https://collective.github.io/
.. _Jazzband: https://jazzband.co/

Jazzbandとは
============

各リンクの内容を読んで、重要そうだと思ったところをメモしました。

- About: https://jazzband.co/about

  序文

  - Jazzbandは、開発メンバーが少ないOSSプロジェクトを長期間維持するストレスから産まれました
  - コードへの貢献の障壁を下げて幅広いユーザーが協力できるようにするよう務めます
  - 責務を複数の人で共有し、プロジェクトを生かしつづけるための開発方法を見つけるのを助けます
  - つまり、協調コーディングです。

  参加方法

  - https://jazzband.co/account/login から参加登録する
  - 自動的にGitHubのorganizationに追加される
  - その後は次のようなことができるようになる: リポジトリの移譲、既存プロジェクトへのコミット、PyPIへの自動リリース

  行動規範

  - Code of Conduct https://jazzband.co/about/conduct
  - 人を攻撃したり差別的な発言をしたりしない、という行動規範

- Guidelines: https://jazzband.co/about/guidelines

  - 新しいプロジェクトを始めたり、転送する場合、以下のガイドラインに従うこと。
  - 特にプロジェクトを転送する前に慎重に検討してください。ガイドラインを遵守してないプロジェクトはRoadiesによって躊躇なく削除されます。

Jazzbandへの参加でやったこと
============================

- Django Redshift BackendのIssueに、移行しますチケットを立てた: https://github.com/shimizukawa/django-redshift-backend/issues/30
- About: https://jazzband.co/about を一通り読んだ
- Code of Conduct https://jazzband.co/about/conduct  を一通り読んだ
- https://jazzband.co/account/login から参加登録

  - Jazzband-botがGitHub OAuthの認可を求めてくるので、許可する
  - 数分後に招待メールが来るので、 ``Join Jazzband`` のリンクをクリックして承認する

  - .. figure:: jazzband-members-shimizukawa.*
       :target: https://github.com/orgs/jazzband/people?query=shimizukawa

       347番目のJazzbandメンバーになりました

- Guidelines: https://jazzband.co/about/guidelines を読み中


（以下、更新中）


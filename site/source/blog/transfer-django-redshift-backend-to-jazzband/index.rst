:date: 2018-04-07 23:30
:tags: Python, Django, Redshift

================================================
Jazzband - PythonのOSSを保守する共同コミュニティ
================================================

`Django Redshift Backend`_ プロジェクトの移譲先を検討していて調べた、 Jazzband_ というコミュニティについて。

.. _Django Redshift Backend: https://pypi.org/project/django-redshift-backend/

.. contents::
   :local:

プロジェクト移譲の動機
======================

なぜ、 `Django Redshift Backend`_ プロジェクトを移譲しようと思ったのか。

* 自分が使わなくなってしまった
* 生活が変わって時間がとれなくなってしまった
* 利用者がそれなりにいるため、プロジェクト存続の道を模索した
* `伽藍とバザール`_ に **「5. あるソフトに興味をなくしたら、最後の仕事としてそれを有能な後継者に引き渡すこと。」** とあるので

.. _伽藍とバザール: https://cruel.org/freeware/cathedral.html


移譲先の検討
============

* OSSのプロジェクトを多人数でメンテナンスする仕組みがあれば、そこに移譲したい
* 移譲先として適切な仕組み（組織）がなかったら、引き継いでくれる個人が現れるのを待つ
* Ploneには Collective_ というのがある
* Djangoには Jazzband_ というのがある

  - Jazzband is a collaborative community to share the responsibility of maintaining Python-based projects.
  - Jazzband は、Pythonベースのプロジェクトの保守更新についての責務を共有する共同コミュニティです。

  JazzbandはDjangoに特化したコミュニティ、ではないっぽいですね（コミュニティ名がDjango Reinhardt にちなんでそうなのでDjango用かと思ってた）。

調べてみて、Jazzbandはガイドラインがしっかり書かれていて、やるべきことが明確だったので、第一候補として進めることにしました。Jazzbandのガイドライン（後述）は、Jazzbandに参加しないとしてもOSSプロジェクトを作るときには参考にすると役立つことが多いと思います。

.. _Collective: https://collective.github.io/
.. _Jazzband: https://jazzband.co/

Jazzbandとは
============

https://jazzband.co/ の各リンクの内容を読んで、重要そうだと思ったところをメモしました。

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

  1. 存続可能性: プロジェクトはコードスニペットや一発モノのオモチャではいけない。
  2. ドキュメント: 利用者向け **と** コントリビューター向け。インラインのコードコメントが推奨される。
  3. テスト: CIでの自動テスト
  4. 規範: プロジェクトはJazzbandの行動規範に則っていること。
  5. コントリビュートガイドライン: Jazzbandの情報をCONTRIBUTING.mdのヘッダに持たせる。
  6. バッヂ: Jazzbandのバッヂを掲載してもよい(オプション)

Jazzbandにプロジェクトを転送する準備としてやったこと
====================================================

- Django Redshift BackendのIssueに、移行しますチケットを立てた: `Issue#30 consider transferring ownership of this repository to Jazzband community <https://github.com/shimizukawa/django-redshift-backend/issues/30>`_
- About: https://jazzband.co/about を一通り読んだ
- Code of Conduct https://jazzband.co/about/conduct  を一通り読んだ
- Jazzbandに参加:

  - https://jazzband.co/account/login から参加登録
  - Jazzband-botがGitHub OAuthの認可を求めてくるので、許可する
  - 数分後に招待メールが来るので、 ``Join Jazzband`` のリンクをクリックして承認する

  - .. figure:: jazzband-members-shimizukawa.*
       :target: https://github.com/orgs/jazzband/people?query=shimizukawa

       347番目のJazzbandメンバーになりました

- Guidelines: https://jazzband.co/about/guidelines を一通り読んだ
- `Issue#30: consider transferring ownership of this repository to Jazzband community`_ で、共同開発者を募った。過去にPRをくれた人にメンション。
- `Issue#30: consider transferring ownership of this repository to Jazzband community`_ に、現状 Jazzband Guidelines を満たしているかどうかを確認してコメントした。

  1. 存続可能性: 可能だけど、もうすこし開発者が必要
  2. ドキュメント: 不足している。README.rstしかない。
  3. テスト: ある。
  4. 規範: 今はないがJazzbandのCoCを採用可能
  5. コントリビュートガイドライン: CONTRIBUTING.mdがない
  6. バッヂ: すぐ可能

現状、Jazzband Organizationに転送する前に、いくつかの準備が必要そう。ドキュメントの不足を補うことと、Jazzbandへの転送後にプロジェクトを生かし続けるには、いまのうちに共同開発者が必要。

まずは、一人でできることを準備しつつ、共同開発者を待つことにします。


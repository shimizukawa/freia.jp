:date: 2025-05-10 01:00
:tags: Nuxt, Scroll, SPA, History API

=====================================================================
Nuxt3 向け、スクロール位置復元モジュールの実装とnpmjs公開
=====================================================================

SPAアプリでF5リロードした時に、スクロール位置が復元されない問題を解決するためのNuxt3モジュール ``nuxt-scroll-restoration`` を作成し、npmで公開しました。これが、私のnpmで初めてのリリースになりました。

.. figure:: nuxt-scroll-restoration-on-npmjs.*

   npmjs での表示

モチベーション
=================

Nuxtでアプリを作ると、リロード時にスクロール位置が復元されません。
ページ編集結果を確認するためにリロードしたら、スクロール位置が失われて先頭が表示されてしまうため、共同編集中などにとても不便です。

従来のHTMLサイトではブラウザ標準のスクロール位置復元機能が働きますが、NuxtのようなSPAではそれが期待通りに動作しません。

解決策を探しているうちに `delayed-scroll-restoration-polyfill`_ を見つけましたが、これはJS一般用の実装だったため、Nuxt向けにそのままでは使えませんでした。そこで、Nuxt3用に調整したパッケージを作りました。

最近は AI Agent でコーディングしていることもあり、それほど時間をかけずにパッケージ公開まで出来るんじゃないだろうか？と思えたことも、動機の１つです。

.. _delayed-scroll-restoration-polyfill: https://github.com/janpaul123/delayed-scroll-restoration-polyfill

前提
=======

* Node 18+
* TypeScript
* Nuxt 3.9+
* `delayed-scroll-restoration-polyfill`_ (参考実装)

コードはGitHubで公開しています：

- https://github.com/shimizukawa/nuxt-scroll-restoration

npmパッケージ：

- https://www.npmjs.com/package/nuxt-scroll-restoration

実装アプローチ
==================

実装にあたって、 `delayed-scroll-restoration-polyfill`_ というパッケージを参考にしました。このコードをAI Agent（GitHub Copilot Agent + Sonnet 3.7）に参照させました。

まずは手元のNuxt3アプリ向けプラグインとして動作するようにコードを調整させました。数回の会話でそれなりに動作する状態になりましたが、Nuxt3は開発モードが重いので、「リロード後にスクロール位置が復元される」のを確認する人間側の作業にけっこう時間がかかりました。

次にnpmjsでパッケージ公開できるようにパッケージ化してもらいました。
自分自身はJSのパッケージを作ったことがありませんが、まあまあ良さそうな ``package.json`` が作れたと思います。


動作の仕組み / Archietecture
=======================================

このモジュールは以下のアーキテクチャでスクロール位置を復元します。

1. ブラウザの標準スクロール復元機能（ `history.scrollRestoration`_ ）を無効化
2. Historyのstate操作をフックして、現在のスクロール位置を記録
3. ページ遷移後、保存したスクロール位置に復元を試みる
4. 動的コンテンツの読み込みを考慮して、一定時間スクロール復元を繰り返し試行

.. _history.scrollRestoration: https://developer.mozilla.org/ja/docs/Web/API/History/scrollRestoration

.. code-block:: typescript

   // history APIの操作をオーバーライド
   const originalPushState = window.history.pushState;
   window.history.pushState = function (...args) {
     // 現在のスクロール位置を保存
     state = {
       ...state,
       __scrollX: window.scrollX,
       __scrollY: window.scrollY
     }
     return originalPushState.apply(window.history, args);
   };

この実装では、History APIを上書きしてスクロール位置を記録し、popstate時やページロード後にその位置に復元します。また、コンテンツが非同期に読み込まれる場合に備えて、一定時間をかけてスクロール位置の復元を試みます。

シーケンス図
-------------

動作の流れを以下のシーケンス図で表現します。

.. mermaid::

   sequenceDiagram
       participant Browser as ブラウザ
       participant NuxtApp as Nuxtアプリ
       participant HistoryAPI as window.history
       participant DOM as DOM
   
       Browser->>NuxtApp: Nuxtアプリケーションの読み込み
       NuxtApp->>HistoryAPI: scrollRestorationを"manual"に設定
       Note over HistoryAPI: ブラウザの標準スクロール復元を無効化
   
       NuxtApp->>HistoryAPI: pushStateとreplaceStateをオーバーライド
       Note over HistoryAPI: スクロール位置をstateに保存するフック
   
       NuxtApp->>NuxtApp: app:mountedフック
       Note over NuxtApp: アプリが完全にマウントされたことを確認
   
       Browser->>NuxtApp: ナビゲーション実行（リンククリックなど）
       NuxtApp->>HistoryAPI: 現在のスクロール位置を保存するreplaceState呼び出し
       HistoryAPI->>HistoryAPI: state内に__scrollXと__scrollYを保存
   
       Browser->>NuxtApp: ページリロードまたはナビゲーション実行
       NuxtApp->>NuxtApp: page:finishフック
       Note over NuxtApp: ナビゲーション後にスクロール位置を復元
   
       NuxtApp->>HistoryAPI: 保存されたスクロール位置をstateから確認
       alt stateに有効なスクロール位置がある場合
           NuxtApp->>DOM: 保存された位置へのスクロール試行
           loop タイムアウトまたはスクロール成功まで
               DOM->>DOM: スクロールが可能か確認
           end
       else 有効なスクロール位置がない場合
           NuxtApp->>DOM: トップ(0, 0)へスクロール
       end
   
       Browser->>NuxtApp: popstateイベント発生
       NuxtApp->>HistoryAPI: イベントからstateを取得
       HistoryAPI->>NuxtApp: 保存されたスクロール位置を提供
       NuxtApp->>DOM: スクロール位置を復元

適切なフックポイントの調査
----------------------------------------------

シーケンス図で、 ``page:finish`` と書きましたが、これが良いフックポイントなのかはよく分かっていません。
手元のNuxt3アプリではうまくいくようですが、Nuxt3プレイグランドではうまくいきませんでした。

そこで、次のようなテストプラグインを実装して、フックポイントを調査しました。

.. code-block:: typescript

   import type { Router, RouteLocationNormalized } from "vue-router";
 
   export default defineNuxtPlugin((nuxtApp) => {
     console.log("plugin", "test.ts")
     for (const key of [
       "app:created",
       "app:error",
       "app:error:cleared",
       "app:data:refresh",
       "vue:setup",
       "vue:error",
       "app:rendered",
       "app:redirected",
       "app:beforeMount",
       "app:mounted",
       "app:suspense:resolve",
       "link:prefetch",
       "page:start",
       "page:finish",
       "page:transition:finish",
     ]) {
       // console.log("# register nuxtApp.hook", key);
       nuxtApp.hook(key, () => {
         console.log("nuxt", key);
       });
     }
 
     (nuxtApp.$router as Router).beforeResolve(
       (to: RouteLocationNormalized, from: RouteLocationNormalized) => {
         console.log("router", "beforeResolve");
       }
     );
 
     (nuxtApp.$router as Router).beforeEach(
       (to: RouteLocationNormalized, from: RouteLocationNormalized) => {
         console.log("router", "beforeEach");
       }
     );
 
     (nuxtApp.$router as Router).afterEach(
       (to: RouteLocationNormalized, from: RouteLocationNormalized) => {
         console.log("router", "afterEach");
       }
     );
 
   });


この後、ブラウザの開発コンソールとにらめっこしながら、良さそうなフックポイントを決めました。

JSモジュール作成とnpmjs公開
=================================

npmjsでパッケージ公開できるようにパッケージ化する作業は、 AI Agent がやってくれました。やってくれたのですが、さすがに何も知らないままリリースするのはどうかと思い、 ``npm run dev`` で実行されるプレイグラウンド（デモ）の動作くらいは確認しようかと思いました。そこで、手元のNuxt3アプリでは動作しても、プレイグラウンドでは動作しないことに気付いてしまい、良い感じに動作するよう調整するのに数時間かかりました。

また、READMEドキュメントは日英を用意しましたが、どちらも AI Agent が書いてくれたものを微調整した程度で採用しました。

使い方
==========

Nuxtプロジェクトに以下のようにインストールし、pluginとして設定します。

.. code-block:: bash

   npm install nuxt-scroll-restoration

``nuxt.config.ts`` に追加：

.. code-block:: typescript

   export default defineNuxtConfig({
     modules: [
       'nuxt-scroll-restoration'
     ],
     
     // オプション設定（任意）
     scrollRestoration: {
       scrollRestorationTimeoutMs: 3000, // 最大試行時間（ミリ秒）
       tryToScrollIntervalMs: 50        // 試行間隔（ミリ秒）
     }
   })

これで、ブラウザバックやリロード時にスクロール位置が復元されるようになります。

制限事項
============

このモジュールにはいくつかの制限事項があります：

1. ブラウザのHistory APIサポートが必要（ほとんどのモダンブラウザは対応済み）
2. 動的コンテンツの読み込みタイミングによっては正確な復元が難しい場合がある
3. スクロール復元の最大試行時間は3秒（デフォルト）

まとめ
========

Nuxtモジュールを作成して公開することで、他のNuxtユーザーにも便利な機能を提供できると思いますが、それよりも、仕事のコードから分離することで個人的に探究することができ、ついでにnpmjsでパッケージ公開するところまで出来ました。

実装自体はそれほど複雑ではありませんが、Nuxtのローディング処理のどこに差し込むとよいかを測るのはけっこう大変でした。これをモジュール化することで再利用性が高まり、導入も簡単になります。また、個人開発のパッケージにすることで、仕事の都合で雑多な処理が入り込むこともなくなり独立性を確保出来ました。

今のところ、シンプルな目的が達成できているのでこれ以上機能追加することはないような気がしていますが、今回対応していない機能もいくつかあります。例えば、textareaのスクロール位置の復元には対応していません。また、アプリによってはうまく適合しない可能性もあります。フィードバックをもらえたら修正、機能追加してみようと思います。

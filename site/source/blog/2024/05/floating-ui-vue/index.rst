:date: 2024-05-02 15:00
:tags: Vue, VueTippy, tippyjs, popper

=================================================================
Floating UI/Vue でバルーン表示（VueTippyから乗り換え）
=================================================================

Webアプリでよく見かける、バルーン（吹き出し）表示を作るためのライブラリが `Floating UI`_ です。

.. figure:: ./floating-image.*

   "?" アイコンにマウスオーバーすると表示されるバルーンの例

表示のデザインやアニメーション込みですぐに使えるライブラリには VueTippy_ などがあって、私も :doc:`../../03/markdown-it-customize/index` では **VueTippy** を使いました [#]_ 。しかし、いくつかの問題があって、 **Floating UI** に乗り換えることにしました。

その結果、バルーンの位置制御という一番面倒な処理だけを外部ライブラリに任せて、調整したい表示部分を自由に扱えるようになりました。

.. figure:: ./20240502-demo.mp4
   :class: controls

.. [#] https://github.com/shimizukawa/vue-md-editor-vdom/commit/54c3d045f909af666a4005f931a1a91db76b0c5e

.. _Floating UI: https://floating-ui.com/
.. _VueTippy: https://vue-tippy.netlify.app/

モチベーション
=====================

これまで使っていた **VueTippy** には、気分的なものも含めて、以下のようないくつかの問題がありました。

- やりたいことに対して機能が豊富すぎる: 使い方を把握する必要があるのか判断できないオプションがたくさんあって、うまく動作しないときにそういったオプションで解決するのか等を調べるのに時間がとられました。
- ライブラリの階層が深すぎる: オプションの多くは親ライブラリの **Tippy.js** が提供していて、そこで説明されていない場合はさらに親の **Popper** を調べる必要がありました。
- トラブル時の解決に手間がかかりすぎる: 問題解決のためにソースコードを読んでも、3つの階層を把握して原因を探るのは大変でした。

トラブル解決のためにバージョンを変えてみようと思い調べたところ、親ライブラリたち **Tippy.js** と **Popper** のリリースが止まっていて、Popper後継の **Floating UI** がリリースされてることが分かりました。

.. csv-table:: 最新バージョンとリリース日
   :header-rows: 1

   名前,URL,バージョン,リリース日
   VueTippy,https://vue-tippy.netlify.app/,6.4.1,2023/12/27
   Tippy.js,https://atomiks.github.io/tippyjs/,v6.3.7,2021/11/10
   Popper,https://popper.js.org/,2.11.8,2023/05/27
   Floating UI,https://floating-ui.com/,1.6.1,2024/04/28

**Floating UI** はアンカー座標に対するポジショニング処理を提供するライブラリで、表示用デザインやアニメーション処理などは提供していません。そのため、VUeTippyのようにタグを書くだけで良い感じに表示されるわけではなく、どうやって表示するかを自分で実装する必要があります。そのため、out-of-the-boxで使いたいケースでは利用のハードルがあります。

**Floating UI** には表示部分の機能はありませんが、 ``@floating-ui/vue`` を提供してくれているためVueへの組み込みは比較的簡単に行えます。そこで、多機能なVueTippの代わりに ``@floating-ui/vue`` を使ってポップアップ表示を組み込むことにしました。

なお、React向けには ``@floating-ui/react*`` が提供されていて、Vue向けよりも機能提供されているようです。
React向けについては、以下の情報を参照してみてください。

- `React | Floating UI`_
- `Floating UIのすすめ: 特徴と使い方を紹介 - Sansan Tech Blog`_

.. _`React | Floating UI`: https://floating-ui.com/docs/react
.. _`Floating UIのすすめ: 特徴と使い方を紹介 - Sansan Tech Blog`: https://buildersbox.corp-sansan.com/entry/2024/01/31/110000

前提
=======

* Node 18
* TypeScript
* Vue 3.4.14
* ``@floating-ui/vue`` 1.0.6

  * ``@floating-ui/core`` 1.6.0
  * ``@floating-ui/dom`` 1.6.3
  * ``@floating-ui/utils`` 0.2.1

コードはGitHubにあります。

https://github.com/shimizukawa/vue-md-editor-vdom/tree/2024.05.02


@floating-ui/vue の使い方
=================================

基本は、おおよそ以下の公式ドキュメントで紹介されています。

- `Vue | Floating UI`_

この公式ドキュメントを読みつつ、今回実装した `Floating.vue`_ を読めば把握できると思います。

今回実装した ``<Floating>`` コンポーネントは、 ``@floating-ui/vue`` にインタラクション制御とデザインをくっつけたものです。全体は、コードコメント40行、scriptが100行くらい、30行弱、70行くらいです。

以下の様に、VueTippyっぽく書けるようにできるだけインターフェースを合わせて作りました。

.. code-block:: html

   <Floating placement="top-start" theme="warning" :delay="200">
     <template #default>
       <button>?</button>
     </template>
     <template #content>
       <div class="hint">
         Virtual DOM is a programming concept where an ideal, (略)
       </div>
     </template>
   </Floating>

以下のセクションでは、私が最初分からなかった点をいくつか紹介します。

.. _`Vue | Floating UI`: https://floating-ui.com/docs/vue
.. _Floating.vue: https://github.com/shimizukawa/vue-md-editor-vdom/blob/2e47317eb6247ca727cb593cf0cda53e6f5f8d1a/src/components/Floating.vue

ユーザー操作による表示、非表示の制御
---------------------------------------

``@floating-ui/vue`` は表示、非表示の制御を提供していません。このため `チュートリアル`_ ではイベントリスナーでCSSの ``display`` を切り替える方法が紹介されています。

これは実装面倒だなー、と思ったのですが、Vueなのだから ``v-if`` や ``v-show`` で制御ができます。
そして条件のトリガーにはVue本体やVueUseの機能が使えます。

そこで、VueUseの useElementHover_ を使って、ターゲットエレメントにマウスホバーした時に表示するように実装しました。また、バルーン表示上にマウスホバーしている間は表示を維持したいため、マウスがターゲットとバルーンのどちらかにあれば表示を維持するようにしました。

.. code-block:: ts

   const isTargetHovered = useElementHover(targetRef, {
     delayEnter: delayOptions.value.delayEnter,
     delayLeave: delayOptions.value.delayLeave + (interactive.value ? 100 : 0),
   });
   const isTooltipHovered = useElementHover(floatingRef, {
     delayEnter: 0, // keep tooltip open when hovering over the tooltip
     delayLeave: delayOptions.value.delayLeave,
   });
   const isTriggered = computed((): boolean => {
     const triggered = triggerRef.value ?? isTargetHovered.value;
     if (interactive.value) {
       return triggered || isTooltipHovered.value;
     } else {
       return triggered;
     }
   });

実際のコードは以下にあります:
https://github.com/shimizukawa/vue-md-editor-vdom/blob/2e47317eb6247ca727cb593cf0cda53e6f5f8d1a/src/components/Floating.vue#L115-L130

.. _チュートリアル: https://floating-ui.com/docs/tutorial#functionality

親エレメントの指定
--------------------

コンポーネントはその親のDOM要素の範囲で表示されますが、バルーン表示がその範囲でしか表示できないと困る事があります。例えば、テーブルセル内でしか表示できない場合、ほとんど見えないことになってしまいます。
対策として、こういったライブラリではバルーンのコンテンツ部分のDOMをたとえばbodyタグ直下に移動するなどして表示していますが、それを実装するのは面倒だなーと思いました。

Vueでは Teleport_ コンポーネントを使う事で任意のDOM配下に要素を移動できるので、これを使って実装しました。

.. code-block:: html

   <Teleport v-if="slots.content" to="body">
     <div ref="floatingRef">
       <slot name="content" />
       <div v-if="arrowProp" />
     </div>
   </Teleport>

実際のコードは以下にあります:
https://github.com/shimizukawa/vue-md-editor-vdom/blob/2e47317eb6247ca727cb593cf0cda53e6f5f8d1a/src/components/Floating.vue#L165C1-L185C14


まとめ
===========

組み込んでみて分かった事ですが、ポップアップの表示条件や表示時間の制御などは、使い慣れた仕組みで実装すればそれほど手がかかりませんでした。今回は表示条件の制御にVueUseの useElementHover_ を使い、DOM配置にはVueの `スロット`_ や Teleport_ を使いました。

また、デザイン調整もCSSの ``box-shadow`` で影を付ける程度で十分なものができました。

この切り替えによって、以下の様なメリットデメリットがありました。

- デメリット　

  - out-of-the-boxですぐ使える状態を失った
  - 200行ほどの自前実装が必要になった

- メリット

  - 多階層でデバッグしづらい状況から脱却した
  - 表示制御はよく知っているコードなのでカスタマイズが容易になった
  - 依存ライブラリのサイズがgzip時で半分になった

.. _useElementHover: https://vueuse.org/core/useelementhover/
.. _スロット: https://ja.vuejs.org/guide/components/slots
.. _Teleport: https://ja.vuejs.org/guide/built-ins/teleport


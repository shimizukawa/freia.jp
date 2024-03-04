:date: 2023-11-25 15:00
:tags: Vue, VirtualDOM, Markdown, Mermaid

============================================================================
Vue MarkdownエディタにMermaidを組み込んで仮想DOMでレンダリング
============================================================================

MermaidJS_ をサイトに組み込む場合、多くのケースではMermaidが ``pre.mermaid`` を認識してグラフ等をレンダリングします。

.. _MermaidJS: https://mermaid.js.org/

しかし、この方法をMarkdownエディタのプレビューに組み込むと、エディタ側を1文字変更するごとにMermaid記法をHTMLの ``pre.mermaid`` タグで出力して、改めてSVGに置き換える処理を行うことになります。その結果、 ``pre`` が ``SVG`` に差し替わるタイミングでエレメントの高さが変わってしまい、プレビュー側のスクロール位置がズレてしまう問題があります。

先日のblog :doc:`../vue-md-editor-vdom/index` でMarkdownエディタのプレビューを仮想DOMでレンダリングしました。
この延長で、MermaidのSVG出力も仮想DOMに含めるよう実装します。
そうすれば、変更がないエレメントは更新されないし、変更があるエレメントもはじめからSVGでレンダリングされるため、不要な高さ変更やそれに伴うスクローズ位置のズレを防止できます。

実装した結果、以下のデモ動画のように期待する動作が得られました。

.. figure:: ./20231125-demo.mp4
   :class: controls

エディタに入力したとき、innnerHTMLによる更新（プレビューの左側）ではMermaidの高さが変化してスクロール位置が変わってしまっています。
しかし、仮想DOMによる更新（プレビューの右側）では高さが変わらずスクロール位置への影響もありません。


前提
=======

* Node 18
* Vue 3.3.4
* TypeScript
* markdown-it 13.0.2
* Mermaid 10.6.1

コードはGitHubにあります。

https://github.com/shimizukawa/vue-md-editor-vdom/tree/2023.11.25


Mermaidレンダーコンポーネント
========================================

Mermaid記法を受け取ってSVGをレンダリングする ``MarkdownRendererMermaid`` を実装しました。
コード全体は https://github.com/shimizukawa/vue-md-editor-vdom/blob/2023.11.25/src/components/MarkdownRendererMermaid.vue にあります。

Mermaid記法のSVGレンダリングでは、Vueプラグインで初期化した ``$mermaid`` を使います。
``$mermaid.parse()`` で記法のチェックを行い、エラーがあればそのまま画面に表示します。
エラーがなければ、 ``$mermaid.render()`` 関数でSVGをレンダリングします。

.. code-block:: ts

   const render = async () => {
     rendered.value = await renderMermaid(index.value, content.value);
   };
 
   const renderMermaid = async (index: number, code: string): Promise<string> => {
     try {
       await $mermaid.parse(code);
     } catch ({ message }: any) {
       return message as string;
     }
 
     const { svg } = await $mermaid.render(`mermaid${index}`, code);
     return svg;
   };

``$mermaid.render()`` の第一引数はキャッシュキー（という理解）です。同じ値にするとキャッシュされたSVGを返してくるので、コンテンツ毎に変えます。キーに使っている ``index`` は記法が登場したエレメントの位置で、コンポーネントの外から受け取っています。

* ``$mermaid.render()`` のドキュメント: `mermaidjs.github.io/docs/mermaidAPI.md <https://github.com/mermaidjs/mermaidjs.github.io/blob/master/docs/mermaidAPI.md#render>`_

レンダリング結果は ``rendered`` に格納し、 ``v-html`` で表示します。
正常な場合はSVGが出力され、エラーがある場合は ``parse()`` が例外出力する ``message`` が画面に表示されます。

.. code-block:: html

   <template>
     <pre v-html="rendered" />
   </template>


仮想DOMへのMermaidコンポーネント追加
========================================

仮想DOMの構築時に、HTMLタグではなく任意のコンポーネントの指定もできます。
詳細は公式ドキュメント `レンダー関数と JSX | Vue.js <https://ja.vuejs.org/guide/extras/render-function.html>`_ にあります。

``MarkdownRendererMermaid`` コンポーネントを仮想DOMの構築に組み込むには、以下のように実装します。

.. code-block:: ts

    import { h } from 'vue'

    const index = !node.parentNode ? 0 : (
      [
        ...node.parentNode.querySelectorAll(".mermaid")
      ].findIndex((_node) => _node === node)
    );
    const vnode = h(
      MarkdownRendererMermaid, // type
      {
        content: node.textContent,
        index,
      }, // props
      null, // children / slot
    )

markdown-itの実装で、mermaidコードブロックはコードハイライトなどせずそのまま出力しています。
そのため、 ``node.textContent`` にはMermaid記法がそのまま格納されています。
また、一意なindexを用意するため、ノード全体での登場位置を算出してコンポーネントに渡します。

これで、Mermaid記法のコードブロックを書き替えたときに、スクロール位置への影響を無くせました。
また、SVGの生成を自前のコードで行っているため、連続で生成する場合にインターバルを設けて生成負荷を下げるといったことも可能になりました。

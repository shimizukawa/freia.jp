:date: 2023-11-19 12:00
:tags: Vue, VirtualDOM, Markdown

============================================================================
VueでMarkdownのプレビューをVueの仮想DOMで表示する 
============================================================================

動機 / モチベーション
============================

Markdown エディタとそのプレビューを作ったんですが、エディタ側を1文字変更するごとにプレビュー側の全エレメントが更新されてしまいました。
このため、画像の再ロードが発生したり、それに伴ってエレメントの高さが変わってしまうため、プレビュー側のスクロール位置が編集中どんどんズレていったり、などの問題がありました。

.. figure:: ./20231119-vhtml.mp4
   :class: controls

Vueは **仮想DOM** っていうやつで差分のあるエレメントだけ更新している、と思ったけど、全部更新されてるじゃん！と思って調べてみました。

全部更新されていた理由は、MarkdownをHTMLレンダリングしたあと、それを ``v-html`` に入れていたためでした。 ``innerHTML`` 相当なので、そのエレメント配下のエレメントは差分更新ではなく全更新になっていたというオチです。

.. code-block:: html

   <div class="preview" v-html="render(content)" />


前提
=======

* Node 18
* Vue 3.3.4
* TypeScript
* markdown-it 13.0.2

コードはGitHubにあります。
https://github.com/shimizukawa/vue-md-editor-vdom/tree/main


仮想DOMの構築
===================

公式ドキュメント `レンダー関数と JSX | Vue.js <https://ja.vuejs.org/guide/extras/render-function.html>`_ によると、コンポーネントの ``setup`` で ``render`` 関数を返し、その ``render`` 関数が仮想DOMを構築して返せばよさそうです。

HTMLに対応する仮想DOMの構築は以下のような関係になっています。

.. code-block:: html

    <div id="foo" class="bar">
      Hello <strong>World!</strong>
    </div>

.. code-block:: ts

    import { h } from 'vue'

    const vnode = h(
      'div', // type
      { id: 'foo', class: 'bar' }, // props
      [ // children
        "Hello,",
        h('strong', 'World!'),
      ]
    )

この置き換えを行うために、HTMLをparser代わりの ``div.innerHTML`` に突っ込んで、 ``div.childNode`` を対象に仮想DOM化する処理を行えばよさそうです。

``render`` 関数は以下の様になります。

.. code-block:: ts

    export default defineComponent({
      setup(props) {
        // レンダー関数を返す
        return () => {
          if (!props.content) {
            return h("div");
          }
  
          const outer = document.createElement("div");
          outer.innerHTML = props.content;
  
          return walkNodes(outer);
        };
      },
    });

``walkNodes`` 関数の実装は、実装方法がいくつかあります。

Markdown のプレビュー用途であればパラグラフ単位で差分更新できれば充分なので、ルート直下のノードそれぞれを仮想DOMにして、それらに属するHTMLは ``innerHTML`` で持たせてしまっても良さそうです。

.. code-block:: ts

    export default defineComponent({
      setup(props) {
        const walkNodes = (node: HTMLElement): any => {
          return Array.from(node.childNodes).map((_node) => {
    
            if (_node.nodeType === Node.TEXT_NODE) {
              return _node.textContent || "";
            } else if (node.nodeType === Node.ELEMENT_NODE) {
              const _props: any = {};
              for (let i = 0; i < _node.attributes.length; i++) {
                const attr = _node.attributes[i];
                _props[attr.name] = attr.value;
              }
              _props["innerHTML"] = _node.innerHTML;
              return h(
                node.tagName.toLowerCase(),
                _props,
              );
            } else {
              throw new Error("Not implemented nodeType: " + node.nodeType);
            }
          });
        };

        // レンダー関数を返す
        return () => {
          ...
        };
      }
    });

一方で、子ノードを全て仮想DOMとして扱えるようになれば、一部の子ノードを別のコンポーネントに差し替えたり、イベントハンドラを設定したりなど、色々差し込めるようになるので応用が利きそうです。
ノードツリーを全て辿って仮想DOMに置き換える、ビジターパターンで実装したコードはGitHubにあります。
https://github.com/shimizukawa/vue-md-editor-vdom/blob/main/src/components/MarkdownRenderer.ts

これで、プレビュー上の変更差分だけが更新されました。

.. figure:: ./20231119-vdom.mp4
   :class: controls

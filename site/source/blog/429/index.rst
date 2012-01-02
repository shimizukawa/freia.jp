:date: 2007-03-27 23:55:00
:categories: ['Plone']
:body type: text/x-rst

================================================
2007/03/27 PloneでReferenceのW/F状態による色分け
================================================

*Category: 'Plone'*

自宅サーバーのPloneはデフォルトステータスを非公開にしているため、時々ステータスを公開に変更し忘れてしまうことがある。大抵は単に公開されないだけなので後で気がつけば問題ないが、COREBlog2の ``オブジェクトの関連づけ`` で関連づけられた先のオブジェクトが非公開状態の場合、BlogのエントリやBlogのTopページを表示しようとしたときに認証画面に遷移してしまう。

Blog記事を書いたときにどうして気づかないのか、というと、記事を書いてるときは認証済みの状態のため、非公開の関連づけオブジェクトがあっても問題なく表示できてしまう。ここで、表示できてしまっても気づけるようにするため、Plone本体と同じように、関連づけオブジェクトのタイトル文字列に、W/Fの状態による色分けを設定してみる。

COREBlog2/skins/COREBlog2/media_view.pt

.. code-block:: xml

    <!-- macro for Image -->
    <metal:commentform_macro define-macro="image"
     tal:define="scale python:test(mediasizestr != 'no_resize',mediasizestr,None);
                 getInfoFor python:wtool.getInfoFor;
                 item_wf_state obj/review_state|python:getInfoFor(obj, 'review_state', '');
                 item_wf_state_class python:'state-'+normalizeString(item_wf_state);
                 ">
    <div class="contentsHanderItem">
        <div class="contentsHanderImageWrapper">
            <a href="#"
               tal:attributes="href obj/absolute_url;
                               target string:_blank;
                               ">
                <div tal:replace="structure python:obj.tag(scale= scale,css_class='contentsHanderImage')" />
            </a>
        </div>
        <span class="contentsHanderImageCaption"
              tal:content="obj/pretty_title_or_id"
              tal:attributes="class string:$item_wf_state_class contentsHanderImageCaption;" />
    </div>
    </metal:commentform_macro>

ポイントは最初と最後。 item_wf_state_class にcss用のクラス名を生成・代入しておき、タイトル部分でtal:attributesを使ってclassを設定する。色はPloneのものを使用する。

とりあえずこれで見た目で気づくことが出来るようになる。


.. :extend type: text/html
.. :extend:


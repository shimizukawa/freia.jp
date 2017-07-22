:date: 2012-04-09 23:40:00
:categories: ['Python', 'docutils', 'development']
:body type: text/x-rst

======================================================
2012/04/09 Docutilsのnode-treeを疑似XMLで出力する
======================================================

rst2textileを実装する過程でreStructuredTextのnode-treeを見たくなったので以下のようにして出力してみました。


.. code-block:: bash

   $ rst2pseudoxml.py in.rst out.pxml

   または

   $ python -c "from docutils.core import publish_cmdline as p; p()" in.rst out.pxml

このコマンドに渡している `in.rst` の内容は以下の通りです。

.. code-block:: rst

   ==========
   Heading1
   ==========

   :Date: Today
   :Author: SpamEgg
   :Location: Here

   Heading2
   ==========

   Heading3
   ----------

   Heading4
   ^^^^^^^^^^

   *emphasized* (e.g., italics)

   **strongly emphasized** (e.g., boldface)

   - An item in a bulleted (unordered) list

   - Another item in a bulleted list

     - Second Level

     * Second Level Items

       * Third level

   #. An item in an enumerated (ordered) list xxxxxxx

   #. Another item in an enumerated list yyyyyy

      #. Another level in an enumerated list vvvvvvvv


   Blockquotes

      This text will be enclosed in an HTML blockquote element.

      Second Paragraph.

   Links

      `link text <link_address>`_

   Images

       .. image:: imageurl


これが以下のような `out.pxml` に出力されます。

.. code-block:: xml


   <document ids="heading1" names="heading1" source="sample.rst" title="Heading1">
       <title>
           Heading1
       <docinfo>
           <date>
               Today
           <author>
               SpamEgg
           <field>
               <field_name>
                   Location
               <field_body>
                   <paragraph>
                       Here
       <section ids="heading2" names="heading2">
           <title>
               Heading2
           <section ids="heading3" names="heading3">
               <title>
                   Heading3
               <section ids="heading4" names="heading4">
                   <title>
                       Heading4
                   <paragraph>
                       <emphasis>
                           emphasized
                        (e.g., italics)
                   <paragraph>
                       <strong>
                           strongly emphasized
                        (e.g., boldface)
                   <bullet_list bullet="-">
                       <list_item>
                           <paragraph>
                               An item in a bulleted (unordered) list
                       <list_item>
                           <paragraph>
                               Another item in a bulleted list
                           <bullet_list bullet="-">
                               <list_item>
                                   <paragraph>
                                       Second Level
                           <bullet_list bullet="*">
                               <list_item>
                                   <paragraph>
                                       Second Level Items
                                   <bullet_list bullet="*">
                                       <list_item>
                                           <paragraph>
                                               Third level
                   <enumerated_list enumtype="arabic" prefix="" suffix=".">
                       <list_item>
                           <paragraph>
                               An item in an enumerated (ordered) list xxxxxxx
                       <list_item>
                           <paragraph>
                               Another item in an enumerated list yyyyyy
                           <enumerated_list enumtype="arabic" prefix="" suffix=".">
                               <list_item>
                                   <paragraph>
                                       Another level in an enumerated list vvvvvvvv
                   <paragraph>
                       Blockquotes
                   <block_quote>
                       <paragraph>
                           This text will be enclosed in an HTML blockquote element.
                       <paragraph>
                           Second Paragraph.
                   <paragraph>
                       Links
                   <block_quote>
                       <paragraph>
                           <reference name="link text" refuri="link_address">
                               link text
                           <target ids="link-text" names="link\ text" refuri="link_address">
                   <paragraph>
                       Images
                   <block_quote>
                       <image uri="imageurl">

今までこの構造を把握するのに手間取っていたけど、PseudoXMLを手に入れる方法が分かりました。これを見ながら rst2textile 用の TextileTranslator の visit_xxxx を実装していくのはそれほど難しくない作業でした。

だれかGUIの ``node-tree viewer`` 作らないかなー？


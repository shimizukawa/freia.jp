:date: 2007-04-21 23:55:00
:categories: ['Zope', 'Plone']
:body type: text/x-rst

=======================================
InstanceManagerでZope/Plone環境自動構築
=======================================

先日の `Zope Essentials 6`_ で仕入れたネタ InstanceManager を試してみました。
InstanceManagerはeasy_installで一発インストールできますが、その後の設定がけっこうめんどくさかったです。しかし、設定さえ出来てしまえば、同じ環境をなんどでもコマンド一発で再構築することが出来ます。

とりあえずインストール。Ploneのサイトからもダウンロードできますが、けっこうバグ修正が進んでいるようなので、easy_installを使うかリポジトリから取ってくるのが良いでしょう。

.. topic:: easy_install instancemanager
    :class: dos
    
    | c:\>easy_install instancemanager
    | Searching for instancemanager
    | 
    | Best match: instancemanager 1.0rc.dev-r36992
    | 
    | Installing instancemanager-script.py script to C:\Develop\Python24\Scripts
    | Installing instancemanager.exe script to C:\Develop\Python24\Scripts
    | 
    | Installed c:\develop\python24\lib\site-packages\instancemanager-1.0rc.dev_r36992-py2.4.egg
    | Processing dependencies for instancemanager


無事終わりました。次に一度、空起動します。INSTALL.txtによると、空起動によりホームディレクトリに.instancemanagerが作成され、そこにあるuserdefaults.pyがデフォルト設定を行うファイルになるようです。

.. topic:: instancemanager
    :class: dos

    | c:\>instancemanager
    | usage: Usage: instancemanager [options] [multi-action] <project>
    | multi-action: default ones are 'fresh' and 'soft'.
    | project: the name of the project, available projects are:
    |     You can look at userdefaults.py to change
    |     instancemanager to your local config.
    |     Or run instancemanager again with <project> and <action>.

ずらずらーっとusageが表示されますが、とりあえず無視してホームディレクトリ/.instancemanager/userdefaults.py を編集します。ここまでの実行はWindowsで行いましたが、Windowsだと色々と問題があるので、続きはUnixでやることにします。

うまく環境が構築できると、以下のコマンド一発でPloneの環境が添付画像のように構築されます。

.. topic:: instancemanager fresh
    :class: dos

    % instancemanager fresh testproj


つ・づ・く

- `Instance manager — plone.org`_
- `Revision 40922: /instancemanager`_

.. _`Revision 40922: /instancemanager`: https://svn.plone.org/svn/collective/instancemanager/
.. _`Instance manager — plone.org`: http://plone.org/products/instance-manager
.. _`Zope Essentials 6`: http://www.freia.jp/taka/blog/449


.. :extend type: text/html
.. :extend:

:date: 2007-12-15 15:23:53
:categories: ['python']
:body type: text/x-rst

=================================================
勝手に俺俺リファクタリング for やっつけスクリプト
=================================================

気分転換に、知り合いのblogに載ってたPythonコードを勝手に俺俺リファクタリングしてみます。方針としては、動作を変えず、可読性を損なわず、で。自分ならこう書く、というくらいのものです。

- 元記事: `2007-12-14 - 倖せの迷う森`_

*# こういうの、* cookbook_ *か* `ja.doukaku.org`_ *にありそうだなあ。*

以下、元記事の課題と、俺俺リファクタリング。

.. _`2007-12-14 - 倖せの迷う森`: http://d.hatena.ne.jp/ocs/20071214#1197631241
.. _cookbook: http://aspn.activestate.com/ASPN/Python/Cookbook/
.. _`ja.doukaku.org`: http://ja.doukaku.org/


.. :extend type: text/x-rst
.. :extend:
.. Topic:: 課題

  指定したディレクトリをルートとして、このディレクトリ以下のすべての java ファイルに対して class のコメントを編集します。

変換元ファイル::

  /**
   * Action の基底クラスです。<br>
   * すべての Action は、このクラスを継承します。
   * 
   * @author foo
   */
  public abstract class BaseActionSupport extends ActionSupport {


変換先ファイル::

  /**
   * Action の基底クラスです。<br>
   * すべての Action は、このクラスを継承します。
   * 
   * @author foo
   * @version $Revision$
   * Copyright: (C) xxxxxxxxxx All Right Reserved.
   */
  public abstract class BaseActionSupport extends ActionSupport {


以下が元コード。

.. code-block:: python
    
    # -*- coding: sjis -*-
    import shutil
    import os
    import time
    
    ### functions
    def search_author_tag(filename):
        cnt = 0
        mark = 0
        for line in file(filename, 'r'):
            cnt += 1
            if line.startswith(' * @author'):
                mark = cnt
        
        return mark
    
    def copy_file(filename, srcdir, destdir):
        if not srcdir.endswith('\\'):
            srcdir += '\\'
        if not destdir.endswith('\\'):
            destdir += '\\'
        
        shutil.copy2(srcdir + filename, destdir + filename)
        return destdir + filename
    
    def set_version():
        return ' * @version $Revision$'
    
    def set_copyright():
        return ' * Copyright: (C) xxxxxxxxxx All Right Reserved.'
    
    def append_comment(filepath, mark):
        reader = file(filepath, 'r')
        buf = ''
        cnt = 0
        for line in reader:
            cnt += 1
            buf += line
            if cnt == mark:
                buf += set_version() + '\n'
                buf += set_copyright() + '\n'
        reader.close()
        writer = file(filepath, 'w')
        writer.write(buf)
        writer.close()
    
    
    ### variables
    rootdir = 'D:\\all-in-one-eclipse\\workspace\\someproject\\src\\'
    backupdir_base = 'D:\\backup$date$\\'
    backupdir = backupdir_base.replace('$date$', time.strftime('%y%m%d_%H%M%S'))
    
    
    ### main
    for root, dirs, files in os.walk(rootdir):
        newdir = root.replace(rootdir, backupdir, 1)
        
        if not '\\CVS' in newdir:
            os.makedirs(newdir)
            print 'Create: ' + newdir
            
            for fileentry in files:
                if fileentry.endswith('.java'):
                    # copy
                    destpath = copy_file(fileentry, root, newdir)
                    print 'Copy: ' + root + '\\' + fileentry + ' -> ' + destpath
                    
                    # set doc-comment
                    marker = search_author_tag(destpath)
                    print 'Info: ' + destpath + ': line ' + str(marker) + ': ' + ' @author タグを検出しました。'
                    append_comment(destpath, marker)



以下が俺俺リファクタリングしたコード。OS依存を無くす、os.path.joinを使う、内包表記で.javaだけ抽出、インデントを減らす、''.join(list)で文字連結、...などなどやってみました。

.. code-block:: python
    
    # -*- coding: sjis -*-
    import shutil, os, time
    
    ### functions
    def search_author_tag(filename):
        mark = 0
        for cnt,line in enumerate(file(filename, 'r')):
            if line.startswith(' * @author'):
                mark = cnt
        
        return mark
    
    def copy_file(filename, srcdir, destdir):
        src = os.path.join(srcdir, filename)
        dest = os.path.join(destdir, filename)
        shutil.copy2(src, dest)
        return dest
    
    def set_version():
        return ' * @version $Revision$'
    
    def set_copyright():
        return ' * Copyright: (C) xxxxxxxxxx All Right Reserved.'
    
    def append_comment(filepath, mark):
        reader = file(filepath, 'r')
        buf = []
        for cnt,line in enumerate(reader):
            buf.append(line)
            if cnt == mark:
                buf.append(set_version()+'\n')
                buf.append(set_copyright()+'\n')
        reader.close()
        writer = file(filepath, 'w')
        writer.write(''.join(buf))
        writer.close()
    
    
    ### main
    def main(rootdir, backupdir):
        for root, dirs, files in os.walk(rootdir):
            newdir = root.replace(rootdir, backupdir, 1)
            if os.sep + 'CVS' in newdir:
                continue
    
            os.makedirs(newdir)
            print 'Create:', newdir
    
            files = [x for x in files if x.endswith('.java')]
    
            for fileentry in files:
                # copy
                destpath = copy_file(fileentry, root, newdir)
                srcpath = os.path.join(root, fileentry)
                print 'Copy: %(srcpath)s -> %(destpath)s' % locals()
    
                # set doc-comment
                marker = search_author_tag(destpath)
                ln = marker+1
                print 'Info: %(destpath)s: line %(ln)d:' \
                      ' @author タグを検出しました。' % locals()
                append_comment(destpath, marker)
    
    
    ### variables
    ROOTDIR = r'D:\all-in-one-eclipse\workspace\someproject\src\'
    BACKUPDIR_BASE = r'D:\backup$date$\'
    BACKUPDIR = BACKUPDIR_BASE.replace('$date$',
                                       time.strftime('%y%m%d_%H%M%S'))
    
    if __name__ == '__main__':
        main(ROOTDIR, BACKUPDIR)


行数は変更前・後変わらず71行。速度向上とかは特にしていないので、仕事でこの修正コストが認められるかどうかは微妙。(UnitTestコードも無いしね...)



.. :comments:
.. :comment id: 2007-12-16.7985907926
.. :title: Re:勝手に俺俺リファクタリング for やっつけスクリプト
.. :author: ocs
.. :date: 2007-12-16 01:23:19
.. :email: 
.. :url: 
.. :body:
.. なるほどなるほど。勉強になります。
.. 
.. > こういうの、 cookbook か ja.doukaku.org にありそうだなあ。
.. どう書くorgに似たようなネタがあった気もします。
.. まぁ向こうのほうがお題はハイレベルですが。
.. 

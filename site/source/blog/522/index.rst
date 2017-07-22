:date: 2008-01-25 00:05:16
:tags: python, WZ
:body type: text/x-rst

=====================================================
2008/01/25 WZMailの*.mbxをThunderbirdにインポートする
=====================================================

WZMailのメールボックスは \*.mbx ですが、中身が微妙に独自形式なので他へ移行する際にみんなそれぞれ苦労しているらしい。たしかWZの本家掲示板が生きていた頃にそんな話をいくつか見かけた気がする。

で、今回自分もThunderbirdへの移行を画策して、移行ツールを探してみたけど案の定「これ一発で行けますぜ旦那！」っていう感じのツールは見つからなかった。しょうがないので、変換スクリプトをPythonで書いてみたら意外とすぐいけてしまった。

変換できたら、Thunderbirdのメールデータ用フォルダに変換後のファイルを置いてThunderbirdを起動するだけでフォルダツリーに表示される。クリックするとインデックスの更新が行われて無事取り込み完了（のはず）。
文字コード変換の処理を手抜きしているので、変換できない文字が空白に置き換えられる。あと、Subjectが壊れることがあるみたい。5万件のメッセージを変換して10件くらいSubjectが壊れたけど、まあいいか。

ところで、1フォルダに5万件のメールが入ってると表示が遅いのは何とかならないものか。UIもいろいろ気になるところ...。Thunderbirdが手になじむツールになる日は..来るのだろうか？

というこで、以下、変換コードです。


.. :extend type: text/x-rst
.. :extend:

.. code-block:: python

    import os, sys
    
    def output(out, mfrom, stack):
        stack.insert(0, mfrom)
        out.write(''.join(stack))
    
    ignore_chars = r'\/:*?"<>|'
    
    def getsubject(filename):
        cfgname = filename[:-4] + '.cfg'
        f = file(cfgname,'r')
        for l in f:
            if l.startswith('Subject:'):
                subject = l[8:].strip()
                break
        else:
            subject = 'new_' + filename
    
        # char replace
        for c in ignore_chars:
            subject = subject.replace(c,'_')
    
        # name chooser
        if os.path.exists(subject):
            n = 0
            while os.path.exists(subject+str(n)):
                n += 1
            subject += str(n)
    
        return subject
    
    def main(filename):
        f = file(filename, 'r')
        subject = getsubject(filename)
        print subject
        o = file(subject, 'w')
        
        stack = []
        mfrom = 'From dummy\n'
        
        for l in f:
            if l == '\x08<mh>\n':
                print '.',
                output(o, mfrom, stack)
                stack = []
                mfrom = 'From dummy\n'
            else:
                try:
                    j = l.decode('cp932','replace').encode('iso2022-jp','replace')
                except:
                    print l
                    raise
                stack.append(j)
                if j.startswith('From:'):
                    mfrom = 'From '+j[5:]
                    mfrom = mfrom.strip() + '\n'
        else:
            if stack:
                output(o, mfrom, stack)
        
        o.close()
        f.close()
        print
    
    def conv_all_mbx():
        from glob import glob
        l = glob('*.mbx')
        for f in l:
            main(f)
    
    if __name__ == '__main__':
        if len(sys.argv) == 2:
            filename = sys.argv[1]
            main(filename)
        else:
            conv_all_mbx()


.. :comments:
.. :comment id: 2008-01-25.3823230908
.. :title: Re:WZMailの*.mbxをThunderbirdにインポートする
.. :author: M.Shibata
.. :date: 2008-01-25 02:39:43
.. :email: mshibata@emptypage.jp
.. :url: 
.. :body:
.. 自分も昔おんなじようなことしました。
.. http://www.emptypage.jp/whining/2006-09-24.html
.. Python はテキスト処理のパーサが書きやすいですよね。
.. で、Thunderbird からメールを IMAP のメールフォルダに移動させて Gmail で吸い上げました。
.. 
.. 
.. :comments:
.. :comment id: 2008-01-25.6142969273
.. :title: Re: Thunderbird > IMAP > Gmail
.. :author: しみずかわ
.. :date: 2008-01-25 10:13:35
.. :email: 
.. :url: 
.. :body:
.. やはり先駆者がいましたか。そんな気はしてたんです（笑
.. 
.. >で、Thunderbird からメールを IMAP のメールフォルダに移動させて Gmail で吸い上げました。
.. 
.. それは思いつかなかった！
.. WZ掲示板もそれで移行できるなあ...
.. 
.. 
.. :comments:
.. :comment id: 2008-01-31.9823448837
.. :title: Re: Thunderbird > IMAP > Gmail 
.. :author: M.Shibata
.. :date: 2008-01-31 19:39:43
.. :email: mshibata@emptypage.jp
.. :url: 
.. :body:
.. 今日気づいたのですが、いつの間にか日本語版の Gmail も IMAP 設定できるようになってますね。
.. いまなら直接 Gmail にドロップできるかもしれません。
.. WZ BBS のログはそのままにしてますが、取り込めたら面白いですね。ヘッダの独自部分をうまく扱ってやるだけでいけそうですが……。
.. # 下の「確認」ボタンって動いてる？
.. 
.. :comments:
.. :comment id: 2008-01-31.7016972443
.. :title: Re:確認ボタン
.. :author: taka
.. :date: 2008-01-31 23:45:01
.. :email: 
.. :url: 
.. :body:
.. 動いていませんでした。なおしました。
.. 

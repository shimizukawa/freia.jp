:date: 2009-09-22 00:08:08
:categories: ['Event', 'food', 'python']
:body type: text/x-rst

=======================================================================================
2009/09/22 PILで画像をタイル表示しEXIFの日本語タイトルを埋め込む by 串かつ専門店 でめ金
=======================================================================================

*Category: 'Event', 'food', 'python'*

色々詰め込んだら意味が分からないタイトルになりましたが、 http://atnd.org/events/1468 の 唐揚げの会 #1 に参加して、串かつを山のように食べてきたのですが、それをそのままBlogに載せてもつまらないので、そのときの写真をタイル状に並べて1枚の画像にしつつ、各画像のEXIFのタイトルに設定してある日本語文字列を各画像に埋め込む、というPythonスクリプトをビールを飲みながら書いてみようというエントリです。

用意するもの

* ビール（ウルケル、セントセバスチャンダーク、ベルビュークリーク）
* `串かつ専門店 でめ金`_ の写真多数
* でめ金のご予算 7500円くらい
* Python 2.4以降
* PIL (Python Imaging Library) 1.6
* TrueType Font (IPA-Fontとか,MSゴシックとか)
* EXIFの読み出し方の参考: `Reading out EXIF data via Python`_
* PILで日本語文字列をprintする参考: `PILでTrueType日本語フォントを使う`_
* ImagePack.py (以下のコード)


.. code-block:: python

    import os,sys,math
    from PIL import Image, ImageDraw, ImageFont
    font = ImageFont.truetype('c:/windows/fonts/msmincho.ttf', 11)

    WIDTH = 640
    HEIGHT = 480

    def imaged_text(text, fontfile, fontsize, color, bgcolor=None, scale_bias=4):
        font = ImageFont.truetype(fontfile, fontsize * scale_bias)
        image = Image.new('RGBA', (1, 1))
        draw = ImageDraw.Draw(image)
        w,h = draw.textsize(text, font=font)
        del draw
        kw = {}
        if bgcolor:
            kw['color'] = bgcolor
        image = Image.new('RGBA', (w, h), **kw)
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), text, font=font, fill=color)
        del draw
        return image.resize((w / scale_bias, h / scale_bias), Image.ANTIALIAS)

    def draw_text_to(target, position, text, fontfile, fontsize, color, bgcolor):
        image = imaged_text(text, fontfile, fontsize, color, bgcolor)
        target.paste(image , position, image)

    def guess_charset(data):
        f = lambda d, enc: d.decode(enc) and enc

        try: return f(data, 'utf-8')
        except: pass
        try: return f(data, 'shift-jis')
        except: pass
        try: return f(data, 'euc-jp')
        except: pass
        try: return f(data, 'iso2022-jp')
        except: pass
        return None

    def safe_decode(data):
        charset = guess_charset(data)
        if charset:
            return data.decode(charset,'replace')
        return data

    def get_files(target_path):
        files = os.listdir(target_path)
        filtered_files = []
        for f in files:
            try:
                img = Image.open(os.path.join(target_path, f))
                del img
                filtered_files.append(f)
            except:
                pass
        return filtered_files


    def main(target_path='.', width=640, cols=5):
        files = get_files(target_path)
        rows = int(math.ceil(1.0 * len(files) / cols))
        height = int(math.ceil((1.0 * HEIGHT / WIDTH) * width / cols * rows))
        w = width / cols # unit
        h = height / rows # unit
        x, y = 0, 0 # paste coord
        print '%dx%d (%d,%d)' % (width,height,cols,rows)
        canvas = Image.new('RGB',(width, height))
        for f in files:
            fpath = os.path.join(target_path, f)
            img = Image.open(fpath)
            r = img.size[0] / w # scale rate
            rh = img.size[1] / r # resize height
            img2 = img.resize((w,rh))

            # draw text
            exif = img._getexif()
            text = ''
            if exif:
                text = exif.get(270, f) # EXIF title
            if not text:
                text = f # filename
            text = safe_decode(text)
            draw_text_to(img2, (5, 5), text, 'msgothic.ttc', 10, '#FFF', (0,0,0))
            # paste to canvas
            canvas.paste(img2, (w*x,h*y))

            #print f, x, y, w*x, h*y
            #sys.stdout.write('.')

            x += 1
            if (x/cols) >= 1:
                x = 0
                y += 1

        print ''
        #canvas.show()
        canvas.save('packed.jpg', 'JPEG')


    if __name__ == '__main__':
        if len(sys.argv) >= 2:
            path = sys.argv[1]
        else:
            path = os.getcwd()

        if len(sys.argv) >= 3:
            width = int(sys.argv[2])
        else:
            width = 640

        if len(sys.argv) >= 4:
            cols = int(sys.argv[3])
        else:
            cols = 5

        main(path, width, cols)


ビール飲みながら書いたので、動きゃいいや的なコードになってます。いちおう途中までは色々できるようには作ってたんですが...動くかどうかは知らない。いちおう仕様はこんなかんじ。

:画像収集対象Dir: カレントDir or 第一引数のパス
:対象となるファイルの種類: Image.openで開けるやつ
:保存ファイル名: カレントのpacked.jpg固定
:出力する画像の幅: 640 or 第二引数
:横の列数: 5 or 第三引数
:実行例: python ImagePack.py photos 640 7


というわけで、 `唐揚げの会 #1`_ に参加した皆さん、途中合流したV嫁様、お疲れ様でした。


.. _`唐揚げの会 #1`: http://atnd.org/events/1468
.. _`串かつ専門店 でめ金`: http://r.gnavi.co.jp/p583000/
.. _`Reading out EXIF data via Python`: http://wolfram.kriesing.de/blog/index.php/2006/reading-out-exif-data-via-python
.. _`PILでTrueType日本語フォントを使う`: http://d.hatena.ne.jp/tanakahisateru/20081008/1223450159


.. :extend type: text/html
.. :extend:

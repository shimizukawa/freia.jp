:date: 2009-02-04 01:06:19
:categories: ['Programming', 'ruby-on-rails']
:body type: text/x-rst

=========================================
2009/02/04 RailsとCSVとストリーミングと。
=========================================

*Category: 'Programming', 'ruby-on-rails'*

とある処理のためにRailsアプリにCSVを食わせたり、CSVを出力したりという事をしました。で、このCSVというやつがけっこうデカイので、余計なDISKとかメモリとかを食わなくて良いように、ストリーミング入力、ストリーミング出力できるように実装してみました。

ストリーミング出力
-----------------

ストリーミング出力するための仕組みはRailsに備わっていて（少なくとも2.1には）、 ``render :text`` で実現できるようになっています。

log_controller:

.. code-block:: ruby

    render :text => proc { |response, out|
      column_names = ['date','hour','url','status','agent']
      CSV.generate_row(column_names, column_names.size, out)

      AccessLog.query(date) do |row|
        data = column_names.collect{|name| row[name.to_sym]}
        CSV.generate_row(data, data.size, out)
      end
    }

要は、renderの:textにはprocを渡せるようになってるので、procを渡せば実際にデータを送る段階でprocを実行してくれるので、その中でoutストリームに書き込んでいけばストリーミングが出来るようになっているわけです。（素のmongrelではこれは動きませんが、動くようにも出来ます。それはまた別の機会に...）


ストリーミング入力？
-------------------

次に、調子に乗ってCSVファイルのアップロードをストリーミングで処理しようと思い、次のようなコードを書いてみました。

log_controller:

.. code-block:: ruby

    upload_io = params[:file_data]
    CSV.parse(upload_io) do |row|
      r = AccessLog.new
      r.date = row[0]
      r.hour = row[1]
      ...
      r.save
    end

これがうまく動きません。CSV.parseのリファレンスには、第一引数に ``str_or_readable`` を受け取ると書いてあって、上記のupload_ioはStringIOなので受け取ってくれそうなのに、StringIOをStringに変換しようとして失敗したとか言って落ちやがります（Rubyは1.8.6です）。

調べてみると、CSV#parseの実装が以下のようになっていて、互換性のために第一引数が実ファイルへのパスが渡ってくることを想定している処理が入っていました（最初の5行）。

ruby/1.8/csv.rb:

.. code-block:: ruby

  def CSV.parse(str_or_readable, fs = nil, rs = nil, &block)
    if File.exist?(str_or_readable)
      STDERR.puts("CSV.parse(filename) is deprecated." +
        "  Use CSV.open(filename, 'r') instead.")
      return open_reader(str_or_readable, 'r', fs, rs, &block)
    end
    if block
      CSV::Reader.parse(str_or_readable, fs, rs) do |row|
        yield(row)
      end
      nil
    else
      CSV::Reader.create(str_or_readable, fs, rs).collect { |row| row }
    end
  end

今回はそんな想定は要らないので、CSV.parseを使う代わりに、CSV::Reader.parseを呼び出すようにしたらうまく動作するようになりました。

log_controller:

.. code-block:: ruby

    upload_io = params[:file_data]
    CSV::Reader.parse(upload_io) do |row|
      r = AccessLog.new
      r.date = row[0]
      r.hour = row[1]
      ...
      r.save
    end


動くようにはなりましたが、upload_ioはStringIOのインスタンスだったので、それってストリーミング受信してる訳では無いような気がします。全部readしてしまうよりはメモリ効率は良さそうだけど...。非mongrelならsocketが渡されて来たり.....はしないですね。複数ファイルuploadを考慮できなくなっちゃうし。残念。



.. :extend type: text/html
.. :extend:

:date: 2009-12-16 23:55:00
:categories: ['ruby-on-rails']
:body type: text/x-rst

======================================================
2009/12/16 Rails + SQLServer で data型を扱うとハマる話
======================================================

*Category: 'ruby-on-rails'*

はまります。

Rails + SQLServer で data型を使おうとすると、とってもはまります。

あ、 Ruby on Rails 2.2.2 + sqlserever_adapter-1.0.0 での話です。

まず、DBを以下のように用意するわけですよ::

  create_table "contacts" do |t|
    t.string   :name
    t.date     :birthday
    t.timestamps
  end

で、フォームを用意するわけですよ::

  <%= f.text_field :name %>
  <%= f.date_select :birthday, :use_month_numbers => true %>

それを以下のようなコントローラで受けて処理するわけですよ::

  contact = Contact.new
  contact.attributes = params[:contact]

ところが、このフォームで実際に 1950/12/25 と言う日付をPOSTするとエラーになるわけですよ。

原因は、上記で作られる select box は年・月・日の３つのセレクトボックスとして表示されて、POSTすると ``{'birthday(1i)'=>'1950', 'birthday(2i)'=>'12', 'birthday(3i)'=>'25',..`` というようなデータがサーバーに送られるわけですが、 contact.attributes = params[:contact] としている箇所で Rails が色々やってくれようとして、そこで SQLServer では Date 型が無いために、一見原因が分からないややこしいエラーが発生します。

ということで、コードを追いかけてみました。

SQLServer用の sqlserver_adapter を使うと、dateを使う！ってdb/migrationsに書いても、DBに用意される型は datetime になります。型の対応は以下のような感じです::

    class SQLServerAdapter < AbstractAdapter

      def native_database_types
        {
          :primary_key => "int NOT NULL IDENTITY(1, 1) PRIMARY KEY",
          :string      => { :name => "varchar", :limit => 255  },
          :text        => { :name => "text" },
          :integer     => { :name => "int" },
          :float       => { :name => "float", :limit => 8 },
          :decimal     => { :name => "decimal" },
          :datetime    => { :name => "datetime" },
          :timestamp   => { :name => "datetime" },
          :time        => { :name => "datetime" },
          :date        => { :name => "datetime" },
          :binary      => { :name => "image"},
          :boolean     => { :name => "bit"}
        }
      end

で、ActiveRecordの仕組みによって、DBの型から自動的にRails内でのデータ型が以下のように決まります::

  module ActiveRecord
    module ConnectionAdapters #:nodoc:
      class Column
        def klass
          case type
            when :integer       then Fixnum
            when :float         then Float
            when :decimal       then BigDecimal
            when :datetime      then Time
            when :date          then Date
            when :timestamp     then Time
            when :time          then Time
            when :text, :string then String
            when :binary        then String
            when :boolean       then Object
          end
        end

そうすると、Date型のつもりの値がdatetimeを経由して結果としてTime型で扱われてしまうという問題が発生します（多分sqlserver_adapter の問題）。

このため、1970年より前の年数を扱いたいからDate型を指定したはずなのに、実際はRails内部のデータ型がTime型なので、1950年でPOSTするとTime型で扱える範囲を超えていて、エラーになります。

エラー起こしてる直接のコードの箇所は ActiveRecord::Base#execute_callstack_for_multiparameter_attributes でした。

この問題を回避するため、色々調べたら `こういう手`_ は見つけたんですが、リリース直前なので今回は避けて、結局データをstringで持つことにしてContactモデルに以下の実装を加えてごまかしました::

  class DateColumn
    def self.klass
      Date
    end
  end

  class Contact < ActiveRecord::Base

    def column_for_attribute(name)
      if name.to_s == 'birthday1'
        ::DateColumn
      else
        self.class.columns_hash[name.to_s]
      end
    end
  
    attr_accessor :birthday1
    def birthday1= value
      @birthday1 = value
      self.birthday = value.strftime('%Y/%m/%d') if value
    end
    def birthday1
      Date.new(*self.birthday.split('/').collect{|n|n.to_i}) rescue @birthday1
    end
  end

もっと良い手をご存じの方はご連絡下さい！＞＜


.. _`こういう手`: http://mspeight.blogspot.com/2007/12/solved-rails-mssql-dates-prior-to-1970.html

.. :extend type: text/x-rst
.. :extend:


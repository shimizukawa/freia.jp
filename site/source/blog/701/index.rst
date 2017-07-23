:date: 2009-12-15 23:55:00
:tags: ruby-on-rails

===========================
Rubyでメール送信
===========================

現在、12/15 27:05 です。忙しさのピークを迎えていますが、RailsのActionMailerでハマっています。SMTPサーバーの問題なのか、設定の問題なのか、Railsの問題なのかを切り分けるために、Rubyで直接SMTPを叩いてみました。

irbで対話形式でこんな感じにメールを送信します。

::

  irb(main):008:0> require 'net/smtp'
  true
  irb(main):009:0> smtp = Net::SMTP.new('127.0.0.1', 25)
  => #<Net::SMTP 127.0.0.1:25 started=false>
  irb(main):010:0> smtp.start()
  => #<Net::SMTP 127.0.0.1:25 started=true>
  irb(main):012:0> smtp.sendmail(
  irb(main):013:1*   "To: shimizukawa@example.com\r\n\r\nTestTestTest",
  irb(main):014:1*   'noreply@example.com', ['shimizukawa@example.com'])
  => #<Net::SMTP::Response:0x2da23dc @string="250 2.0.0 nBFHk4B3023515 Message accepted for delivery\n", @status="250">

ちょっと読みづらいですが、最終行で送信が成功しているのが分かります。

Railsではうまくいかないのに、Ruby直だとちゃんと動くという...。じゃあ次はsmtp.start()に色々パラメータを与えてみるかな。



.. :extend type: text/x-rst
.. :extend:



.. :comments:
.. :comment id: 2009-12-16.5854118613
.. :title: Re:Rubyでメール送信
.. :author: しみずかわ
.. :date: 2009-12-16 23:43:06
.. :email: 
.. :url: 
.. :body:
.. 最終的には送信出来るようになりました。start()の:domainオプションがHELOコマンドに渡っているんですが、これがSMTPサーバー側の設定と合っていないとだめだったたけでした。
.. 
.. が、今度は別の問題が。initializers に以下の内容を書くと、手元の環境ではうまくいくのに本番環境では送信出来ないという...。どっちもWindowsなんだけどな。
.. 
.. config = Rails.configuration
.. config.action_mailer.delivery_method = :smtp
.. config.action_mailer.smtp_settings = {
..   :address => 'smtp.example.com',
..   :port => 25,
..   :domain => 'example.com',
.. }
.. 
.. ‥‥ RAILS_ENVがdevelopmentとproductionという違いがあるけど、関係あるかな？

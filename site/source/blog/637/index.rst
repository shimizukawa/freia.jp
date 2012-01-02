:date: 2009-05-27 06:59:11
:categories: ['python']
:body type: text/x-rst

=======================================================
Re: pythonで毎回使いたいloggingモジュールのテンプレート
=======================================================

`pythonで毎回使いたいloggingモジュールのテンプレート - a2c.get.diary`_ への時間差反応です。2ヶ月差？
自分が普段使っているloggingのテンプレを貼っておきます。複数のloggerオブジェクトを作れるとか色々やった痕跡があったりして、元記事よりもコードがでかいなぁ...。

.. code-block:: python
  import sys, logging
  logger = logging.getLogger('foologger')
  
  def setup_logger(opts):
      # setup output
      if opts.log:
          hdlr = logging.FileHandler(opts.log, 'a')
      else:
          hdlr = logging.StreamHandler(sys.stdout)
      formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
      hdlr.setFormatter(formatter)
      logger.addHandler(hdlr)
      if opts.debug:
          logger.setLevel(logging.DEBUG)
      else:
          logger.setLevel(logging.INFO)
  
      # setup error output
      hdlr = logging.StreamHandler()
      hdlr.setLevel(logging.ERROR)
      hdlr.setFormatter(formatter)
      logger.addHandler(hdlr)
  
  
  def setup_optparser():
      from optparse import OptionParser, OptionGroup
      usage = 'usage: %prog [options] command'
      parser = OptionParser(usage=usage)
      parser.add_option('-l', '--log',
                        dest='log',
                        default='',
                        help="Filename for log output",
                        )
      parser.add_option('-d', '--debug',
                        dest='debug',
                        action='store_true',
                        default=False,
                        help="Enable debug output",
                        )
      group = OptionGroup(parser, "command",
                          "something else..."
                          )
      parser.add_option_group(group)
      return parser
  
  
  if __name__ == '__main__':
      parser = setup_optparser()
      options, args = parser.parse_args(sys.argv)
      setup_logger(options)
  
      if len(args)<2:
          parser.print_help()
          sys.exit(1)
  
      # do something...


.. _`pythonで毎回使いたいloggingモジュールのテンプレート - a2c.get.diary`: http://d.hatena.ne.jp/a2c/20090305/1236241477


.. :extend type: text/html
.. :extend:

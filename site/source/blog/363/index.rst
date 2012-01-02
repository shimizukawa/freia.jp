:date: 2006-08-25 01:29:45
:categories: ['Programming']
:body type: text/x-rst

=============================================
2006/08/25 Re: 私は、こんな悲惨なコードを見た
=============================================

.. epigraph::

  「私は、こんな悲惨なコードを見た」という証言を募集！

  -- `So-net blog:ある nakagami の日記:Java と Oracle って偉いなー、つうか可哀想だなぁ`_


.. _`So-net blog:ある nakagami の日記:Java と Oracle って偉いなー、つうか可哀想だなぁ`: http://blog.so-net.ne.jp/nakagami/2006-08-24

私は見ました。それはある長いプロジェクトの半ばにさしかかった頃でした……。（略）

.. code-block:: cpp

  BOOL IsApplet(CONTEXT* context, BOOL *bFlag)
  {
    ...
    if (bResult==TRUE)
    {
      *bFlag = (hogehoge==fugafuga)? TRUE: FALSE;
    }
    return bResult;
  }


返値はTRUEかFALSEなんですが、TRUEの時には第二引数bFlagにTRUEかFALSEが格納されて返ってくる。つまり3つの状態を返す可能性があったわけです。全然Isじゃない。そう言えば、これが発見されたのは、第三引数にさらに別の値を返そうとしている所を目撃した時だったような気が……。

今はもう、C言語のような難しい言語に触ることはほとんどない生活なので、幸せな毎日を送っています。（実際問題、言語は関係ないんだよね……。）


.. :extend type: text/html
.. :extend:

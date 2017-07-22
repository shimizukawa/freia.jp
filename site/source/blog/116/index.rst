:date: 2005-01-20 01:34:25
:categories: ['WZ', 'python']
:body type: text/x-rst

=============================================
2005/01/20 WZマクロからPythonコードを実行する
=============================================

`WZ Editor`_ のマクロから Python_ コードを実行するためのDLLを作ってみた。

WZマクロの例::

	int main(TX* text)
	{
		printf( "1: %d\n", fnPygw("pywz","func1","teststrings") );
		printf( "2: %d\n", fnPygw("pywz","func2","teststrings") );
	
		char* code = "reduce(lambda x,y:x+y,[x for x in range(0,10)])";
		printf( "3: %d\n", fnPygw("pywz","func3", code) );
	
		return 0;
	}

呼び出されるPythonコードの例::

	func1 = lambda x: len(x)
	func2 = lambda x: 15
	def func3(x):
		return eval(x)

実行結果::

	1: 11
	2: 15
	3: 45

実行結果が説得力に欠けるな‥‥。

WZマクロ側から指定できるのは今のところ *呼び出すPythonモジュール名* , *モジュールの関数名* , *引数となる文字列* だけで、返値はint決め打ちだから、あんまり複雑なことはできない。でも可能性はあるかも。

file: `pygw20050119.lzh`_

.. _`WZ Editor`: http://www.villagecenter.co.jp/soft/wz50/
.. _Python: http://python.jp/
.. _`pygw20050119.lzh`: file/wz/pygw20050119.lzh



.. :extend type: text/plain
.. :extend:


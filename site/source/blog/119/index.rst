:date: 2005-01-22 01:43:18
:tags: WZ, python
:body type: text/x-rst

===============================================
2005/01/22 WZマクロからPythonコードを実行する２
===============================================

先日作った pygw [1]_ を拡張して、 Python_ のprint文出力先をWZの任意の関数に接続できるようにしてみた。

WZマクロの例::

	#include <windows.h>
	#include "pygw.h"
	
	static FARPROC PrinfRegCode; //RegCode
	
	void CALLBACK Print(char* str)
	{
		printf(str);
	}
	
	int main(TX* text)
	{
		PrinfRegCode = txpcodeRegisterCallback( Print, 1 );
		PYGW_SetStdout( PrinfRegCode );
	
		PYGW_Pygw("pywz","func1","teststrings");
		PYGW_Pygw("pywz","func2","teststrings");
		PYGW_Pygw("pywz","func3","reduce(lambda x,y:x+y,[x for x in range(0,10)])");
		PYGW_Pygw("pywz","func4","Hello");
	
		txpcodeUnregisterCallback( PrinfRegCode );
		PrinfRegCode = NULL;
		return 0;
	}

呼び出されるPythonコードの例::

	import stdout
	
	def func1(x):
		print "1: ", len(x)
		return len(x)
	
	def func2(x):
		print "2: ", x
		return 0
	
	def func3(x):
		print "3: ", x, " ==> ", eval(x)
		return eval(x)
	
	def func4(x):
		print "4: ", [s for s in x]
		return len(x)

実行結果::

	1:  11
	2:  teststrings
	3:  reduce(lambda x,y:x+y,[x for x in range(0,10)])  ==>  45
	4:  ['H', 'e', 'l', 'l', 'o']

実行結果はもちろんWZのSTDOUTに出力される。以下が証拠画像だ！（ねつ造じゃないよ？）

|pygw_wz1|


file: `pygw20050121.lzh`_

.. [1] `WZ Editor`_ のマクロから Python_ コードを実行するためのDLL
.. _`WZ Editor`: http://www.villagecenter.co.jp/soft/wz50/
.. _Python: http://python.jp/
.. _`pygw20050121.lzh`: file/wz/pygw20050121.lzh
.. |pygw_wz1| image:: pygw_wz1



.. :extend type: text/plain
.. :extend:


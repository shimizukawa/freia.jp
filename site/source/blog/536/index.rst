:date: 2008-02-06 03:08:17
:categories: ['work', 'cpp']
:body type: text/x-rst

========================================================
2008/02/06 C++のtemplateでBREW用にshared_ptrを書いてみた
========================================================

*Category: 'work', 'cpp'*

追記： **修正版があります！** http://www.freia.jp/taka/blog/594%%%%%%%%%-----

とりあえずVC++ではビルドできるけど、実機で問題なく使えるかどうかは不明。ARMコンパイラがちゃんとビルドしてくれれば動くかもしれない。夜中に寝ながら書いたので動作保証ありません、と言ったら職場で採用が見送られました。そんなコードですが、誰か使ってみてうまくいったら教えてください。次のプロジェクトで使ってみます。

いや、冗談ですが、半分本気です。なんて言うか、このへん動作保証できるBREWアプリ開発者が日本に何人いるのか非常に怪しい、と思うくらいにBREW開発って罠が多い気がする。

コード中では operators.h をインクルードしてるけど、これはソフィアあたりから取得してください。operator new 系をBREWのMALLOCで実装してるやつです。

以下、コード。


.. :extend type: text/x-rst
.. :extend:
.. code-block:: cpp

    #ifndef __BREW_SHARED_PTR_H__
    #define __BREW_SHARED_PTR_H__
    #include ".\operators.h"
    
    class shared_counter {
    private:
    	int count;
    public:
    	shared_counter():count(1){}
    	~shared_counter(){}
    
    	int inc() {return ++count;}
    	int dec() {return --count;}
    };
    
    template<class T>
    class shared_ptr {
    private:
    	T* px;
    	shared_counter* pn;
    
    public:
    	shared_ptr()
    		:px(0),pn(0)
    	{}
    
    	template<class T>
    	shared_ptr(T* p)
    		:px(p),pn(0)
    	{
    		pn = new shared_counter()
    	}
    
    	template<class T>
    	shared_ptr(shared_ptr<T> r)
    		:px(r.px),pn(r.pn)
    	{
    		pn->inc();
    	}
    
    	~shared_ptr()
    	{
    		if(pn && pn->dec()==0)
    		{
    			delete pn;
    			delete px;
    		}
    	}
    
    	template<class T>
    	shared_ptr& operator=(T* const p)
    	{
    		if(pn && pn->dec()==0)
    		{
    			delete pn;
    			delete px;
    		}
    		px = p;
    		pn = new shared_counter();
    		return *this;
    	}
    
    	template<class T>
    	shared_ptr& operator=(shared_ptr<T> const & r)
    	{
    		px = r.px;
    		pn = r.pn;
    		pn->inc();
    		return *this;
    	}
    
    	T& operator*() const
    	{
    		return *px;
    	}
    
    	T* operator->() const
    	{
    		return px;
    	}
    
    	operator T*() const
    	{
    		return px;
    	}
    };
    
    
    #endif // __BREW_SHARED_PTR_H__


.. :comments:
.. :comment id: 2008-06-29.4793257296
.. :title: あらかじめ言い訳を書いておく
.. :author: しみずかわ
.. :date: 2008-06-29 00:30:24
.. :email: 
.. :url: 
.. :body:
.. 西尾さんのblog http://d.hatena.ne.jp/nishiohirokazu/20080628 からリンクされてしまったので、あらかじめ言い訳を書いておく。
.. 
.. ・バグがあってもいじめないでね。
.. ・shared_ptrは参照カウントよりリンクリストのほうが効率いい (thanks とやま)
.. ・リンクリストにすればshared_counterいらないよね
.. 
.. 
.. :comments:
.. :comment id: 2008-06-29.8331508502
.. :title: やっぱりバグがあった
.. :author: しみずかわ
.. :date: 2008-06-29 02:57:13
.. :email: 
.. :url: 
.. :body:
.. ・代入演算子で自分を解放していない！
.. ・自己代入で変なことになる！
.. 

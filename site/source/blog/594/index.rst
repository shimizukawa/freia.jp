:date: 2008-07-04 01:14:55
:tags: cpp
:body type: text/x-rst

==============================================================
2008/07/04 C++のtemplateでBREW用にshared_ptrを書いてみた（改）
==============================================================

`Python温泉3, 2日目深夜, shared_ptr大会`_ を経て、いくつかのバグが見つかったので、BREW用に作ったshared_ptrを修正してみる。修正にあたり、とやまに意見をもらったりした。ありがとう。実際問題、C++現役から離れて久しいのできっとまだバグがあるに違いない...。でも晒しておこう。

以下の点に注意。

- 簡単なテストしかしてません。流用は自己責任で。。
- 結局BREW用に書いたものの採用しませんでした（開発後期だったため）
- カウンタはLinkListで作った方が良いと思われる
- 大本のコードはboostのshared_ptrです
- `前作`_ から、shared_ptr同士の代入と、自己代入のバグを修正

ということで、以下コード。


.. _`Python温泉3, 2日目深夜, shared_ptr大会`: http://www.freia.jp/taka/blog/589
.. _`前作`: http://www.freia.jp/taka/blog/536/edit

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
    
    	template<class Y>
    	shared_ptr(Y* p)
    		:px(p),pn(0)
    	{
    		pn = new shared_counter()
    	}
    
    	template<class Y>
    	shared_ptr(shared_ptr<Y> r)
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
    
        shared_ptr & operator=(shared_ptr const & r)
        {
            if(*this == r) return *this;
            if(pn && pn->dec()==0)
            {
                    delete pn;
                    delete px;
            }
            px = r.px;
            pn = r.pn;
            pn->inc();
            return *this;
        }

        template<class Y>
        shared_ptr & operator=(shared_ptr<Y> const & r)
        {
            if(*this == r) return *this;
            if(pn && pn->dec()==0)
            {
                delete pn;
                delete px;
            }
            px = r.px;
            pn = r.pn;
            pn->inc();
            return *this;
        }

        template<class Y>
        shared_ptr& operator=(Y* const p)
        {
            if(px == p) return *this;
            if(pn && pn->dec()==0)
            {
                delete pn;
                delete px;
            }
            px = p;
            pn = new shared_counter();
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

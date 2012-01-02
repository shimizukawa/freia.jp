:date: 2008-01-24 00:18:23
:categories: ['vim']
:body type: text/x-rst

================================
2008/01/24 vim(gvim)の設定を晒す
================================

*Category: 'vim'*

まだ設定周りはよくわかってませんが、とりあえず晒します。ほとんどあちこちのサイトで公開されていたもののコピペです。

まずは参考にしたサイトから。

- `.vimrc - Twisted Mind`_
- `gVim覚書`_
- `名無しのvim使い`_
- `vimを使っている方は、便利に使うためにどんなテクニックがありますか？ あるいはvimスクリプトがあったら教えてください。 現在使っているのは easy (un)commenting out o.. - 人力検索はてな`_
- `OZACC.blog: Vista ファイルの関連付け`_

設定が落ち着いたら、 `Vimpi`_ に登録してプロフィールと一緒にvimrcを晒すことにしよう。


.. _`Vimpi`: http://vimpi.net/user/dubhead
.. _`.vimrc - Twisted Mind`: http://d.hatena.ne.jp/Voluntas/20070427/1177695694
.. _`gVim覚書`: http://www002.upp.so-net.ne.jp/janus/vim.html
.. _`名無しのvim使い`: http://nanasi.jp/
.. _`vimを使っている方は、便利に使うためにどんなテクニックがありますか？ あるいはvimスクリプトがあったら教えてください。 現在使っているのは easy (un)commenting out o.. - 人力検索はてな`: http://q.hatena.ne.jp/1137486621
.. _`OZACC.blog: Vista ファイルの関連付け`: http://blog.ozacc.com/archives/001741.html



.. :extend type: text/x-rst
.. :extend:

::

	colorscheme darkblue
	set guioptions-=T
	
	" Source other vim command
	"if has('mac')
	"    source $VIMRUNTIME/delmenu.vim
	"	set langmenu=ja_jp.utf-8
	"	source $VIMRUNTIME/menu.vim
	"	set antialias
	"	set macatsui
	"	set termencoding=japan
	"	set guifont=Osaka-Mono:h15
	"endif
	if has("gui_win32")
		if $TERM == ""
			set shell=$BASHPATH\ --login
		else
			set shell=$BASHPATH
		endif
		set shellslash
	
		" Add .vim directory to runtimepath
		set runtimepath+=$HOME\.vim
	
		" Windows setting for Access permissions
		set backupcopy=yes
		set nobackup
	endif
	if has('kaoriya')
	  highlight CursorIM guibg=Purple guifg=NONE
	  inoremap <silent> <ESC> <ESC>:set iminsert=0<CR>
	  set iminsert=0 imsearch=0
	endif
	
	highlight SpecialKey cterm=underline ctermfg=darkgrey
	highlight ZenkakuSpace cterm=underline ctermfg=lightblue guibg=white
	match ZenkakuSpace /　/
	
	set transparency=220
	
	".vimrc
	
	
	" Common options
	syntax on
	"set nobk
	set grepprg=search\ $*
	set iminsert=0
	set imsearch=0
	set listchars=eol:$,tab:>-
	set ruler
	set shortmess+=I
	set visualbell
	set scrolloff=2
	
	set fileformats=unix,dos,mac " 改行コードの自動認識
	"set showcmd
	"set number
	set nocompatible
	set clipboard+=unnamed
	set wildmode=list:longest
	set autoread
	set showmode
	set hidden
	set noinsertmode
	set showmode
	set cmdheight=1
	set nowrap
	"set wrap
	set laststatus=2
	"set cmdheight=2
	set showcmd
	set title
	set statusline=%<%f\ %m%r%h%w%{'['.(&fenc!=''?&fenc:&enc).']['.&ff.']'}%=%l,%c%V%8P
	
	if has("gui_win32")
		set guifont=ＭＳ_ゴシック:h12:cSHIFTJIS
		set printfont=ＭＳ_ゴシック:h10:cSHIFTJIS
		" autocmd GUIEnter * simalt ~x
		" autocmd GUIEnter * winpos 100 0
		autocmd GUIEnter * winsize 80 52
	else
		au BufNewFile,BufRead fstab setf fstab
		if has("gui_running")
			if $LANG == "ja_JP.utf-8"
				inoremap   :set iminsert=0
				if $HOSTNAME == "vaio"
					" set guifontset=-alias-fixed-medium-r-normal-*-*-160-*-*-c-*-jisx0201.1976-0
					set printfont=-alias-fixed-medium-r-normal-*-*-160-*-*-c-*-jisx0201.1976-0
					set guifont=gothic\ Medium\ 14
				else
					set guifontset=-alias-fixed-medium-r-normal-*-*-160-*-*-c-*-jisx0201.1976-0
					set printfont=-alias-fixed-medium-r-normal-*-*-160-*-*-c-*-jisx0201.1976-0
				endif
				set imactivatekey=S-space
			endif
			autocmd GUIEnter * winsize 80 45 
		else
			set mouse=a
		endif
	endif
	
	"tab
	set tabstop=4
	set shiftwidth=4
	set smarttab
	set expandtab
	set softtabstop=4
	set autoindent
	
	"edit
	set smartindent
	set showmatch
	set backspace=indent,eol,start
	set nolist
	
	" search
	set ignorecase
	set smartcase
	"set hlsearch
	set nohlsearch
	set incsearch 
	
	" backup
	set nobackup
	set nowritebackup
	set swapfile
	
	" □とか○の文字があってもカーソル位置がずれないようにする
	set ambiwidth=double
	
	"set encoding=utf8 "menu encoding...
	set fileencoding=utf8
	
	" 文字コードの自動認識
	if has('iconv')
	  let s:enc_euc = 'euc-jp'
	  let s:enc_jis = 'iso-2022-jp'
	  " iconvがeucJP-msに対応しているかをチェック
	  if iconv("\x87\x64\x87\x6a", 'cp932', 'eucjp-ms') ==# "\xad\xc5\xad\xcb"
	    let s:enc_euc = 'eucjp-ms'
	    let s:enc_jis = 'iso-2022-jp-3'
	  " iconvがJISX0213に対応しているかをチェック
	  elseif iconv("\x87\x64\x87\x6a", 'cp932', 'euc-jisx0213') ==# "\xad\xc5\xad\xcb"
	    let s:enc_euc = 'euc-jisx0213'
	    let s:enc_jis = 'iso-2022-jp-3'
	  endif
	  " fileencodingsを構築
	  if &encoding ==# 'utf-8'
	    let s:fileencodings_default = &fileencodings
	    let &fileencodings = s:enc_jis .','. s:enc_euc .',cp932'
	    let &fileencodings = &fileencodings .','. s:fileencodings_default
	    unlet s:fileencodings_default
	  else
	    let &fileencodings = &fileencodings .','. s:enc_jis
	    set fileencodings+=utf-8,ucs-2le,ucs-2
	    if &encoding =~# '^\(euc-jp\|euc-jisx0213\|eucjp-ms\)$'
	      set fileencodings+=cp932
	      set fileencodings-=euc-jp
	      set fileencodings-=euc-jisx0213
	      set fileencodings-=eucjp-ms
	      let &encoding = s:enc_euc
	      let &fileencoding = s:enc_euc
	    else
	      let &fileencodings = &fileencodings .','. s:enc_euc
	    endif
	  endif
	  " 定数を処分
	  unlet s:enc_euc
	  unlet s:enc_jis
	endif
	" 日本語を含まない場合は fileencoding に encoding を使うようにする
	if has('autocmd')
	  function! AU_ReCheck_FENC()
	    if &fileencoding =~# 'iso-2022-jp' && search("[^\x01-\x7e]", 'n') == 0
	      let &fileencoding=&encoding
	    endif
	  endfunction
	  autocmd BufReadPost * call AU_ReCheck_FENC()
	endif
	
	"taglist.vim
	set tags=tags
	
	"python.vim
	let python_highlight_all = 1
	
	"minibufexpl.vim
	"set minibfexp
	let g:miniBufExplMapWindowNavVim=1
	let g:miniBufExplSplitBelow=0
	let g:miniBufExplMapWindowNavArrows=1
	let g:miniBufExplMapCTabSwitchBufs=1
	let g:miniBufExplModSelTarget=1
	let g:miniBufExplSplitToEdge=1
	
	" minibufexpl.vim
	nmap <Space> :MBEbn<CR>
	nmap <S-Space> :MBEbp<CR>
	
	if has('mac')
	  set iskeyword=@,48-57,_,128-167,224-235
	  " SpotlightOpen
	  let g:spotlightopen_match = 2
	endif
	
	" key map
	nmap j gj
	nmap k gk
	vmap j gj
	vmap k gk
	
	" mru.vim 
	let MRU_Max_Entries = 50
	let MRU_Exclude_Files = '^/tmp/.*\|^/var/tmp/.*'
	let MRU_Window_Height = 20 
	" let MRU_Use_Current_Window = 1
	" let MRU_Auto_Close = 0


.. :comments:
.. :comment id: 2009-01-05.8239722741
.. :title: Re:vim(gvim)の設定を晒す
.. :author: 通りすがり
.. :date: 2009-01-05 15:27:05
.. :email: 
.. :url: 
.. :body:
.. " 文字コードの自動認識
.. " 日本語を含まない場合は fileencoding に encoding を使うようにする
.. のふたつをコピーして利用させてもらいました。
.. MacOS 10.5 + MacVimで問題なく動作しています。
.. 非常に便利になりました。ありがとうございました。多謝！！

:date: 2012-04-07 10:20:00
:tags: Python, Distutils2, packaging
:body type: text/x-rst

======================================================
2012/04/07 Distutils2/packagingのpysetup createが長い
======================================================

作りかけだったrst2textileを公開して欲しいという要望をもらったので、setup.py書かなきゃ。あ、それなら ``pysetup create`` でsetup.cfg作れば楽じゃね？ということでやってみた。


.. code-block:: bash

   $ pysetup create
   Project name [rst2textile]:
   Current version number [1.0.0]: 0.1.0
   Project description summary:
      > rst2textile is docutils textile writer convert reStructuredText(rst) to Textile format.
   Author name: Takayuki SHIMIZUKAWA
   Author email address: shimizukawa@gmail.com
   Project home page: https://bitbucket.org/shimizukawa/rst2textile
   Do you want me to automatically build the file list with everything I can find in the current directory? If you say no, you will have to define them manually. (y/n): y
   Do you want to set Trove classifiers? (y/n): y
               Please select the project status:

               0 - Planning
   1 - Pre-Alpha
   2 - Alpha
   3 - Beta
   4 - Production/Stable
   5 - Mature
   6 - Inactive

               Status: 3
   What license do you use?: apache
   Matching licenses:

      1) License :: OSI Approved :: Apache Software License

   Type the number of the license you wish to use or ? to try again:: 1
   What license do you use?:
   Do you want to set other trove identifiers? (y/n) [n]: y
   Do you want to set items under
      "Development Status" (7 sub-items)? (y/n)
       [n]: y
   Add "Development Status" :: 1 - Planning (y/n) [n]:
   Add "Development Status" :: 2 - Pre-Alpha (y/n) [n]:
   Add "Development Status" :: 3 - Alpha (y/n) [n]:
   Add "Development Status" :: 4 - Beta (y/n) [n]: y
   Add "Development Status" :: 5 - Production/Stable (y/n) [n]:
   Add "Development Status" :: 6 - Mature (y/n) [n]:
   Add "Development Status" :: 7 - Inactive (y/n) [n]:
   Do you want to set items under
      "Environment" (9 sub-items)? (y/n) [n]: y
   Do you want to set items under
      "Console" (4 sub-items)? (y/n) [n]: y
   Add "Environment :: Console" :: Curses (y/n) [n]:
   Add "Environment :: Console" :: Framebuffer (y/n) [n]:
   Add "Environment :: Console" :: Newt (y/n) [n]:
   Add "Environment :: Console" :: svgalib (y/n) [n]:
   Add "Environment" :: Handhelds/PDA's (y/n) [n]:
   Do you want to set items under
      "MacOS X" (3 sub-items)? (y/n) [n]:
   Add "Environment" :: No Input/Output (Daemon) (y/n) [n]:
   Add "Environment" :: Other Environment (y/n) [n]: y
   Add "Environment" :: Plugins (y/n) [n]:
   Do you want to set items under
      "Web Environment" (3 sub-items)? (y/n)
       [n]:
   Add "Environment" :: Win32 (MS Windows) (y/n) [n]:
   Do you want to set items under
      "X11 Applications" (4 sub-items)? (y/n)
       [n]:
   Do you want to set items under
      "Framework" (18 sub-items)? (y/n) [n]: n
   Do you want to set items under
      "Intended Audience" (14 sub-items)? (y/n)
       [n]:
   Do you want to set items under
      "License" (16 sub-items)? (y/n) [n]:
   Do you want to set items under
      "Natural Language" (52 sub-items)? (y/n)
       [n]:
   Do you want to set items under
      "Operating System" (10 sub-items)? (y/n)
       [n]:
   Do you want to set items under
      "Programming Language" (54 sub-items)? (y/n)
       [n]: y
   Add "Programming Language" :: APL (y/n) [n]:
   Add "Programming Language" :: ASP (y/n) [n]:
   Add "Programming Language" :: Ada (y/n) [n]:
   Add "Programming Language" :: Assembly (y/n) [n]:
   Add "Programming Language" :: Awk (y/n) [n]:
   Add "Programming Language" :: Basic (y/n) [n]:
   Add "Programming Language" :: C (y/n) [n]:
   Add "Programming Language" :: C# (y/n) [n]:
   Add "Programming Language" :: C++ (y/n) [n]:
   Add "Programming Language" :: Cold Fusion (y/n) [n]:
   Add "Programming Language" :: Cython (y/n) [n]:
   Add "Programming Language" :: Delphi/Kylix (y/n) [n]:
   Add "Programming Language" :: Dylan (y/n) [n]:
   Add "Programming Language" :: Eiffel (y/n) [n]:
   Add "Programming Language" :: Emacs-Lisp (y/n) [n]:
   Add "Programming Language" :: Erlang (y/n) [n]:
   Add "Programming Language" :: Euler (y/n) [n]:
   Add "Programming Language" :: Euphoria (y/n) [n]:
   Add "Programming Language" :: Forth (y/n) [n]:
   Add "Programming Language" :: Fortran (y/n) [n]:
   Add "Programming Language" :: Haskell (y/n) [n]:
   Add "Programming Language" :: Java (y/n) [n]:
   Add "Programming Language" :: JavaScript (y/n) [n]:
   Add "Programming Language" :: Lisp (y/n) [n]:
   Add "Programming Language" :: Logo (y/n) [n]:
   Add "Programming Language" :: ML (y/n) [n]:
   Add "Programming Language" :: Modula (y/n) [n]:
   Add "Programming Language" :: OCaml (y/n) [n]:
   Add "Programming Language" :: Object Pascal (y/n) [n]:
   Add "Programming Language" :: Objective C (y/n) [n]:
   Add "Programming Language" :: Other (y/n) [n]:
   Add "Programming Language" :: Other Scripting Engines (y/n) [n]:
   Add "Programming Language" :: PHP (y/n) [n]:
   Add "Programming Language" :: PL/SQL (y/n) [n]:
   Add "Programming Language" :: PROGRESS (y/n) [n]:
   Add "Programming Language" :: Pascal (y/n) [n]:
   Add "Programming Language" :: Perl (y/n) [n]:
   Add "Programming Language" :: Pike (y/n) [n]:
   Add "Programming Language" :: Pliant (y/n) [n]:
   Add "Programming Language" :: Prolog (y/n) [n]:
   Do you want to set items under
      "Python" (11 sub-items)? (y/n) [n]: y
   Add "Programming Language :: Python" :: 2 (y/n) [n]: y
   Add "Programming Language :: Python" :: 2.3 (y/n) [n]:
   Add "Programming Language :: Python" :: 2.4 (y/n) [n]:
   Add "Programming Language :: Python" :: 2.5 (y/n) [n]: y
   Add "Programming Language :: Python" :: 2.6 (y/n) [n]: y
   Add "Programming Language :: Python" :: 2.7 (y/n) [n]: y
   Add "Programming Language :: Python" :: 3 (y/n) [n]:
   Add "Programming Language :: Python" :: 3.0 (y/n) [n]:
   Add "Programming Language :: Python" :: 3.1 (y/n) [n]:
   Add "Programming Language :: Python" :: 3.2 (y/n) [n]:
   Do you want to set items under
      "Implementation" (5 sub-items)? (y/n)
       [n]: y
   Add "Programming Language :: Python :: Implementation" :: CPython (y/n)
       [n]: n
   Add "Programming Language :: Python :: Implementation" :: IronPython (y/n)
       [n]:
   Add "Programming Language :: Python :: Implementation" :: Jython (y/n)
       [n]:
   Add "Programming Language :: Python :: Implementation" :: PyPy (y/n) [n]:
   Add "Programming Language :: Python :: Implementation" :: Stackless (y/n)
       [n]:
   Add "Programming Language" :: REBOL (y/n) [n]:
   Add "Programming Language" :: Rexx (y/n) [n]:
   Add "Programming Language" :: Ruby (y/n) [n]:
   Add "Programming Language" :: SQL (y/n) [n]:
   Add "Programming Language" :: Scheme (y/n) [n]:
   Add "Programming Language" :: Simula (y/n) [n]:
   Add "Programming Language" :: Smalltalk (y/n) [n]:
   Add "Programming Language" :: Tcl (y/n) [n]:
   Add "Programming Language" :: Unix Shell (y/n) [n]:
   Add "Programming Language" :: Visual Basic (y/n) [n]:
   Add "Programming Language" :: XBasic (y/n) [n]:
   Add "Programming Language" :: YACC (y/n) [n]:
   Add "Programming Language" :: Zope (y/n) [n]:
   Do you want to set items under
      "Topic" (24 sub-items)? (y/n) [n]: y
   Add "Topic" :: Adaptive Technologies (y/n) [n]:
   Add "Topic" :: Artistic Software (y/n) [n]:
   Do you want to set items under
      "Communications" (11 sub-items)? (y/n)
       [n]:
   Do you want to set items under
      "Database" (2 sub-items)? (y/n) [n]:
   Do you want to set items under
      "Desktop Environment" (7 sub-items)? (y/n)
       [n]:
   Add "Topic" :: Documentation (y/n) [n]: y
   Do you want to set items under
      "Education" (2 sub-items)? (y/n) [n]:
   Do you want to set items under
      "Games/Entertainment" (11 sub-items)? (y/n)
       [n]:
   Add "Topic" :: Home Automation (y/n) [n]:
   Do you want to set items under
      "Internet" (8 sub-items)? (y/n) [n]:
   Do you want to set items under
      "Multimedia" (3 sub-items)? (y/n) [n]:
   Do you want to set items under
      "Office/Business" (5 sub-items)? (y/n)
       [n]:
   Add "Topic" :: Other/Nonlisted Topic (y/n) [n]:
   Add "Topic" :: Printing (y/n) [n]:
   Add "Topic" :: Religion (y/n) [n]:
   Do you want to set items under
      "Scientific/Engineering" (16 sub-items)? (y/n)
       [n]:
   Do you want to set items under
      "Security" (1 sub-items)? (y/n) [n]:
   Do you want to set items under
      "Sociology" (2 sub-items)? (y/n) [n]:
   Do you want to set items under
      "Software Development" (20 sub-items)? (y/n)
       [n]:
   Do you want to set items under
      "System" (21 sub-items)? (y/n) [n]:
   Do you want to set items under
      "Terminals" (3 sub-items)? (y/n) [n]:
   Do you want to set items under
      "Text Editors" (5 sub-items)? (y/n) [n]:
   Do you want to set items under
      "Text Processing" (6 sub-items)? (y/n)
       [n]: y
   Add "Topic :: Text Processing" :: Filters (y/n) [n]:
   Add "Topic :: Text Processing" :: Fonts (y/n) [n]:
   Add "Topic :: Text Processing" :: General (y/n) [n]: y
   Add "Topic :: Text Processing" :: Indexing (y/n) [n]:
   Add "Topic :: Text Processing" :: Linguistic (y/n) [n]:
   Do you want to set items under
      "Markup" (5 sub-items)? (y/n) [n]: y
   Add "Topic :: Text Processing :: Markup" :: HTML (y/n) [n]:
   Add "Topic :: Text Processing :: Markup" :: LaTeX (y/n) [n]:
   Add "Topic :: Text Processing :: Markup" :: SGML (y/n) [n]:
   Add "Topic :: Text Processing :: Markup" :: VRML (y/n) [n]:
   Add "Topic :: Text Processing :: Markup" :: XML (y/n) [n]:
   Add "Topic" :: Utilities (y/n) [n]: y
   Wrote "setup.cfg".


長い。とっても長い。Trove classifiersは手動で設定した方が良いかもしれない。けど、色々気づかなかったclassifierがあるのに気づけたのは収穫だなー。

こうして生成されたsetup.cfgは以下の通り。

.. code-block:: ini


   [metadata]
   name = rst2textile
   version = 0.1.0
   summary = rst2textile is docutils textile writer convert reStructuredText(rst) to Textile format.
   download_url = UNKNOWN
   home_page = https://bitbucket.org/shimizukawa/rst2textile
   author = Takayuki SHIMIZUKAWA
   author_email = shimizukawa@gmail.com
   classifier = Development Status :: 3 - Alpha
       Topic :: Utilities
       Environment :: Other Environment
       License :: OSI Approved :: Apache Software License
       Development Status :: 4 - Beta
       Topic :: Documentation
       Topic :: Text Processing :: General
       Programming Language :: Python :: 2
       Programming Language :: Python :: 2.6
       Programming Language :: Python :: 2.7
       Programming Language :: Python :: 2.5

   [files]
   modules = rst2textile
   extra_files = sample.rst
       sample.txt
       text.txt


なぜか `Development Status` が2回出てきてる。Classifire指定でも聞かれたからだと思う。1回目の方はBeta指定したはずなのにAlphaになってる。これは多分バグだなー。

上記も含め、Distutils2/packagingで気がついた問題点。

* 対話形式でsetup.cfg作るとBeta指定がAlphaで出力される
* install_requires相当の関連パッケージインストールさせる方法が分からない
* Windowsでtgz形式のアーカイブ作ろうとするとException
* `pysetup generate-setup` で作成したsetup.pyを `pysetup create` が変換対象として認識してしまう
* setup.pyがモジュールとしてsetup.cfgのmodulesフィールドに記載される

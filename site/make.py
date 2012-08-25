# -*- coding: utf-8 -*-
# Makefile for Sphinx documentation
#
# You can set these variables from the command line.
ENVPREFIX     = '../env/'
SPHINXOPTS    = ''
SPHINXBUILD   = ENVPREFIX + 'bin/sphinx-build'
HG            = ENVPREFIX + 'bin/hg'
BUILDOUT      = ENVPREFIX + 'bin/buildout'
PYTHON        = 'python'
PAPER         = ''
BUILDDIR      = 'build'
PROJECTNAME   = 'freia'

# Internal variables.
PAPEROPT      = ('-D latex_paper_size=' + PAPER) if PAPER else ''
ALLSPHINXOPTS = [
    '-d', BUILDDIR + '/doctrees',
    PAPEROPT,
    SPHINXOPTS,
    'source',
]


import sys
import os

sys.path.insert(0, os.path.join(ENVPREFIX, 'utils'))

from mk import make

target, sh, echo = make.target, make.sh, make.echo

#.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest

@target()
def clean():
    """to remove BUILDDIR/*"""
    return make.rm(BUILDDIR + '/*')

@target()
def bootstrap():
    """to bootstraping buildout environment"""
    os.chdir(ENVPREFIX)
    return sh(PYTHON, '-S', 'bootstrap.py', '-d')

@target()
def buildout():
    """to update buildout environment"""
    os.chdir(ENVPREFIX)
    return sh(BUILDOUT)

@target()
def update():
    """to pull & update & make html"""
    if sh(HG, 'incoming', '-q'):
        print('not changed')
        return
    if sh(HG, 'pull', '-u'):
        return
    return make.call('html')

@target()
def html():
    """to make standalone HTML files"""
    bdir = BUILDDIR + '/html'
    sh(SPHINXBUILD, '-b', 'html', ALLSPHINXOPTS, bdir)
    echo()
    echo("Build finished. The HTML pages are in {bdir}.")

@target()
def dirhtml():
    """to make HTML files named index.html in directories"""
    bdir = BUILDDIR + '/dirhtml'
    sh(SPHINXBUILD, '-b', 'dirhtml', ALLSPHINXOPTS, bdir)
    echo()
    echo("Build finished. The HTML pages are in {bdir}.")

@target()
def singlehtml():
    """to make a single large HTML file"""
    bdir = BUILDDIR + '/singlehtml'
    sh(SPHINXBUILD, '-b', 'singlehtml', ALLSPHINXOPTS, bdir)
    echo()
    echo("Build finished. The HTML page is in {bdir}.")

@target()
def pickle():
    """to make pickle files"""
    bdir = BUILDDIR + '/pickle'
    sh(SPHINXBUILD, '-b', 'pickle', ALLSPHINXOPTS, bdir)
    echo()
    echo("Build finished; now you can process the pickle files.")

@target()
def json():
    """to make JSON files"""
    bdir = BUILDDIR + '/json'
    sh(SPHINXBUILD, '-b', 'json', ALLSPHINXOPTS, bdir)
    echo()
    echo("Build finished; now you can process the JSON files.")

@target()
def htmlhelp():
    """to make HTML files and a HTML help project"""
    bdir = BUILDDIR + '/htmlhelp'
    sh(SPHINXBUILD, '-b', 'htmlhelp', ALLSPHINXOPTS, bdir)
    echo()
    echo("Build finished; now you can run HTML Help Workshop with the"
         ".hhp project file in {bdir}.")

@target()
def qthelp():
    """to make HTML files and a qthelp project"""
    bdir = BUILDDIR + '/qthelp'
    sh(SPHINXBUILD, '-b', 'qthelp', ALLSPHINXOPTS, bdir)
    echo()
    echo("Build finished; now you can run `qcollectiongenerator` with the"
         ".qhcp project file in {bdir}, like this:\n"
         "# qcollectiongenerator {bdir}/{PROJECTNAME}.qhcp"
         "To view the help file:\n"
         "# assistant -collectionFile {bdir}/{PROJECTNAME}.qhc")

@target()
def devhelp():
    """to make HTML files and a Devhelp project"""
    bdir = BUILDDIR + '/devhelp'
    sh(SPHINXBUILD, '-b', 'devhelp', ALLSPHINXOPTS, bdir)
    echo()
    echo("Build finished.")
    echo("To view the help file:")
    echo("# mkdir -p $HOME/.local/share/devhelp/{PROJECTNAME}")
    echo("# ln -s {bdir} $HOME/.local/share/devhelp/{PROJECTNAME}")
    echo("# devhelp")

@target()
def epub():
    """to make an epub"""
    bdir = BUILDDIR + '/epub'
    sh(SPHINXBUILD, '-b', 'epub', ALLSPHINXOPTS, bdir)
    echo()
    echo("Build finished. The epub file is in {bdir}.")

@target()
def latex():
    """to make LaTeX files, you can set PAPER=a4 or PAPER=letter"""
    #TODO: PAPER is envoronment? option args?
    bdir = BUILDDIR + '/latex'
    sh(SPHINXBUILD, '-b', 'latex', ALLSPHINXOPTS, bdir)
    echo()
    echo("Build finished; the LaTeX files are in {bdir}.")
    echo("Run `make' in that directory to run these through (pdf)latex"
         "(use `make latexpdf' here to do that automatically).")

@target()
def latexpdf(sub_target='all_pdf'):
    """to make LaTeX files and run them through pdflatex"""
    bdir = BUILDDIR + '/latex'
    sh(SPHINXBUILD, '-b', 'latex', ALLSPHINXOPTS, bdir)
    echo("Running LaTeX files through pdflatex...")
    sh('make.py', sub_target, cwd=bdir)
    echo("pdflatex finished; the PDF files are in {bdir}.")

@target()
def latexpdfja():
    """to make LaTeX files and run them through pdflatex"""
    make.call('latexpdf', 'all_pdf_ja')

@target()
def text():
    """to make text files"""
    bdir = BUILDDIR + '/text'
    sh(SPHINXBUILD, '-b', 'text', ALLSPHINXOPTS, bdir)
    echo()
    echo("Build finished. The text files are in {bdir}.")

@target()
def man():
    """to make manual pages"""
    bdir = BUILDDIR + '/man'
    sh(SPHINXBUILD, '-b', 'man', ALLSPHINXOPTS, bdir)
    echo()
    echo("Build finished. The manual pages are in {bdir}.")

@target()
def changes():
    """to make an overview of all changed/added/deprecated items"""
    bdir = BUILDDIR + '/changes'
    sh(SPHINXBUILD, '-b', 'changes', ALLSPHINXOPTS, bdir)
    echo()
    echo("The overview file is in {bdir}.")

@target()
def linkcheck():
    """to check all external links for integrity"""
    bdir = BUILDDIR + '/linkcheck'
    sh(SPHINXBUILD, '-b', 'linkcheck', ALLSPHINXOPTS, bdir)
    echo()
    echo("Link check complete; look for any errors in the above output "
         "or in {bdir}/output.txt.")

@target()
def doctest():
    """to run all doctests embedded in the documentation (if enabled)"""
    bdir = BUILDDIR + '/doctest'
    sh(SPHINXBUILD, '-b', 'doctest', ALLSPHINXOPTS, bdir)
    echo("Testing of doctests in the sources finished, look at the "
         "results in {bdir}/output.txt.")


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    make.run()

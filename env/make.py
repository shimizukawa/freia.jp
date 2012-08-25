# -*- coding: utf-8 -*-
# Makefile for Sphinx documentation
#
# You can set these variables from the command line.
ENVPREFIX     = './'
HG            = ENVPREFIX + 'bin/hg'
BUILDOUT      = ENVPREFIX + 'bin/buildout'
PYTHON        = 'python'

import sys
import os

sys.path.insert(0, os.path.join(ENVPREFIX, 'utils'))

from mk import make

target, sh, echo = make.target, make.sh, make.echo

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
        echo('not changed')
        return
    if sh(HG, 'pull', '-u'):
        return
    return make.call('html')


if __name__ == '__main__':
    make.run()

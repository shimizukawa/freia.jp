# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import os
import sys
import time
import tarfile

from .mk import make


#defines
WORK_DIRS = ['bin', 'parts', 'develop-eggs']
EGG_DIR = 'eggs'
BUILDOUT_CMD = 'bin/buildout'
if sys.platform.startswith('win'):
    BUILDOUT_CMD += '.exe'


@make.target() #this is make target.
@make.depend('buildout') #run dependents before target
def all():
    return make.sh(BUILDOUT_CMD, '-N') #call shell command


@make.target(BUILDOUT_CMD) #check existent
def buildout():
    make.mkdir(EGG_DIR) #make dir if not exist
    return make.sh(
        sys.executable, '-S', 'bootstrap.py',
        '-d',
        '--eggs', EGG_DIR,
        '--setup-source', 'distribute_setup.py',
        '--version', '1.5.2',
    )


@make.target()
def clean():
    make.rm(*WORK_DIRS) #remove directories if exist


@make.target()
def remove_eggs():
    make.rm(EGG_DIR)


@make.target()
@make.depend('clean', 'remove_eggs', 'buildout')
def pkg():
    make.sh(BUILDOUT_CMD, '-c', 'buildout-mkpkg.cfg')
    make.call('clean') #call another make target

    name = os.path.basename(os.getcwd())
    filename = '{0}-{1}.tgz'.format(name, time.strftime('%Y%m%d-%H%M%S'))
    with tarfile.open('../'+filename, 'w|gz') as tar:
        tar.add('.', name)

    print('deploy package:', filename)


if __name__ == '__main__':
    make.run()

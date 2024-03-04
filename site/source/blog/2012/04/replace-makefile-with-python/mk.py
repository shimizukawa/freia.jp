# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import sys
import subprocess
import shutil


class Runner(object):
    def __init__(self, func, depends=None, targets=None):
        if isinstance(func, self.__class__):
            self.func = func.func
            self.depends = depends or func.depends or []
            self.targets = targets or func.targets or []
        else:
            self.func = func
            self.depends = depends or []
            self.targets = targets or []
        self.name = self.func.__name__

    def __call__(self, *args, **kw):
        # targets
        if self.targets and __builtins__.all(
                os.path.exists(target) for target in self.targets):
            print("Skip:", self.name)
            print(" all targets are exists:", self.targets)
            return 0

        # depends
        for depend in self.depends:
            ret = make.call(depend)
            if ret:
                return ret
        # main
        print("In:", self.name)
        ret = self.func(*args, **kw)
        print("Out:", self.name)
        return ret


class make(object):
    """class for namespace"""
    __commands = {}

    #private
    @classmethod
    def _register(cls, func, depends=None, targets=None):
        func = Runner(func, depends=depends, targets=targets)
        cls.__commands[func.name] = func
        return func

    #decorator
    @classmethod
    def depend(cls, *depends):
        def inner(func):
            return cls._register(func, depends=depends)
        return inner

    #decorator
    @classmethod
    def target(cls, *targets):
        def inner(func):
            return cls._register(func, targets=targets)
        return inner

    #utility
    @classmethod
    def sh(cls, *args):
        print(' '.join(args))
        return subprocess.check_call(args)

    #utility
    @classmethod
    def rm(cls, *dirs):
        for d in dirs:
            shutil.rmtree(d, True)

    #utility
    @classmethod
    def mkdir(cls, path):
        if not os.path.exists(path):
            os.makedirs(EGG_DIR)

    #utility
    @classmethod
    def call(cls, name, args=[], kw={}):
        return cls.__commands[name](*args, **kw)

    #utility
    @classmethod
    def run(cls):
        if len(sys.argv) < 2:
            if 'all' in cls.__commands:
                sys.argv.append('all')
            else:
                print(sys.argv[0], 'need target.')
                for key in sorted(cls.__commands.keys()):
                    print(' ', key)
                sys.exit(-1)

        target = sys.argv[1]
        try:
            ret = cls.call(target)
        except:
            print('Error in', target)
            raise

        if ret:
            print('Error in', target, '::', ret)
        if not isinstance(ret, int) and ret is not None:
            ret = -1
        sys.exit(ret)

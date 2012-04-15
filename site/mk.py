# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import sys
import glob
import subprocess
import shutil


def flatten(seq):
    def _flatten(seq):
        if isinstance(seq, (list, tuple)):
            for s in seq:
                for x in _flatten(s):
                    yield x
        else:
            yield seq
    return filter(None, _flatten(seq))


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
        self.__name__ = self.func.__name__
        self.__doc__ = self.func.__doc__

    def __call__(self, *args, **kw):
        # targets
        if self.targets and __builtins__.all(
                os.path.exists(target) for target in self.targets):
            print("Skip:", self.__name__)
            print(" all targets are exists:", self.targets)
            return 0

        # depends
        for depend in self.depends:
            ret = make.call(depend)
            if ret:
                return ret
        # main
        print("In:", self.__name__)
        ret = self.func(*args, **kw)
        print("Out:", self.__name__)
        return ret


class make(object):
    """class for namespace"""
    __commands = {}
    __commands_order = []

    #private
    @classmethod
    def _register(cls, func, depends=None, targets=None):
        func = Runner(func, depends=depends, targets=targets)
        cls.__commands[func.__name__] = func
        if func.__name__ not in cls.__commands_order:
            cls.__commands_order.append(func.__name__)
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
        args = flatten(args)
        print(' '.join(args))
        return subprocess.check_call(args)

    #utility
    @classmethod
    def rm(cls, *dirs):
        for d in dirs:
            for f in glob.glob(d):
                shutil.rmtree(f, True)

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
    def echo(cls, *args, **kw):
        d = dict(sys._getframe().f_back.f_globals)
        d.update(dict(sys._getframe().f_back.f_locals))
        args = [a.format(**d) for a in args]
        print(*args, **kw)

    #utility
    @classmethod
    def targets(cls):
        return [cls.__commands[t] for t in cls.__commands_order]

    #utility
    @classmethod
    def run(cls):
        target = ''
        if len(sys.argv) >= 2:
            target = sys.argv[1]
        if not target:
            if len(cls.__commands_order):
                target = cls.__commands_order[0]
            else:
                print(sys.argv[0], 'have no target.')
                sys.exit(-1)

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

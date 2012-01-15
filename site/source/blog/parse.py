# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division

import os
import re
import io
import unicodedata
import datetime
import itertools
import urllib2
import shutil


filetype = {
        'text/structured': '.stx',
        'text/x-rst': '.rst',
        'text/plain': '.txt',
        'text/html': '.html',
}


def wlen(text):
    n = 0
    for c in text:
        if unicodedata.east_asian_width(c) in ('F', 'W', 'A'):
            n += 2
        else:  # 'N', 'Na', 'H'
            n += 1
    return n


class FieldListProc(object):
    matcher = re.compile('^:([\w\s_-]+):\s*(.*)\s*$').match

    def __call__(self, entry, line):
        m = self.matcher(line)
        if not m:
            return line

        key,value = m.groups()
        if key == 'id':
            entry.id = value
            line = None
        elif key == 'title':
            entry.title = value
            line = None
        elif key == 'date':
            entry.date = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        elif key == 'categories':
            entry.categories = value.strip('[] \r\n')
        elif key == 'body type':
            entry.body_type = value
        elif key == 'extend type':
            line = '.. ' + line
        elif key == 'extend':
            line = '.. ' + line + '\n'
        elif key in ('comments', 'trackbacks'):
            line = '.. ' + line
            entry.comment = True
        elif key == 'body':
            line = ''
            title = entry.title
            if title:
                if entry.date:
                    title = entry.date.strftime('%Y/%m/%d ') + title
                border = '=' * wlen(title)
                line = ''.join([
                    '\n',
                    border+'\n',
                    title+'\n',
                    border+'\n',
                    '\n',
                ])
            if entry.categories:
                line += '*Category: %s*\n\n' % entry.categories
            if value:
                line += value

        if line is not None:
            entry.body.append(line)
        return None


class CodeblockProc(object):
    matcher = re.compile('^(\s*.. code-block::)\s+([\w\s_-]+)\s*$').match

    def __call__(self, entry, line):
        m = self.matcher(line)
        if not m:
            return line

        key,value = m.groups()
        entry.body.append("%s %s" % (key, value.lower()))
        return None


class ImageDirectiveProc(object):
    matcher = re.compile('^(\s*.. (.+\s+)?(image|figure)::)\s+(.+)\s*$').match

    def __call__(self, entry, line):
        m = self.matcher(line)
        if not m:
            return line

        key, rep, _, value = m.groups()

        if value[0] == '/':
            value = 'http://www.freia.jp' + value

        if value.startswith("http"):
            try:
                print("INFO: check URL:", value)
                uo = urllib2.urlopen(value)
                uo.read()
            except:
                print("Warning: image not found at:", value)
            entry.body.append("%s %s\n" % (key, value))

        elif os.path.exists(value):
            entry.related_files.append(os.path.abspath(value))
            value = value.split('/')[-1]
            entry.body.append("%s %s\n" % (key, value))

        else:
            parts_rest = value.split('/')
            parts = []
            for v in parts_rest:
                if not os.path.exists('/'.join(parts + [v])):
                    break
                parts.append(v)
            parts_rest = parts_rest[len(parts):]
            if parts:
                entry.related_files.append('/'.join(parts))
                value = parts[-1]
                entry.body.append("%s %s\n" % (key, value))
            if parts_rest:
                print("Warning: discard extra image path:", parts_rest)
        return None


class CorrectShortlineProc(object):

    def __init__(self):
        self.prev_wlen = 0

    def __call__(self, entry, line):
        l = line.rstrip('\r\n ')
        grouped = list(itertools.groupby(sorted(l)))
        if len(grouped) == 1:
            k, g = grouped[0]
            if k in '#*=-^"~':
                if len(l) < self.prev_wlen:
                    line = k * self.prev_wlen + '\n'
        self.prev_wlen = wlen(line.rstrip('\r\n '))
        return line


class Entry(object):
    id = ''
    title = ''
    body = []

    def __init__(self):
        pass

    @classmethod
    def generate(cls, payload):
        self = cls()
        self._payload = payload
        self.body = []
        self.comment = False
        self.body_type = None
        self.date = None
        self.categories = None
        self.related_files = []

        procs = [FieldListProc(), CodeblockProc(),
                ImageDirectiveProc(), CorrectShortlineProc()]

        for line in payload:
            if self.comment:
                self.body.append('.. ' + line)
                continue

            for proc in procs:
                line = proc(self, line)
                if line is None:
                    break
            else:
                self.body.append(line)

        return self

    @property
    def ext(self):
        return filetype.get(self.body_type, '.xtxt')

    @property
    def ref(self):
        return '/'.join([self.id, 'index' + self.ext])

    def save(self):
        if not self.id:
            raise RuntimeError('entry id need not Empty')
        if self.id[-1] == 'x' or self.id.endswith('_ng'):
            print("INFO: skip entry:", self.id)
            if os.path.isdir(self.id):
                shutil.rmtree(self.id)
                print("INFO: directory removed", self.id)
            return
        if not os.path.isdir(self.id):
            os.mkdir(self.id)
        fn = self.ref
        print('saving', fn)
        with io.open(fn, 'wt', encoding='utf-8') as f:
            while not self.body[0].rstrip('\r\n'):
                self.body.pop(0)
            f.writelines(self.body)
            f.close()

        if self.related_files:
            for fpath in self.related_files:
                print('copying', fpath, '...')
                shutil.copy2(fpath, self.id)



def payload_gen(fobj):
    payload = []
    for line in iter(fobj.readline, ''):
        if line == '%%%%%%%%%\n':
            yield payload
            payload = []
        else:
            payload.append(line)


def entry_gen(fobj):
    for payload in payload_gen(fobj):
        yield Entry.generate(payload)


def main():
    idx = []
    with io.open('_CoreblogExport.txt', 'rU', encoding='utf-8') as f:
        for entry in entry_gen(f):
            entry.save()
            idx.append('   ' + entry.ref + '\n')

    fn = '_index.out'
    with io.open(fn, 'wt', encoding='utf-8') as f:
        print('saving', fn)
        f.write('.. toctree::\n')
        f.write('   :maxdepth: 1\n\n')
        f.writelines(reversed(idx))


if __name__ == '__main__':
    main()

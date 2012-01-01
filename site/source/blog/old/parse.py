# -*- coding utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division

import os
import re
import io
import unicodedata

field_matcher = re.compile('^:([\w\s_-]+):\s*(.*)\s*$').match

filetype = {
        'text/structured': '.stx',
        'text/x-rst': '.rst',
        'text/plain': '.txt',
        'text/html': '.html',
}


def wlen(text):
    n = 0
    for c in text:
        if unicodedata.east_asian_width(c) == 'W':
            n += 2
        else:
            n += 1
    return n


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

        for line in payload:
            if self.comment:
                self.body.append('.. ' + line)
                continue

            m = field_matcher(line)
            if not m:
                self.body.append(line)
                continue
            else:
                key,value = m.groups()
                if key == 'id':
                    self.id = value
                elif key == 'title':
                    self.title = value
                elif key == 'body type':
                    self.body.append(line)
                    self.body_type = value
                elif key == 'extend':
                    self.body.append('.. ' + line)
                elif key == 'extend type':
                    self.body.append('.. ' + line)
                elif key == 'comments':
                    self.body.append('.. ' + line)
                    self.comment = True
                elif key == 'body':
                    if self.title:
                        border = '=' * wlen(self.title)
                        self.body.append('\n')
                        self.body.append(border+'\n')
                        self.body.append(self.title+'\n')
                        self.body.append(border+'\n')
                        self.body.append('\n')
                    if value:
                        self.body.append(line)
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
        if not os.path.isdir(self.id):
            os.mkdir(self.id)
        fn = self.ref
        print('saving', fn)
        with io.open(fn, 'wt', encoding='utf-8') as f:
            while not self.body[0].rstrip('\r\n'):
                self.body.pop(0)
            f.writelines(self.body)
            f.close()


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
    with io.open('index.rst', 'wt', encoding='utf-8') as idx:
        idx.write('.. toctree::\n\n')
        with io.open('TopPage.txt', 'rU', encoding='utf-8') as f:
            for entry in entry_gen(f):
                entry.save()
                idx.write('   ' + entry.ref + '\n')


if __name__ == '__main__':
    main()

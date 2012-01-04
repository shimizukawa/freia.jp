# -*- coding utf-8 -*-
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

field_matcher = re.compile('^:([\w\s_-]+):\s*(.*)\s*$').match
codeblock_matcher = re.compile('^(\s*.. code-block::)\s+([\w\s_-]+)\s*$').match

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
        self.prev_wlen = 0  # for correct_shortline_proc

        def field_list_proc(line):
            m = field_matcher(line)
            if not m:
                return line

            key,value = m.groups()
            if key == 'id':
                self.id = value
                line = None
            elif key == 'title':
                self.title = value
                line = None
            elif key == 'date':
                self.date = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
            elif key == 'categories':
                self.categories = value.strip('[] \r\n')
            elif key == 'body type':
                self.body_type = value
            elif key == 'extend type':
                line = '.. ' + line
            elif key == 'extend':
                line = '.. ' + line + '\n'
            elif key in ('comments', 'trackbacks'):
                line = '.. ' + line
                self.comment = True
            elif key == 'body':
                line = ''
                title = self.title
                if title:
                    if self.date:
                        title = self.date.strftime('%Y/%m/%d ') + title
                    border = '=' * wlen(title)
                    line = ''.join([
                        '\n',
                        border+'\n',
                        title+'\n',
                        border+'\n',
                        '\n',
                    ])
                if self.categories:
                    line += '*Category: %s*\n\n' % self.categories
                if value:
                    line += value

            if line is not None:
                self.body.append(line)
            return None

        def codeblock_proc(line):
            m = codeblock_matcher(line)
            if not m:
                return line

            key,value = m.groups()
            self.body.append("%s %s" % (key, value.lower()))
            return None

        def correct_shortline_proc(line):
            l = line.rstrip('\r\n ')
            grouped = list(itertools.groupby(sorted(l)))
            if len(grouped) == 1:
                k, g = grouped[0]
                if k in '#*=-^"~':
                    if len(l) < self.prev_wlen:
                        line = k * self.prev_wlen + '\n'
            self.prev_wlen = wlen(line.rstrip('\r\n '))
            return line

        for line in payload:
            if self.comment:
                self.body.append('.. ' + line)
                continue

            for proc in [field_list_proc, codeblock_proc, correct_shortline_proc]:
                line = proc(line)
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

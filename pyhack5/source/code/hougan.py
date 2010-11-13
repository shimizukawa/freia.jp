# -*- coding: utf-8 -*-
from types import *
import re

__all__ = ['Hougan']

COLOR_PALETTE = {
    0: 'black',
    1: 'white',
    2: 'red',
    3: 'green',
    4: 'brue',
    5: 'yellow',
    6: 'magenda',
    7: 'cyan',
}

rowcol_finder = re.compile('^([a-zA-Z]+)(\d+)$').findall
range_finder = re.compile('^([a-zA-Z]+\d+):([a-zA-Z]+\d+)$').findall


class HouganError(Exception):
    pass


class UnknownIndexError(HouganError):
    pass

class CellIndexError(UnknownIndexError):
    pass

class RangeIndexError(UnknownIndexError):
    pass


def col_by_name(colname):
    """
    文字列で与えられた列座標を数値の座標に変換します。

        >>> col_by_name('A')
        0
        >>> col_by_name('AE')
        30

    """
    col = 0
    pow = 1
    for i in xrange(len(colname)-1, -1, -1):
        ch = colname[i]
        col += (ord(ch) - ord('A') + 1) * pow
        pow *= 26
    return col - 1


def rowcol_to_cell(row, col):
    """
    数値で与えられた座標を 'A1' のような文字列での座標に変換します。

        >>> rowcol_to_cell(0, 0)
        'A1'
        >>> rowcol_to_cell(100, 100)
        'CW101'

    """
    d = col // 26
    m = col % 26
    chr1 = ""    # Most significant character in AA1
    if d > 0:
        chr1 = chr(ord('A') + d  - 1)
    chr2 = chr(ord('A') + m)
    # Zero index to 1-index
    return chr1 + chr2 + str(row + 1)


def cell_index_by_name(name):
    """
    >>> cell_index_by_name((0,0))
    (0, 0)

    >>> cell_index_by_name([0, 0])
    (0, 0)

    >>> cell_index_by_name((-1, -1))
    Traceback (most recent call last):
    ...
    CellIndexError: (-1, -1)

    >>> cell_index_by_name((0,1,2))
    Traceback (most recent call last):
    ...
    CellIndexError: (0, 1, 2)

    >>> cell_index_by_name('A1')
    (0, 0)

    >>> cell_index_by_name('A')
    Traceback (most recent call last):
    ...
    CellIndexError: 'A'

    >>> cell_index_by_name('B10')
    (9, 1)

    >>> cell_index_by_name('c10')
    (9, 2)

    >>> cell_index_by_name('AB10')
    (9, 27)

    >>> cell_index_by_name(('A', 1))
    Traceback (most recent call last):
    ...
    CellIndexError: ('A', 1)
    """
    if type(name) in (ListType, TupleType):
        index = tuple(name)
        if len(index) != 2:
            raise CellIndexError(repr(name))

    elif isinstance(name, basestring):
        parsed = rowcol_finder(name)
        if not parsed:
            raise CellIndexError(repr(name))
        col_name, row_name = parsed[0]
        col_idx = col_by_name(col_name.upper())
        row_idx = int(row_name) - 1
        index = row_idx, col_idx

    if not all(isinstance(x, int) for x in index):
        raise CellIndexError(repr(name))

    if not all(x >= 0 for x in index):
        raise CellIndexError(repr(name))

    return index


def range_index_by_name(_range):
    """
    >>> range_index_by_name('A1:B2')
    ((0, 0), (1, 1))

    >>> range_index_by_name( ((0,10),(15,22)) )
    ((0, 10), (15, 22))

    >>> range_index_by_name('A1')
    Traceback (most recent call last):
    ...
    RangeIndexError: 'A1'

    >>> range_index_by_name('foo-bar')
    Traceback (most recent call last):
    ...
    RangeIndexError: 'foo-bar'
    """
    if type(_range) in (ListType, TupleType):
        index = tuple(_range)
        if len(index) != 2:
            raise RangeIndexError(repr(_range))

    elif isinstance(_range, basestring):
        parsed = range_finder(_range)
        if not parsed:
            raise RangeIndexError(repr(_range))
        index = parsed[0]

    return tuple(cell_index_by_name(x) for x in index)


class Cell(object):

    def __init__(self, index, value=None):
        """
        >>> Cell((0,0))
        <Cell 'A1' (0, 0), value=None, color=black at ...>
        >>> Cell('Z10')
        <Cell 'Z10' (9, 25), value=None, color=black at ...>
        """
        self.index = cell_index_by_name(index)
        self.value = None
        self.color = 0

    def __repr__(self):
        """
        >>> c = Cell((0,0))
        >>> c
        <Cell 'A1' (0, 0), value=None, color=black at ...>

        >>> c.value = 10
        >>> c
        <Cell 'A1' (0, 0), value=10, color=black at ...>

        >>> c.color = 7
        >>> c
        <Cell 'A1' (0, 0), value=10, color=cyan at ...>
        """
        class_name = self.__class__.__name__
        index = self.index
        rowcol = rowcol_to_cell(*index)
        value = self.value
        color = COLOR_PALETTE.get(self.color, 'unknown')
        addr = id(self)
        return "<%(class_name)s '%(rowcol)s' %(index)r, value=%(value)r, color=%(color)s at 0x%(addr)08x>" % locals()


class Range(object):
    """
    >>> hougan = Hougan()
    >>> r1 = Range(hougan, 'A1:B2')
    >>> r2 = hougan['A1:B2']

    >>> r1
    <Range 'A1:B2' (0, 0)-(1, 1), ...>
    >>> r2
    <Range 'A1:B2' (0, 0)-(1, 1), ...>
    >>> r1 is r2
    False
    >>> r1 == r2
    True

    >>> for cell in r1:
    ...     print cell
    <Cell 'A1' (0, 0), value=None, color=black at ...>
    <Cell 'B1' (0, 1), value=None, color=black at ...>
    <Cell 'A2' (1, 0), value=None, color=black at ...>
    <Cell 'B2' (1, 1), value=None, color=black at ...>

    >>> r1.value = 'foo'
    >>> for cell in r1:
    ...     print cell
    <Cell 'A1' (0, 0), value='foo', color=black at ...>
    <Cell 'B1' (0, 1), value='foo', color=black at ...>
    <Cell 'A2' (1, 0), value='foo', color=black at ...>
    <Cell 'B2' (1, 1), value='foo', color=black at ...>

    """

    def __init__(self, _hougan, _range):
        """
        >>> hougan = Hougan()
        >>> Range(hougan, 'A1:B2')
        <Range 'A1:B2' (0, 0)-(1, 1), ...>
        >>> Range(hougan, ((0,10),(15,22)) )
        <Range 'K1:W16' (0, 10)-(15, 22), ...>
        """
        self._hougan = _hougan
        self.index1, self.index2 = range_index_by_name(_range)

    def __repr__(self):
        class_name = self.__class__.__name__
        index1 = self.index1
        index2 = self.index2
        rowcol1 = rowcol_to_cell(*index1)
        rowcol2 = rowcol_to_cell(*index2)
        addr = id(self)
        return "<%(class_name)s '%(rowcol1)s:%(rowcol2)s' %(index1)r-%(index2)r, 0x%(addr)08x>" % locals()

    def __eq__(self, rhs):
        """
        >>> hougan = Hougan()
        >>> r1 = Range(hougan, 'A1:B2')
        >>> r2 = hougan['A1:B2']
        >>> r1 == r2
        True
        """
        if (self.index1, self.index2) == (rhs.index1, rhs.index2):
            return self._hougan is rhs._hougan
        return False

    def __iter__(self):
        """
        >>> hougan = Hougan()
        >>> for cell in Range(hougan, 'A1:B2'):
        ...     print cell
        <Cell 'A1' (0, 0), value=None, color=black at ...>
        <Cell 'B1' (0, 1), value=None, color=black at ...>
        <Cell 'A2' (1, 0), value=None, color=black at ...>
        <Cell 'B2' (1, 1), value=None, color=black at ...>
        """
        for row in range(self.index1[0], self.index2[0]+1):
            for col in range(self.index1[1], self.index2[1]+1):
                yield self._hougan[row,col]

    @property
    def value(self):
        raise NotImplementedError('Range.value setter is not implemented yet')

    @value.setter
    def value(self, value):
        """
        >>> hougan = Hougan()
        >>> hougan['A1']
        <Cell 'A1' (0, 0), value=None, color=black at ...>

        >>> r = Range(hougan, 'A1:B2')
        >>> r.value = 'foo'
        >>> hougan['A1']
        <Cell 'A1' (0, 0), value='foo', color=black at ...>
        >>> hougan['B2']
        <Cell 'B2' (1, 1), value='foo', color=black at ...>
        """
        for cell in self:
            cell.value = value
        return value

    @property
    def color(self):
        raise NotImplementedError('Range.color setter is not implemented yet')

    @color.setter
    def color(self, color):
        """
        >>> hougan = Hougan()
        >>> hougan['A1']
        <Cell 'A1' (0, 0), value=None, color=black at ...>

        >>> r = Range(hougan, 'A1:B2')
        >>> r.color = 2
        >>> hougan['A1']
        <Cell 'A1' (0, 0), value='foo', color=black at ...>
        >>> hougan['B2']
        <Cell 'B2' (1, 1), value='foo', color=black at ...>
        """
        for cell in self:
            cell.color = color
        return color

    # TODO: self.value と self.color は同じロジックなのでまとめるべきか？
    # このvalue, color のsetter/getter実装をまとめるのは早計と判断。


class Hougan(object):
    """
    Hougan は縦横のマス目のある方眼紙状のデータを簡単に扱うクラスです。

        >>> hougan = Hougan()
        >>> hougan
        <Hougan (1x1) at ...>

    方眼紙には行と列があり、それぞれが0行目、0列目からはじまります。
    方眼紙の各マス目をそれぞれセルとよび、その座標は行と列の
    インデックスで表されます。つまり一番左上は `セル(0, 0)` です。

    セルは、任意の座標(ここでは0,0)を指定してhouganから以下のように
    取り出すことが出来ます。

        >>> cell = hougan[0,0]
        >>> cell
        <Cell 'A1' (0, 0), value=None, color=black at ...>

    各セルには値(value)と背景色(color)の属性があり、値には数値や
    文字列を格納できますが初期値はNoneです。

        >>> cell.value is None
        True

        >>> cell.value = 1

    色は0から7までの値で表現され、それぞれ以下の色を意味しています。

        == ========
        値 色名
        -- --------
        0  black
        1  white
        2  red
        3  green
        4  brue
        5  yellow
        6  magenda
        7  cyan
        == ========

    colorは値で取得・設定します。

        >>> cell.color
        0

        >>> cell.color = 1


    座標1,1に値を設定するには、例えば以下のようにします。

        >>> hougan[1,1].value = 123

    Houganインスタンスは座標の最大値を保持しています。

        >>> hougan
        <Hougan (2x2) at ...>

    方眼紙はテキストで出力することができます。テキストの場合、色は
    表示されず、値が方眼紙状に表示されます。

        >>> print str(hougan)
        = ===
        1
          123
        = ===

    将来的にはcsv形式や表計算ソフトで読み込める形式の出力も実装
    する予定ですが、現在はサポートしていません。
    """

    def __init__(self):
        """
        Hougan は初期化状態で1x1のサイズのセルを持っています。
        この方眼紙のサイズは値を設定した際に自動的に拡張されます。

            >>> hougan = Hougan()
            >>> hougan
            <Hougan (1x1) at ...>
        """
        self._cell_pool = {}
        self._max_cell = (0, 0)

    def _update_max(self, index):
        r1, c1 = self._max_cell
        r2, c2 = index
        self._max_cell = (max(r1,r2), max(c1,c2))

    def __repr__(self):
        class_name = self.__class__.__name__
        row_max = self._max_cell[0] + 1
        col_max = self._max_cell[1] + 1
        addr = id(self)
        return "<%(class_name)s (%(row_max)dx%(col_max)d) at 0x%(addr)08x>" % locals()

    def __iter__(self):
        """
        >>> hougan = Hougan()
        >>> hougan[0,0].color = 6
        >>> hougan[0,1].value = 10
        >>> hougan[1,2].color = 3
        >>> hougan[1,3].value = 20
        >>> hougan[2,0].value = 30
        >>> hougan[2,0].color = 2
        >>> hougan[2,1].color = 5
        >>> for cell in hougan:
        ...     print cell
        <Cell 'A1' (0, 0), value=None, color=magenda at ...>
        <Cell 'B1' (0, 1), value=10, color=black at ...>
        <Cell 'C1' (0, 2), value=None, color=black at ...>
        <Cell 'D1' (0, 3), value=None, color=black at ...>
        <Cell 'A2' (1, 0), value=None, color=black at ...>
        <Cell 'B2' (1, 1), value=None, color=black at ...>
        <Cell 'C2' (1, 2), value=None, color=green at ...>
        <Cell 'D2' (1, 3), value=20, color=black at ...>
        <Cell 'A3' (2, 0), value=30, color=red at ...>
        <Cell 'B3' (2, 1), value=None, color=yellow at ...>
        <Cell 'C3' (2, 2), value=None, color=black at ...>
        <Cell 'D3' (2, 3), value=None, color=black at ...>
        """
        for cell in self[(0,0), self._max_cell]:
            yield cell

    def __getitem__(self, index):
        """
        >>> hougan = Hougan()

        セルを一つ取得します

        >>> hougan[0,0]
        <Cell 'A1' (0, 0), value=None, color=black at ...>
        >>> hougan['B10']
        <Cell 'B10' (9, 1), value=None, color=black at ...>
        >>> hougan['B10'].value is None
        True
        >>> hougan['B10'].color == 0
        True

        範囲オブジェクトRangeを取得します

        >>> hougan[(0,0), (1,1)]
        <Range 'A1:B2' (0, 0)-(1, 1), ...>
        >>> hougan['C1:E4']
        <Range 'C1:E4' (0, 2)-(3, 4), ...>
        >>> hougan['C1:E4'].value = 10
        >>> hougan['C1:E4'].color = 2
        """
        try:
            index = cell_index_by_name(index)
        except CellIndexError,e:
            return Range(self, index)

        if index not in self._cell_pool:
            self._cell_pool[index] = Cell(index)
            self._update_max(index)
        return self._cell_pool[index]

    def __setitem__(self, index, value):
        """
        >>> hougan = Hougan()
        >>> hougan[0,0] = 1
        Traceback (most recent call last):
        ...
        NotImplementedError: Cell is not replacable yet.
        """
        raise NotImplementedError('Cell is not replacable yet.')

    def __str__(self):
        """
        >>> hougan = Hougan()
        >>> hougan[0,0].value = 1
        >>> hougan[1,1].value = 123
        >>> print str(hougan)
        = ===
        1
          123
        = ===
        """
        def to_value(value):
            return str(value) if value is not None else ''

        col_widths = [1] * (self._max_cell[1] + 1)
        for cell in self:
            col_idx = cell.index[1]
            w = col_widths[col_idx]
            col_widths[col_idx] = max(len(to_value(cell.value)), w)

        results = []
        border = ['='*w for w in col_widths]

        results.extend(border)

        for cell in self:
            row_idx, col_idx = cell.index
            w = col_widths[col_idx]
            fmt = '%%-%ds' % w
            results.append(fmt % to_value(cell.value))

        results.extend(border)

        step = len(col_widths)
        rows = (results[s:s+step] for s in xrange(0, len(results), step))
        return '\n'.join(' '.join(row) for row in rows)


if __name__ == '__main__':
    import doctest
    doctest.testmod(
        optionflags = (doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS) )

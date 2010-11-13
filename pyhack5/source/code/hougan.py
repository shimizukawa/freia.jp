# -*- coding: utf-8 -*-
from types import *
import re

__all__ = [
    'Hougan',
]

rowcol_finder = re.compile('^([a-zA-Z]+)(\d+)$').findall
range_finder = re.compile('^([a-zA-Z]+\d+):([a-zA-Z]+\d+)$').findall

class DictMapper(dict):
    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value
        return value


class HouganError(Exception):
    pass


class UnknownIndexError(HouganError):
    pass

class CellIndexError(UnknownIndexError):
    pass

class RangeIndexError(UnknownIndexError):
    pass


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
        <Cell 'A1' (0, 0), value=None, ...>
        >>> Cell('Z10')
        <Cell 'Z10' (9, 25), value=None, ...>
        """
        self.index = cell_index_by_name(index)
        self.value = None
        self.color = 0

    def __repr__(self):
        class_name = self.__class__.__name__
        index = self.index
        rowcol = rowcol_to_cell(*index)
        value = self.value
        addr = id(self)
        return "<%(class_name)s '%(rowcol)s' %(index)r, value=%(value)r, 0x%(addr)08x>" % locals()


class Range(object):
    """
    >>> wsw = Hougan()
    >>> r1 = Range(wsw, 'A1:B2')
    >>> r2 = wsw['A1:B2']

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
    <Cell 'A1' (0, 0), value=None, ...>
    <Cell 'B1' (0, 1), value=None, ...>
    <Cell 'A2' (1, 0), value=None, ...>
    <Cell 'B2' (1, 1), value=None, ...>

    >>> r1.value = 'foo'
    >>> for cell in r1:
    ...     print cell
    <Cell 'A1' (0, 0), value='foo', ...>
    <Cell 'B1' (0, 1), value='foo', ...>
    <Cell 'A2' (1, 0), value='foo', ...>
    <Cell 'B2' (1, 1), value='foo', ...>

    """

    def __init__(self, _worksheet_wrapper, _range):
        """
        >>> wsw = Hougan()
        >>> Range(wsw, 'A1:B2')
        <Range 'A1:B2' (0, 0)-(1, 1), ...>
        >>> Range(wsw, ((0,10),(15,22)) )
        <Range 'K1:W16' (0, 10)-(15, 22), ...>
        """
        self._worksheet_wrapper = _worksheet_wrapper
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
        >>> wsw = Hougan()
        >>> r1 = Range(wsw, 'A1:B2')
        >>> r2 = wsw['A1:B2']
        >>> r1 == r2
        True
        """
        if (self.index1, self.index2) == (rhs.index1, rhs.index2):
            return self._worksheet_wrapper is rhs._worksheet_wrapper
        return False

    def __iter__(self):
        """
        >>> wsw = Hougan()
        >>> for cell in Range(wsw, 'A1:B2'):
        ...     print cell
        <Cell 'A1' (0, 0), value=None, ...>
        <Cell 'B1' (0, 1), value=None, ...>
        <Cell 'A2' (1, 0), value=None, ...>
        <Cell 'B2' (1, 1), value=None, ...>
        """
        for row in range(self.index1[0], self.index2[0]+1):
            for col in range(self.index1[1], self.index2[1]+1):
                yield self._worksheet_wrapper[row,col]

    @property
    def value(self):
        raise NotImplementedError('Range.value setter is not implemented yet')

    @value.setter
    def value(self, value):
        """
        >>> wsw = Hougan()
        >>> wsw['A1']
        <Cell 'A1' (0, 0), value=None, ...>

        >>> r = Range(wsw, 'A1:B2')
        >>> r.value = 'foo'
        >>> wsw['A1']
        <Cell 'A1' (0, 0), value='foo', ...>
        >>> wsw['B2']
        <Cell 'B2' (1, 1), value='foo', ...>
        """
        for cell in self:
            cell.value = value
        return value

    @property
    def style(self):
        """
        >>> wsw = Hougan()
        >>> wsw['C3'].style
        0
        >>> wsw['C4'].style
        0
        >>> wsw['C3:D4'].style
        >>> wsw['C3'].style
        1
        >>> wsw['C4'].style
        1
        """
        def setter(context, name, value):
            for cell in self:
                obj = cell.style
                for n in name[:-1]:
                    obj = getattr(obj, n)
                setattr(obj, name[-1], value)
        return SetAttrHooker(XFStyle(), setter)


class Border(object):
    SOLID = 0x00


def set_border(borders, type, color):
    for area in ('left', 'right', 'top', 'bottom'):
        setattr(borders, area, type)
        setattr(borders, area + '_colour', color)
    return borders


class Pattern(DictMapper):
    NO_PATTERN    = 0x00
    SOLID_PATTERN = 0x01


class Hougan(object):
    """
    This wrapper class wrap pyExcelerator.Worksheet object for easy to use.

    >>> from pyExcelerator import Workbook
    >>> w = Workbook()
    >>> ws1 = w.add_sheet('sheetname')

    ラッパーを使うために、以下のようにしてpyExceleratorのワークシート
    オブジェクトをラップします

    >>> wsw = Hougan(ws1)

    セルの指定は[]で出来ます

    >>> wsw[0,0].value = 'foo'

    数値でもExcelの行列の名前でもアクセスできます

    >>> wsw[1,1].value = wsw['A1'].value
    >>> wsw['B2'].value
    'foo'

    ":" を使って範囲指定できます

    >>> wsw['A1:B2'].value = 'bar'
    >>> wsw['B2'].value
    'bar' 

    対象範囲に枠線を設定できます

    >>> wsw['C1:E4'].style.borders.left = Border.SOLID

    値をもとのワークシートオブジェクトに書き出します
    pyExceleratorの仕様により、一度しか書き出しで来ません

    >>> wsw.finalize()
    >>> w.save('file1.xls')
    """

    def __init__(self, worksheet=None):
        """
        Wrap Worksheet object:

        >>> from pyExcelerator import Workbook
        >>> w = Workbook()
        >>> ws1 = w.add_sheet('sheetname')
        >>> wsw1 = Hougan(ws1)

        or wrap dummy buffer mode:

        >>> wsw2 = Hougan()

        TODO: buffer morde mean what?
        """
        self.worksheet = worksheet
        self._cell_pool = {}
        self._max_cell = (0, 0)

    def _update_max(self, index):
        r1, c1 = self._max_cell
        r2, c2 = index
        self._max_cell = (max(r1,r2), max(c1,c2))

    def __iter__(self):
        """
        >>> wsw = Hougan()
        >>> wsw[0,1].value = 10
        >>> wsw[1,3].value = 20
        >>> wsw[2,0].value = 30
        >>> for cell in wsw:
        ...     print cell
        <Cell 'A1' (0, 0), value=None, ...>
        <Cell 'B1' (0, 1), value=10, ...>
        <Cell 'C1' (0, 2), value=None, ...>
        <Cell 'D1' (0, 3), value=None, ...>
        <Cell 'A2' (1, 0), value=None, ...>
        <Cell 'B2' (1, 1), value=None, ...>
        <Cell 'C2' (1, 2), value=None, ...>
        <Cell 'D2' (1, 3), value=20, ...>
        <Cell 'A3' (2, 0), value=30, ...>
        <Cell 'B3' (2, 1), value=None, ...>
        <Cell 'C3' (2, 2), value=None, ...>
        <Cell 'D3' (2, 3), value=None, ...>
        """
        for cell in self[(0,0), self._max_cell]:
            yield cell

    def __getitem__(self, index):
        """
        >>> wsw = Hougan()

        get single cell

        >>> wsw[0,0]
        <Cell 'A1' (0, 0), value=None, ...>
        >>> wsw['B10']
        <Cell 'B10' (9, 1), value=None, ...>
        >>> wsw['B10'].value is None
        True
        >>> wsw['B10'].style.borders.left = Border.SOLID

        get range

        >>> wsw[(0,0), (1,1)]
        <Range 'A1:B2' (0, 0)-(1, 1), ...>
        >>> wsw['C1:E4']
        <Range 'C1:E4' (0, 2)-(3, 4), ...>
        >>> wsw['C1:E4'].value = 10
        >>> wsw['C1:E4'].style.borders.left = Border.SOLID
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
        >>> wsw = Hougan()
        >>> wsw[0,0] = 1
        Traceback (most recent call last):
        ...
        NotImplementedError: Cell is not replacable yet.
        """
        raise NotImplementedError('Cell is not replacable yet.')

    def finalize(self):
        """
        >>> from pyExcelerator import Workbook
        >>> w = Workbook()
        >>> ws1 = w.add_sheet('sheetname')
        >>> wsw = Hougan(ws1)
        >>> wsw['B2'].value = 'foo'
        >>> wsw['C3:D4'].style.pattern.pattern = Pattern.SOLID_PATTERN
        >>> wsw['C3:D4'].style.pattern.pattern_fore_colour = 'cyan'
        >>> wsw.finalize()
        >>> w.save('file1.xls')
        """
        ws = self.worksheet
        for cell in self:
            kw = dict()
            if cell.value is not None:
                kw['label'] = cell.value
            if cell.style is not None:
                kw['style'] = cell.style
            ws.write(*cell.index, **kw)

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=(doctest.ELLIPSIS|doctest.NORMALIZE_WHITESPACE))


# -*- coding: utf-8 -*-
from datetime import date, timedelta

__all__ = ['DateEx']

class DateEx(date):
    """
    DateEx accept `+` and `-` operation. +/- means add/sub
    a day to DateEx instance::

        >>> d = DateEx(2010, 1, 1)
        >>> d + 1 == DateEx(2010, 1, 2)
        True

    otherwise, DateEx instance compareable with date instance::

        >>> d == date(2010, 1, 1)
        True

    """

    def __add__(self, num):
        """
        `+` operation can accept over 31 days::

            >>> d = DateEx(2010, 1, 1)
            >>> print d + 40
            2010-02-10

        and accept negative number for `+` operation::

            >>> print d + (-5)
            2009-12-27

        """
        if not isinstance(num, int):
            raise RuntimeError('add() accept only int')

        return date.__add__(self, timedelta(days=num))

    def __sub__(self, num):
        """
        DateEx accept - operation::

            >>> d = DateEx(2010, 1, 1)
            >>> d - 5 == date(2009, 12, 27)
            True
        """
        return self + (num * -1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

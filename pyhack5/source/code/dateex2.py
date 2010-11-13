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

    DateEx accept `>>` and `<<` operation for shift some month::

        >>> d >> 1
        DateEx(2010, 2, 1)

        >>> d << 2
        DateEx(2009, 11, 1)

    """

    def __add__(self, num):
        """
        `+` operation can accept over 31 days::

            >>> d = DateEx(2010, 1, 1)
            >>> d + 40
            DateEx(2010, 2, 10)

        and accept negative number for `+` operation::

            >>> d + (-5)
            DateEx(2009, 12, 27)

        if you send timedelta object instead of int, it's work too.

            >>> from datetime import timedelta
            >>> d + timedelta(days=5)
            DateEx(2010, 1, 6)

        """
        if isinstance(num, int):
            d = self + timedelta(days=num)
        elif isinstance(num, timedelta):
            d = date.__add__(self, num)

        return self.__class__.fromordinal(d.toordinal())

    def __sub__(self, num):
        """
        DateEx accept - operation::

            >>> d = DateEx(2010, 1, 1)
            >>> d - 5 == date(2009, 12, 27)
            True
        """
        return self + (num * -1)

    def __rshift__(self, num):
        """
        DateEx accept `>>` operation for shift some month::

            >>> d = DateEx(2010, 1, 1)
            >>> d >> 1
            DateEx(2010, 2, 1)
        """
        y = self.year
        m = self.month
        m += num
        if 1 <= m <= 12:
            pass
        else:
            m -= 1
            y += m / 12
            m = m % 12
            m += 1
        return self.replace(year=y, month=m)

    def __lshift__(self, num):
        """
        DateEx accept `<<` operation for shift some month::

            >>> d = DateEx(2010, 1, 1)
            >>> d << 2
            DateEx(2009, 11, 1)
        """
        return self >> (num * -1)

    def to(self, d):
        """
        iterate from self (as start day) to end day `d`

            >>> start = DateEx(2010, 1, 1)
            >>> end = DateEx(2010, 1, 4)
            >>> for x in start.to(end):
            ...     print x
            2010-01-01
            2010-01-02
            2010-01-03

        """
        for o in range(self.toordinal(), d.toordinal()):
            yield date.fromordinal(o)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

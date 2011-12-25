# -*- coding: utf-8 -*-

def add(x, y):
    """
    関数 :func:`add` は引数2つをうけとり、足した値を返します。

        >>> add(1, 2)
        3

    数値以外にも文字列も足すことが出来ます。

        >>> add('foo', 'bar')
        'foobar'

    """
    return x + y

if __name__ == '__main__':
    import doctest
    doctest.testmod()



# -*- coding: utf-8 -*-

class A(object):
    """My Class
    """

    #: This is attribute document
    #:
    #: type of `abc` is integer.
    abc = 1

    def upper_name(self, name):
        """
        upper_name accept name argument and ...

        :param str name: your name
        :return: upper case your name
        :rtype: str
        """
        return name.upper()

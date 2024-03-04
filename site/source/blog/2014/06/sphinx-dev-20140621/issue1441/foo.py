"""foo module

.. autosummary::

   outer
   outer.meth
   outer.inner

"""

class outer(object):
    "outer class"

    def meth(self):
        "this is outer.meth"
        return 1

    class inner(object):
        "inner class"

        def meth(self):
            """this is outer.inner.meth

            some description for *meth* method.
            """
            return 1

# Python 3.14.4 final / core and builtins / structures

[gh-146615](https://github.com/python/cpython/issues/146615): Stop a crash in [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__) for [METH_METHOD](https://docs.python.org/3.14/c-api/structures.html#c.METH_METHOD) descriptors triggered when an invalid (non-type) object arrives as the second argument. Steven Sun wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

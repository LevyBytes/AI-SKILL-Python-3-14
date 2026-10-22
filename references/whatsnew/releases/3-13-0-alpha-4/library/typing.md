# Python 3.13.0 alpha 4 / library / typing

[gh-115165](https://github.com/python/cpython/issues/115165): When setting the `__orig_class__` attribute on the objects returned from calling [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) generic aliases (those built via [`typing.Annotated`](https://docs.python.org/3.14/library/typing.html#typing.Annotated) included), nearly all exceptions are now swallowed. Formerly just [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) was swallowed. Dave Shawley contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

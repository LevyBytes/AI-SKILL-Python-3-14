# Python 3.14.4 final / library / float

[gh-145633](https://github.com/python/cpython/issues/145633): Corrects `struct.pack('f', float)`: it now relies on [`PyFloat_Pack4()`](https://docs.python.org/3.14/c-api/float.html#c.PyFloat_Pack4) to raise [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError). Sergey B Kirpichev and Victor Stinner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

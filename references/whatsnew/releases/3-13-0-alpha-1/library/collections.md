# Python 3.13.0 alpha 1 / library / collections

[gh-105736](https://github.com/python/cpython/issues/105736): Brought the pure Python [`OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict) into line with the C version. From now on both versions establish their internal state inside `__new__`. Earlier the pure Python version handled that set up within `__init__`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

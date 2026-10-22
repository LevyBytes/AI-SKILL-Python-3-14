# Python 3.14.5 release candidate 1 / core and builtins / marshal

[gh-148653](https://github.com/python/cpython/issues/148653): Disallow [`marshalling`](https://docs.python.org/3.14/library/marshal.html#module-marshal) of recursive code objects and of [`slice`](https://docs.python.org/3.14/library/functions.html#slice) objects that cannot later be unmarshalled correctly.

[gh-148418](https://github.com/python/cpython/issues/148418): Close a potential reference leak triggered by a corrupted `TYPE_CODE` marshal stream.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

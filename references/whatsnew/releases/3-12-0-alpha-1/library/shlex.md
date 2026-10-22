# Python 3.12.0 alpha 1 / library / shlex

[gh-94352](https://github.com/python/cpython/issues/94352): [`shlex.split()`](https://docs.python.org/3.14/library/shlex.html#shlex.split): Handing `None` to the *s* argument now throws an exception instead of reading [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin). This behaviour was deprecated in Python 3.9. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

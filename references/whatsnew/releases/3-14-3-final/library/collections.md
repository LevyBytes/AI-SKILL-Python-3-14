# Python 3.14.3 final / library / collections

[gh-143004](https://github.com/python/cpython/issues/143004): A potential use-after-free in [`collections.Counter.update()`](https://docs.python.org/3.14/library/collections.html#collections.Counter.update), arising when user code mutates the Counter mid-update, is now fixed.

[gh-142495](https://github.com/python/cpython/issues/142495): When pulling default values out of `default_factory`, [`collections.defaultdict`](https://docs.python.org/3.14/library/collections.html#collections.defaultdict) now gives precedence to [`__setitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setitem__) during insertion. The effect is to close a race window in which the default would clobber a value already stored before `default_factory` had returned.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

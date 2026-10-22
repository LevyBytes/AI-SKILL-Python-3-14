# Python 3.14.1 final / library / collections

[gh-140911](https://github.com/python/cpython/issues/140911): [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections): the `UserString.rindex()` and `UserString.index()` methods now take [`collections.UserString`](https://docs.python.org/3.14/library/collections.html#collections.UserString) instances for their sub argument.

[gh-125996](https://github.com/python/cpython/issues/125996): Repair the thread safety of [`collections.OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict). Kumar Aditya supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

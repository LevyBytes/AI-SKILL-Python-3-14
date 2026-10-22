# What's New In Python 3.13 / array — array, collections.abc

### array

- Add the `'w'` type code (`Py_UCS4`) covering Unicode characters. Prefer it over the now-deprecated `'u'` type code. (Contributed by Inada Naoki in [gh-80480](https://github.com/python/cpython/issues/80480).)

- Register [`array.array`](https://docs.python.org/3.14/library/array.html#array.array) as a [`MutableSequence`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.MutableSequence) by way of supplying the [`clear()`](https://docs.python.org/3.14/library/array.html#array.array.clear) method. (Contributed by Mike Zimin in [gh-114894](https://github.com/python/cpython/issues/114894).)

[Subject index](INDEX.md) · [Previous source section](argparse.md) · [Next source section](ast.md) · [Release/subject declaration](summary-release-highlights.md)

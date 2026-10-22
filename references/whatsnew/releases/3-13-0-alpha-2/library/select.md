# Python 3.13.0 alpha 2 / library / select

[gh-111233](https://github.com/python/cpython/issues/111233): Correct [`select`](https://docs.python.org/3.14/library/select.html#module-select) failing to check for errors at initialization.

[gh-110395](https://github.com/python/cpython/issues/110395): Guarantee that [`select.kqueue()`](https://docs.python.org/3.14/library/select.html#select.kqueue) objects show up as closed inside forked children, so that nothing operates on an invalid file descriptor.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

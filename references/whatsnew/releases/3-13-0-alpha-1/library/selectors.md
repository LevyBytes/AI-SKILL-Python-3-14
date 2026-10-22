# Python 3.13.0 alpha 1 / library / selectors

[gh-106751](https://github.com/python/cpython/issues/106751): [`selectors`](https://docs.python.org/3.14/library/selectors.html#module-selectors): Streamline the `EpollSelector.select()` code, shifting a portion of it out of the loop.

[gh-106664](https://github.com/python/cpython/issues/106664): [`selectors`](https://docs.python.org/3.14/library/selectors.html#module-selectors): Introduce a `_SelectorMapping.get()` method and tune `_SelectorMapping.__getitem__()`.

[gh-106554](https://github.com/python/cpython/issues/106554): [`selectors`](https://docs.python.org/3.14/library/selectors.html#module-selectors): Trim Selector overhead by relying on a `dict.get()` to look up file descriptors.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

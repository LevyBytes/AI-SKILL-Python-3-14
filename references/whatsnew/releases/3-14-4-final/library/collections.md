# Python 3.14.4 final / library / collections

[gh-145492](https://github.com/python/cpython/issues/145492): Corrects infinite recursion within [`collections.defaultdict`](https://docs.python.org/3.14/library/collections.html#collections.defaultdict) `__repr__` whenever a `defaultdict` holds itself. Built upon analysis from KowalskiThomas in [gh-145492](https://github.com/python/cpython/issues/145492).

[gh-144809](https://github.com/python/cpython/issues/144809): Makes [`collections.deque`](https://docs.python.org/3.14/library/collections.html#collections.deque) copy atomic throughout the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

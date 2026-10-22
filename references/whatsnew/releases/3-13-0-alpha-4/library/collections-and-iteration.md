# Python 3.13.0 alpha 4 / library / collections and iteration

[gh-101438](https://github.com/python/cpython/issues/101438): Eliminate a reference cycle within ElementTree.iterparse. The iterator that `ElementTree.iterparse` returns can retain a file descriptor. That reference cycle blocked timely clean-up of the descriptor whenever the returned iterator went unexhausted.

[gh-114149](https://github.com/python/cpython/issues/114149): Enum: properly deal with tuple subclasses inside a custom `__new__`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

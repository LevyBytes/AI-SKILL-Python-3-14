# Python 3.12.0 alpha 1 / library / exceptions and tracebacks

[gh-97928](https://github.com/python/cpython/issues/97928): `tkinter.Text.count()` now raises an exception on options that begin with "-" rather than quietly ignoring them.

[gh-83658](https://github.com/python/cpython/issues/83658): Have `multiprocessing.Pool` throw an exception whenever `maxtasksperchild` is something other than `None` or a positive int.

[gh-86388](https://github.com/python/cpython/issues/86388): Took out the randrange() behaviour that had been deprecated since Python 3.10. Previously randrange(10.0) would convert losslessly into randrange(10); it now throws a TypeError. The exception thrown for non-integral inputs like randrange(10.5) or randrange(‘10’) likewise switched from ValueError to TypeError.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

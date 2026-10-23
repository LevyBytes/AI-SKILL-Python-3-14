# What's New In Python 3.4 / functools - functools

### functools

The new [`partialmethod()`](https://docs.python.org/3.14/library/functools.html#functools.partialmethod) descriptor extends partial argument application to descriptors, much as [`partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) does for ordinary callables. This descriptor also smooths the path to making arbitrary callables (including `partial()` instances) act like ordinary instance methods once placed in a class definition. (Contributed by Alon Horev and Nick Coghlan in [bpo-4331](https://bugs.python.org/issue?@action=redirect&bpo=4331).)

The new [`singledispatch()`](https://docs.python.org/3.14/library/functools.html#functools.singledispatch) decorator brings the standard library support for generic functions that dispatch on a single argument. Whereas an object oriented style bundles many operations over one shared set of data inside a class, a generic function instead bundles many implementations of a single operation so it can handle *different* kinds of data.

See also

[**PEP 443**](https://peps.python.org/pep-0443/) ? Single-dispatch generic functions

PEP written and implemented by ?ukasz Langa.

[`total_ordering()`](https://docs.python.org/3.14/library/functools.html#functools.total_ordering) now copes with a return value of [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) coming from the underlying comparison function. (Contributed by Katie Miller in [bpo-10042](https://bugs.python.org/issue?@action=redirect&bpo=10042).)

A pure-python rendering of the [`partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) function now lives in the stdlib; under CPython the C accelerated version supersedes it, yet other implementations are free to draw on it. (Contributed by Brian Thorne in [bpo-12428](https://bugs.python.org/issue?@action=redirect&bpo=12428).)

[Subject index](INDEX.md) · [Previous source section](filecmp.md) · [Next source section](gc.md) · [Release/subject declaration](release-highlights.md)

# Python 3.13.0 alpha 5 / library / functions

[gh-116600](https://github.com/python/cpython/issues/116600): Repair [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) for global [`Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag) members.

[gh-72249](https://github.com/python/cpython/issues/72249): The [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) of [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) objects now always carries the [module](https://docs.python.org/3.14/glossary.html#term-module) name. Furkan Onder and Anilyka Barry contributed the patch.

[gh-115618](https://github.com/python/cpython/issues/115618): Repair the improper decrease of the reference count for the `None` argument across the [`property`](https://docs.python.org/3.14/library/functions.html#property) methods [`getter()`](https://docs.python.org/3.14/library/functions.html#property.getter), [`setter()`](https://docs.python.org/3.14/library/functions.html#property.setter) and [`deleter()`](https://docs.python.org/3.14/library/functions.html#property.deleter).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

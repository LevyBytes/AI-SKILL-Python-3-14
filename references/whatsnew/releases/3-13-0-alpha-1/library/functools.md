# Python 3.13.0 alpha 1 / library / functools

[gh-109653](https://github.com/python/cpython/issues/109653): Better the import time of [`functools`](https://docs.python.org/3.14/library/functools.html#module-functools) by roughly 13%. Alex Waygood authored the patch.

[bpo-40988](https://bugs.python.org/issue?@action=redirect&bpo=40988): Made [`functools.singledispatchmethod`](https://docs.python.org/3.14/library/functools.html#functools.singledispatchmethod) faster by caching the dispatch wrapper it generates. frederico suggested the optimization. @mental32, Alex Waygood and Pieter Eendebak authored the patch.

[gh-107995](https://github.com/python/cpython/issues/107995): On instances of [`functools.cached_property`](https://docs.python.org/3.14/library/functools.html#functools.cached_property), the `__module__` attribute is now assigned the name of the module that defines the cached_property, rather than “functools”. Consequently the doctests sitting in `cached_property` docstrings are now gathered correctly by the [`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest) module. Tyler Smart authored the patch.

[gh-106292](https://github.com/python/cpython/issues/106292): Look for an instance-dict cached value within the `__get__()` method of [`functools.cached_property()`](https://docs.python.org/3.14/library/functools.html#functools.cached_property). This lines up more closely with the pre-3.12 behavior and helps anyone subclassing `functools.cached_property()` and tacking on a `__set__()` method.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

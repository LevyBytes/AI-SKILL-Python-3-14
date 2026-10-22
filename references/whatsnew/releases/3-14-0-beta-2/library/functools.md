# Python 3.14.0 beta 2 / library / functools

[gh-132641](https://github.com/python/cpython/issues/132641): Repaired a race within [`functools.lru_cache()`](https://docs.python.org/3.14/library/functools.html#functools.lru_cache) under free-threading.

[gh-125028](https://github.com/python/cpython/issues/125028): [`functools.Placeholder`](https://docs.python.org/3.14/library/functools.html#functools.Placeholder) may not be handed to [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) as a keyword argument.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

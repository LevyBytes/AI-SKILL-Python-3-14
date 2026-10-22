# Python 3.11.0 alpha 3 / library / sys

[bpo-45703](https://bugs.python.org/issue?@action=redirect&bpo=45703): Suppose a namespace package is imported before some other module belonging to the same namespace gets created or installed at a different [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) spot while the program runs; invoking the [`importlib.invalidate_caches()`](https://docs.python.org/3.14/library/importlib.html#importlib.invalidate_caches) function will now also ensure the new module is detected.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

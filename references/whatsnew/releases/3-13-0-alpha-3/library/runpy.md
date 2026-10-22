# Python 3.13.0 alpha 3 / library / runpy

[gh-99437](https://github.com/python/cpython/issues/99437): Path-like objects are now decoded by [`runpy.run_path()`](https://docs.python.org/3.14/library/runpy.html#runpy.run_path), guaranteeing that the running module's __file__ and sys.argv[0] are always strings.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.11.0 alpha 1 / library / importlib

[bpo-43392](https://bugs.python.org/issue?@action=redirect&bpo=43392): To skip locking once a module is already loaded and ready, `importlib._bootstrap._find_and_load()` now performs a two-step check. Repeated invocations of [`importlib.import_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.import_module) and [`importlib.__import__()`](https://docs.python.org/3.14/library/importlib.html#importlib.__import__) therefore run faster.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

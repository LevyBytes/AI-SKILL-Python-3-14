# What’s New In Python 3.5 / sys - sys

### sys

Through a new `set_coroutine_wrapper()` function you can install a global hook that fires each time an [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) function produces a [coroutine object](https://docs.python.org/3.14/glossary.html#term-coroutine). The matching `get_coroutine_wrapper()` retrieves whatever wrapper is presently installed. Both are [provisional](https://docs.python.org/3.14/glossary.html#term-provisional-API) and serve debugging needs alone. Yury Selivanov contributed this (see [bpo-24017](https://bugs.python.org/issue?@action=redirect&bpo=24017)).

To test whether the Python interpreter is [shutting down](https://docs.python.org/3.14/glossary.html#term-interpreter-shutdown), you can call the new [`is_finalizing()`](https://docs.python.org/3.14/library/sys.html#sys.is_finalizing) function. Antoine Pitrou landed this (see [bpo-22696](https://bugs.python.org/issue?@action=redirect&bpo=22696)).

[Subject index](INDEX.md) · [Previous source section](subprocess.md) · [Next source section](sysconfig.md) · [Release/subject declaration](summary-release-highlights.md)

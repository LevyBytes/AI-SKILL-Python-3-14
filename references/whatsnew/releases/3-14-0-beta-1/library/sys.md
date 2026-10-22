# Python 3.14.0 beta 1 / library / sys

[gh-128384](https://github.com/python/cpython/issues/128384): When the [`sys.flags.context_aware_warnings`](https://docs.python.org/3.14/library/sys.html#sys.flags.context_aware_warnings) flag is true, [`warnings.catch_warnings`](https://docs.python.org/3.14/library/warnings.html#warnings.catch_warnings) now keeps the warning-filtering state in a context variable. That renders the context manager safe to use across threads in multi-threaded code. By default the flag is true in free-threaded builds and false elsewhere. To override its value, use the [`-X context_aware_warnings`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command-line option or the [`PYTHON_CONTEXT_AWARE_WARNINGS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_CONTEXT_AWARE_WARNINGS) environment variable.

[gh-129027](https://github.com/python/cpython/issues/129027): [`sys._clear_type_cache()`](https://docs.python.org/3.14/library/sys.html#sys._clear_type_cache) now triggers a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Although deprecated back in Python 3.13, it had not been emitting a warning at runtime.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

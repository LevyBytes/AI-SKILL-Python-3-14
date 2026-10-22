# Python 3.8.0 beta 1 / tests / test

[bpo-37069](https://bugs.python.org/issue?@action=redirect&bpo=37069): Reworks test_coroutines, test_cprofile, test_generators, test_raise, test_ssl and test_yield_from to lean on [`test.support.catch_unraisable_exception()`](https://docs.python.org/3.14/library/test.html#test.support.catch_unraisable_exception) in place of [`test.support.captured_stderr()`](https://docs.python.org/3.14/library/test.html#test.support.captured_stderr).

[bpo-36829](https://bugs.python.org/issue?@action=redirect&bpo=36829): Adds [`test.support.catch_unraisable_exception()`](https://docs.python.org/3.14/library/test.html#test.support.catch_unraisable_exception): a context manager that captures an unraisable exception by way of [`sys.unraisablehook()`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

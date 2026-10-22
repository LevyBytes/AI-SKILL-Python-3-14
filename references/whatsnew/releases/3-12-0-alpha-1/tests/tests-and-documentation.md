# Python 3.12.0 alpha 1 / tests / tests and documentation

[gh-96624](https://github.com/python/cpython/issues/96624): Repaired the breakage of repeated `test.test_unittest` runs that side effects in `test_dotted_but_module_not_loaded` were causing.

[gh-94208](https://github.com/python/cpython/issues/94208): More of the `test_ssl` tests now verify supported TLS version and protocols.

[gh-84461](https://github.com/python/cpython/issues/84461): `run_tests.py` now deals with cross compiling env vars properly and forwards `HOSTRUNNER` to the regression tests.

[gh-57539](https://github.com/python/cpython/issues/57539): Broaden calendar test coverage of `calendar.LocaleTextCalendar.formatweekday()`.

[gh-92886](https://github.com/python/cpython/issues/92886): Repairing tests within `test_imaplib.py` that break under optimizations (`-O`).

[gh-92886](https://github.com/python/cpython/issues/92886): Repairing tests within `test_zipimport.py` that break under optimizations (`-O`)

[gh-92886](https://github.com/python/cpython/issues/92886): Repairing tests within `test_py_compile.py` that break under optimizations (`-O`)

[gh-92886](https://github.com/python/cpython/issues/92886): Repairing tests within `test_sys_settrace.py` that break under optimizations (`-O`).

[gh-92886](https://github.com/python/cpython/issues/92886): Repairing tests within `_test_multiprocessing.py` that break under optimizations (`-O`)

[gh-92514](https://github.com/python/cpython/issues/92514): Delete the unused `test.support.BasicTestRunner`. Jelle Zijlstra wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

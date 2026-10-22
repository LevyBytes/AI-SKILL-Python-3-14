# Python 3.13.0 alpha 1 / tests / imports and modules

[gh-108388](https://github.com/python/cpython/issues/108388): Turned test_concurrent_futures into a package holding 7 sub-tests. Victor Stinner authored the patch.

[gh-106752](https://github.com/python/cpython/issues/106752): Relocated the tests for `zipfile.Path` into `Lib/test/test_zipfile/_path`. Turned `zipfile._path` into a package.

[gh-106690](https://github.com/python/cpython/issues/106690): Added a .coveragerc into the cpython repository for use alongside the coverage package.

[gh-109230](https://github.com/python/cpython/issues/109230): Repaired `test_pyexpat.test_exception()`: running it from a directory other than the Python source code directory now works. Before, this scenario broke the test. Omit the test when the Modules/pyexpat.c source is missing. Omit it as well on Python implementations besides CPython. Victor Stinner authored the patch.

[gh-109972](https://github.com/python/cpython/issues/109972): Broke the test_gdb.py file apart into a test_gdb package composed of several tests, which lets the tests run concurrently now. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

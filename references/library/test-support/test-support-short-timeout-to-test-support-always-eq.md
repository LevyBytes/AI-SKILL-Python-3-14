# test.support`test.support` - Utilities for the Python test suite

test.support.SHORT_TIMEOUT

Timeout, in seconds, after which a test is failed for taking “too long”.

What the timeout works out to hinges on the regrtest `--timeout` command line option.

Should a test relying on `SHORT_TIMEOUT` begin failing intermittently on sluggish buildbots, switch to `LONG_TIMEOUT`.

Its default value is 30 seconds.

 test.support.LONG_TIMEOUT

Timeout, in seconds, used to catch a hanging test.

It runs long enough to lower the chance of test failure on Python's slowest buildbots. Do not use it to fail a test that runs “too long”. What the timeout works out to hinges on the regrtest `--timeout` command line option.

Its default value is 5 minutes.

See also `LOOPBACK_TIMEOUT`, `INTERNET_TIMEOUT` and `SHORT_TIMEOUT`.

 test.support.PGO

Set when tests can be skipped because they offer no value for PGO.

 test.support.PIPE_MAX_SIZE

A constant chosen to exceed the underlying OS pipe buffer size, so that writes block.

 test.support.Py_DEBUG

`True` when Python was compiled with the [`Py_DEBUG`](https://docs.python.org/3.14/c-api/intro.html#c.Py_DEBUG) macro defined—in other words, when Python was [built in debug mode](https://docs.python.org/3.14/using/configure.html#debug-build).

Added in version 3.12.

 test.support.SOCK_MAX_SIZE

A constant chosen to exceed the underlying OS socket buffer size, so that writes block.

 test.support.TEST_SUPPORT_DIR

Set to the top level directory that contains `test.support`.

 test.support.TEST_HOME_DIR

Set to the top level directory for the test package.

 test.support.TEST_DATA_DIR

Set to the `data` directory within the test package.

 test.support.MAX_Py_ssize_t

Set to [`sys.maxsize`](https://docs.python.org/3.14/library/sys.html#sys.maxsize) for big memory tests.

 test.support.max_memuse

The memory ceiling for big memory tests, set by `set_memlimit()`. Bounded by `MAX_Py_ssize_t`.

 test.support.real_max_memuse

The memory ceiling for big memory tests, set by `set_memlimit()`. Not bounded by `MAX_Py_ssize_t`.

 test.support.MISSING_C_DOCSTRINGS

Set to `True` when Python is compiled without docstrings (that is, when the `WITH_DOC_STRINGS` macro is left undefined). See the [`configure --without-doc-strings`](https://docs.python.org/3.14/using/configure.html#cmdoption-without-doc-strings) option.

See also the `HAVE_DOCSTRINGS` variable.

 test.support.HAVE_DOCSTRINGS

Set to `True` when function docstrings can be accessed. See the [`python -OO`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-O) option, which removes docstrings from functions written in Python.

See also the `MISSING_C_DOCSTRINGS` variable.

 test.support.TEST_HTTP_URL

Define the URL of a dedicated HTTP server for the network tests.

 test.support.ALWAYS_EQ

Object that is equal to anything. Used to test mixed type comparison.

[Subject index](INDEX.md) · [Previous](test-support-testfailed-to-test-support-internet-timeout.md) · [Continue](test-support-never-eq-to-test-support-with-pymalloc.md) · [Owning module, declaration or section: test.support](test-support-testfailed-to-test-support-internet-timeout.md)

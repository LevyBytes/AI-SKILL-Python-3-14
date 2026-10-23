# test.support`test.support` - Utilities for the Python test suite

### `test.support` - Utilities for the Python test suite

Support for Python's regression test suite comes from the `test.support` module.

Note

`test.support` is not a public module. The documentation here exists to assist Python developers in writing tests. Expect this module's API to change between releases with no concern for backwards compatibility.

The exceptions this module declares are:

 *exception *test.support.TestFailed

The exception raised on a failing test. Its use is deprecated in favor of [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest)-based tests together with the assertion methods of [`unittest.TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase).

 *exception *test.support.ResourceDenied

A subclass of [`unittest.SkipTest`](https://docs.python.org/3.14/library/unittest.html#unittest.SkipTest). It is raised whenever a resource (a network connection, say) cannot be reached. The `requires()` function raises it.

The `test.support` module declares the constants below:

 test.support.verbose

`True` whenever verbose output has been turned on. Consult it when a running test calls for fuller detail. `test.regrtest` sets *verbose*.

 test.support.is_jython

`True` if the running interpreter is Jython.

 test.support.is_android

`True` if `sys.platform` is `android`.

 test.support.is_emscripten

`True` if `sys.platform` is `emscripten`.

 test.support.is_wasi

`True` if `sys.platform` is `wasi`.

 test.support.is_apple_mobile

`True` if `sys.platform` is `ios`, `tvos`, or `watchos`.

 test.support.is_apple

`True` if `sys.platform` is `darwin` or `is_apple_mobile` is `True`.

 test.support.unix_shell

Path for shell if not on Windows; otherwise `None`.

 test.support.LOOPBACK_TIMEOUT

Timeout, in seconds, for tests relying on a network server that listens on the local loopback interface, such as `127.0.0.1`.

This timeout is generous enough to avoid spurious test failure: it allows for the client and the server running in separate threads, or even separate processes.

It should give enough headroom for the [`connect()`](https://docs.python.org/3.14/library/socket.html#socket.socket.connect), [`recv()`](https://docs.python.org/3.14/library/socket.html#socket.socket.recv) and [`send()`](https://docs.python.org/3.14/library/socket.html#socket.socket.send) methods of [`socket.socket`](https://docs.python.org/3.14/library/socket.html#socket.socket).

Its default value is 5 seconds.

See also `INTERNET_TIMEOUT`.

 test.support.INTERNET_TIMEOUT

Timeout, in seconds, for network requests reaching out to the internet.

This timeout is brief enough to keep a test from waiting overly long when an internet request is blocked for any reason.

As a rule, a timeout reached via `INTERNET_TIMEOUT` ought to skip the test rather than fail it: see `transient_internet()`.

Its default value is 1 minute.

See also `LOOPBACK_TIMEOUT`.

[Subject index](INDEX.md) · [Previous](../test/running-tests-using-the-command-line-interface.md) · [Continue](test-support-short-timeout-to-test-support-always-eq.md)

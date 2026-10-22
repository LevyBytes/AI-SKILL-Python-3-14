# What's new in Python 3.14 / Build changes — ctypes, fcntl, termios

### Build changes

- [**PEP 776**](https://peps.python.org/pep-0776/): Emscripten now carries official support as a platform at [**tier 3**](https://peps.python.org/pep-0011/#tier-3). During that work, upwards of 25 defects in [Emscripten libc](https://emscripten.org/docs/porting/emscripten-runtime-environment.html) were corrected. Emscripten now ships support for [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes), [`termios`](https://docs.python.org/3.14/library/termios.html#module-termios), and [`fcntl`](https://docs.python.org/3.14/library/fcntl.html#module-fcntl), plus experimental coverage of the new [default interactive shell](https://docs.python.org/3.14/tutorial/interpreter.html#tut-interactive). (Contributed by R. Hood Chatham in [gh-127146](https://github.com/python/cpython/issues/127146), [gh-127683](https://github.com/python/cpython/issues/127683), and [gh-136931](https://github.com/python/cpython/issues/136931).)

- Official Android binary releases are now provided on [python.org](https://www.python.org/downloads/android/).

- Generating `configure` now demands GNU Autoconf 2.72. (Contributed by Erlend Aasland in [gh-115765](https://github.com/python/cpython/issues/115765).)

- Under [**PEP 11**](https://peps.python.org/pep-0011/), `wasm32-unknown-emscripten` has reached tier 3 platform standing. (Contributed by R. Hood Chatham in [gh-127146](https://github.com/python/cpython/issues/127146), [gh-127683](https://github.com/python/cpython/issues/127683), and [gh-136931](https://github.com/python/cpython/issues/136931).)

- You can now turn off `#pragma`-based linking against `python3*.lib` through [Py_NO_LINK_LIB](https://docs.python.org/3.14/extending/windows.html#c.Py_NO_LINK_LIB). (Contributed by Jean-Christophe Fillion-Robin in [gh-82909](https://github.com/python/cpython/issues/82909).)

- For better security, CPython now turns on a curated group of recommended compiler flags out of the box. Pass the [`--disable-safety`](https://docs.python.org/3.14/using/configure.html#cmdoption-disable-safety) `configure` option to switch them off, or the [`--enable-slower-safety`](https://docs.python.org/3.14/using/configure.html#cmdoption-enable-slower-safety) option to add an even broader set, at the expense of some performance.

- The `WITH_FREELISTS` macro and `--without-freelists` `configure` option have been removed.

- A fresh `configure` option, [`--with-tail-call-interp`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-tail-call-interp), can switch on the experimental tail call interpreter. Consult A new type of interpreter for more.

- If you want to drop the new remote debugging support, supply the [`--without-remote-debug`](https://docs.python.org/3.14/using/configure.html#cmdoption-without-remote-debug) `configure` option, which can help for security reasons.

- Apps on iOS and macOS can now be set up so that `stdout` and `stderr` output is routed into the system log. (Contributed by Russell Keith-Magee in [gh-127592](https://github.com/python/cpython/issues/127592).)

- While a test runs, the iOS testbed can now stream its output live. That testbed also works for running the test suites of projects beyond CPython. (Contributed by Russell Keith-Magee in [gh-127592](https://github.com/python/cpython/issues/127592).)

[Subject index](INDEX.md) · [Previous source section](c-api-unscheduled-removals.md) · [Next source section](build-details-json.md) · [Release/subject declaration](summary-release-highlights.md)

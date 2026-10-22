# What's New In Python 3.13 / Build Changes — sqlite3

### Build Changes

- Both `arm64-apple-ios` and `arm64-apple-ios-simulator` have moved up to [**PEP 11**](https://peps.python.org/pep-0011/) tier 3 platform status. (PEP 730 written and implementation contributed by Russell Keith-Magee in [gh-114099](https://github.com/python/cpython/issues/114099).)

- Both `aarch64-linux-android` and `x86_64-linux-android` have likewise reached [**PEP 11**](https://peps.python.org/pep-0011/) tier 3 platform status. (PEP 738 written and implementation contributed by Malcolm Smith in [gh-116622](https://github.com/python/cpython/issues/116622).)

- `wasm32-wasi` has been raised to a [**PEP 11**](https://peps.python.org/pep-0011/) tier 2 platform. (Contributed by Brett Cannon in [gh-115192](https://github.com/python/cpython/issues/115192).)

- `wasm32-emscripten` has dropped off the list of [**PEP 11**](https://peps.python.org/pep-0011/) supported platforms. (Contributed by Brett Cannon in [gh-115192](https://github.com/python/cpython/issues/115192).)

- To build CPython you now need a compiler that supports either the C11 atomic library, GCC's built-in atomic functions, or MSVC interlocked intrinsics.

- Regenerating the `configure` script now calls for Autoconf 2.71 together with aclocal 1.16.5. (Contributed by Christian Heimes in [gh-89886](https://github.com/python/cpython/issues/89886) and by Victor Stinner in [gh-112090](https://github.com/python/cpython/issues/112090).)

- Compiling the [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) extension module now demands SQLite 3.15.2 or a later release. (Contributed by Erlend Aasland in [gh-105875](https://github.com/python/cpython/issues/105875).)

- By default, CPython now ships with the [mimalloc library](https://github.com/microsoft/mimalloc/) included. Its license is MIT; see [mimalloc license](https://docs.python.org/3.14/license.html#mimalloc-license). This bundled mimalloc carries custom modifications, detailed in [gh-113141](https://github.com/python/cpython/issues/113141). (Contributed by Dino Viehland in [gh-109914](https://github.com/python/cpython/issues/109914).)

- For the `configure` option [`--with-system-libmpdec`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-system-libmpdec), the default is now `yes`. Python 3.16 will drop the bundled copy of `libmpdec`.

- A Python compiled with `configure` [`--with-trace-refs`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-trace-refs) (tracing references) is at last ABI compatible with both the Python release build and the [debug build](https://docs.python.org/3.14/using/configure.html#debug-build). (Contributed by Victor Stinner in [gh-108634](https://github.com/python/cpython/issues/108634).)

- Across POSIX systems, the pkg-config (`.pc`) filenames now carry the ABI flags. As an illustration, the free-threaded build produces `python-3.13t.pc` while the debug build produces `python-3.13d.pc`.

- The `errno`, `fcntl`, `grp`, `md5`, `pwd`, `resource`, `termios`, `winsound`, `_ctypes_test`, `_multiprocessing.posixshmem`, `_scproxy`, `_stat`, `_statistics`, `_testconsole`, `_testimportmultiple` and `_uuid` C extensions get compiled against the [limited C API](https://docs.python.org/3.14/c-api/stable.html#limited-c-api) from now on. (Contributed by Victor Stinner in [gh-85283](https://github.com/python/cpython/issues/85283).)

[Subject index](INDEX.md) · [Previous source section](c-api-unscheduled-removals.md) · [Next source section](porting-to-python-3-13.md) · [Release/subject declaration](summary-release-highlights.md)

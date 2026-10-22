# Python 3.12.0 alpha 6 / core and builtins / build and platforms

[gh-102336](https://github.com/python/cpython/issues/102336): Remove the special-case handling specific to Windows 7. Max Bachmann supplied the patch.

[gh-102027](https://github.com/python/cpython/issues/102027): On Windows, fall back to `GetCurrentProcessId` where `getpid` is not available. Max Bachmann supplied the patch.

[gh-101857](https://github.com/python/cpython/issues/101857): Correct xattr support detection on Linux by broadening the test to all of linux rather than glibc alone. That restores support for musl.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

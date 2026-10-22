# Python 3.12.0 beta 1 / build / build and platforms

[gh-101282](https://github.com/python/cpython/issues/101282): When a shared library is being built, BOLT optimization now extends to the libpython shared library. The `BOLT_INSTRUMENT_FLAGS` and `BOLT_APPLY_FLAGS` configure variables now let you steer BOLT's instrumentation and application settings.

[gh-104106](https://github.com/python/cpython/issues/104106): Provide a gcc fallback for mkfifoat/mknodat on macOS. Donghee Na wrote the patch.

[gh-99069](https://github.com/python/cpython/issues/99069): Broaden the workaround that supplies `static_assert` when the libc headers lack it, so it now covers every clang and gcc build. As one consequence, this repairs building on macOS <= 10.10.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

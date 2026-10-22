# Python 3.14.0 alpha 1 / build / build and platforms

[gh-125269](https://github.com/python/cpython/issues/125269): Correct how the configure script decides whether `-latomic` is required during a cross-compile of CPython.

[gh-123990](https://github.com/python/cpython/issues/123990): Drop the `WITH_FREELISTS` macro alongside the `--without-freelists` build configuration

[gh-124102](https://github.com/python/cpython/issues/124102): Refresh the in-tree notes beneath PCbuild so that they now accurately note Windows needing VS2017 or later plus Python 3.10 or later

[gh-123418](https://github.com/python/cpython/issues/123418): The Android build was moved over to OpenSSL 3.0.15.

[gh-121634](https://github.com/python/cpython/issues/121634): It is now possible to name the target compile triple when building for WASI.

[gh-121996](https://github.com/python/cpython/issues/121996): Add the ./configure --disable-safety and --enable-slower-safety switches. Donghee Na wrote the patch.

[gh-120522](https://github.com/python/cpython/issues/120522): A fresh [`--with-app-store-compliance`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-app-store-compliance) option lets you patch around documented snags in the macOS/iOS App Store review workflow.

[gh-121731](https://github.com/python/cpython/issues/121731): Repair the mimalloc compile failure seen on GNU/Hurd

[gh-120831](https://github.com/python/cpython/issues/120831): The lowest supported iOS version by default rose to 13.0.

[gh-121082](https://github.com/python/cpython/issues/121082): Resolve a build failure that occurred when a developer passed `--enable-pystats` arguments to the configuration command following #118450.

[gh-120671](https://github.com/python/cpython/issues/120671): Repair configure tests that were failing on account of a missing space while appending to CFLAGS.

[gh-120602](https://github.com/python/cpython/issues/120602): Properly cope with LLVM installations carrying `LLVM_VERSION_SUFFIX` when the build uses `--enable-experimental-jit`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

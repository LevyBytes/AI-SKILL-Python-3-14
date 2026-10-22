# Python 3.14.0 beta 1 / build / build and platforms

[gh-113464](https://github.com/python/cpython/issues/113464): Windows LLVM dependencies are now managed through the cpython-bin-deps "externals" repository. For Windows JIT builds, installing LLVM by hand is no longer required.

[gh-132649](https://github.com/python/cpython/issues/132649): On Windows ARM64, the `PClayout` script accepts the `--include-tcltk` option now.

[gh-132257](https://github.com/python/cpython/issues/132257): On GCC the default LTO flags were adjusted to stop passing `-flto-partition=none` and to permit LTO parallelization. With more recent GNU makes and GCC, this yields a several-times speedup for LTO build durations while performance shows no perceptible drop.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

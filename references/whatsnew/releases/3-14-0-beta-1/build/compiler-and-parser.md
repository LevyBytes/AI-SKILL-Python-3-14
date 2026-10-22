# Python 3.14.0 beta 1 / build / compiler and parser

[gh-133183](https://github.com/python/cpython/issues/133183): Target triples emitted by the iOS compiler shims now carry `IPHONEOS_DEPLOYMENT_TARGET`, which keeps the SDK version minimums respected.

[gh-133167](https://github.com/python/cpython/issues/133167): Repaired the compilation flow when both `--enable-optimizations` and `--without-docstrings` are in play.

[gh-133171](https://github.com/python/cpython/issues/133171): Because the experimental JIT compiler is unsupported on free-threaded builds, those two configurations can no longer be selected together.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

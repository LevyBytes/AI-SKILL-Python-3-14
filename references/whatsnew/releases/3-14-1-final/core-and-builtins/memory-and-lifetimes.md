# Python 3.14.1 final / core and builtins / memory and lifetimes

[gh-140306](https://github.com/python/cpython/issues/140306): Resolve memory leaks affecting cross-interpreter channel operations as well as shared namespace handling.

[gh-140301](https://github.com/python/cpython/issues/140301): Resolve a memory leak of `PyConfig` within subinterpreters.

[gh-140067](https://github.com/python/cpython/issues/140067): Resolve a memory leak during sub-interpreter creation.

[gh-140530](https://github.com/python/cpython/issues/140530): Resolve a reference leak that struck once `raise exc from cause` failed. Bénédikt Tran supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

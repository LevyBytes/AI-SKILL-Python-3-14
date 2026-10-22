# Python 3.14.0 beta 1 / core and builtins / jit better stripping out unused constant local variable loads issue

[gh-130415](https://github.com/python/cpython/issues/130415): The JIT is now better at stripping out unused constant and local-variable loads, and an issue is fixed in which deallocating unused values could make JIT code crash or misbehave.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.12.0 alpha 2 / core and builtins / compiler and parser

[gh-96793](https://github.com/python/cpython/issues/96793): StopIteration and StopAsyncIteration thrown inside a generator or coroutine are now caught within the bytecode itself, instead of being processed by the surrounding C code.

[gh-98686](https://github.com/python/cpython/issues/98686): Quicken every code object, and apply adaptive bytecode specialization with a heavier hand.

[gh-99298](https://github.com/python/cpython/issues/99298): Address a problem that could conceivably yield incorrect error handling for a number of bytecode instructions.

[gh-99254](https://github.com/python/cpython/issues/99254): The compiler now strips every unused constant from code objects (other than the first, which might serve as a docstring).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

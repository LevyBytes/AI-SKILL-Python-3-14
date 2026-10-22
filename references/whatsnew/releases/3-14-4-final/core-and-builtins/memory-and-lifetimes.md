# Python 3.14.4 final / core and builtins / memory and lifetimes

[gh-144872](https://github.com/python/cpython/issues/144872): Resolves a heap buffer overflow within the parser that OSS-Fuzz uncovered.

[gh-146092](https://github.com/python/cpython/issues/146092): Memory allocation failures arising on str and float opcodes are now handled correctly. Victor Stinner authored the patch.

[gh-145615](https://github.com/python/cpython/issues/145615): Plugged a memory leak inside the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build) where mimalloc pages might turn permanently unreclaimable right up until the owning thread terminated.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

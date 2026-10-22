# Python 3.14.0 alpha 6 / core and builtins / memory and lifetimes

[gh-129953](https://github.com/python/cpython/issues/129953): Whenever execution leaves the interpreter or JIT compiled code, the internal (evaluation) stack is now flushed to memory. No difference should be visible from either Python or builtin extensions, yet this paves the way for several major optimizations later on.

[gh-130794](https://github.com/python/cpython/issues/130794): A memory leak on the [free threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build that appeared when a shared list or dictionary was resized by many short-lived threads has been fixed.

[gh-124878](https://github.com/python/cpython/issues/124878): Race conditions during runtime finalization, which risked reaching freed memory, have been fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

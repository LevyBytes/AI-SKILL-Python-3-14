# Python 3.14.0 beta 2 / core and builtins / drop special casing c stack depth limits wasi

[gh-130397](https://github.com/python/cpython/issues/130397): Drop the special-casing of C stack depth limits for WASI. Because WebAssembly provides built-in stack protection, this raises no security concern.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.0 alpha 2 / build / wasi target triple wasm32 wasip1 rather than wasm32 wasi

[gh-123877](https://github.com/python/cpython/issues/123877): For WASI, the target triple is now `wasm32-wasip1` rather than `wasm32-wasi`. The older name is destined to be reserved for WASI 1.0, whereas CPython presently supports only WASI preview1.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

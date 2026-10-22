# Python 3.12.0 alpha 1 / build / resource

[gh-84461](https://github.com/python/cpython/issues/84461): The `wasm32-emscripten` platform no longer compiles the [`resource`](https://docs.python.org/3.14/library/resource.html#module-resource) module, [`getresuid()`](https://docs.python.org/3.14/library/os.html#os.getresuid), [`getresgid()`](https://docs.python.org/3.14/library/os.html#os.getresgid), or their setters. These APIs are non-functional stubs.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

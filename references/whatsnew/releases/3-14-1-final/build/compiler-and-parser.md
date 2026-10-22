# Python 3.14.1 final / build / compiler and parser

[gh-138489](https://github.com/python/cpython/issues/138489): For WASI cross-compilation driven by `build_wasm` or `build_emscripten`, the `build-details.json` step now runs as part of the build, mirroring how native builds behave.

That correction addresses the `libinstall` task, since it depends on the `build-details.json` file while it runs.

[gh-123681](https://github.com/python/cpython/issues/123681): Verify the `strftime()` behavior while the program runs rather than during compilation so that cross-compiling works. Drop the internal `_Py_NORMALIZE_CENTURY` macro.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.12.0 alpha 5 / build / build and platforms

[gh-77532](https://github.com/python/cpython/issues/77532): Small fixes that permit building with `PlatformToolset=ClangCL` on Windows.

[gh-100340](https://github.com/python/cpython/issues/100340): Permit -Wno-int-conversion for wasm-sdk 17 and later, which lets WASI builds compile once against the newest sdk.

[gh-101060](https://github.com/python/cpython/issues/101060): Add `-fno-reorder-blocks-and-partition` conditionally during configure. This in effect repairs `--enable-bolt` under Clang, since the flag turns out to be GCC-only.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.0 alpha 4 / build / gc

[gh-128627](https://github.com/python/cpython/issues/128627): On Emscripten builds the trampoline that performs the function pointer cast call now reaches for the wasm-gc ref.test instruction when present, rather than relying on Wasm JS type reflection.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

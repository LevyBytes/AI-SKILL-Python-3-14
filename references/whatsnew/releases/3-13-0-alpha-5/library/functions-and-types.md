# Python 3.13.0 alpha 5 / library / functions and types

[gh-115978](https://github.com/python/cpython/issues/115978): Switch off preadv(), readv(), pwritev(), and writev() under WASI.

On wasmtime for WASI 0.2, those functions fail test_posix ([https://github.com/bytecodealliance/wasmtime/issues/7830](https://github.com/bytecodealliance/wasmtime/issues/7830)).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

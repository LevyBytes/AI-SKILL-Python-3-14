# Python 3.14.0 alpha 2 / core and builtins / dis

[gh-125837](https://github.com/python/cpython/issues/125837): Two new instructions arrive, [`LOAD_SMALL_INT`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_SMALL_INT) and [`LOAD_CONST_IMMORTAL`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_CONST_IMMORTAL). A small integer matching the `oparg` gets pushed onto the stack by `LOAD_SMALL_INT`. Behaving like `LOAD_CONST` yet faster for immortal objects, `LOAD_CONST_IMMORTAL` handles those cases. The `RETURN_CONST` instruction is dropped.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

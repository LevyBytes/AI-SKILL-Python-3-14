# --with-assertions

--with-assertions

Compile with C assertions switched on (off by default): `assert(...);` and `_PyObject_ASSERT(...);`.

When this is set, the `OPT` compiler variable leaves the `NDEBUG` macro undefined.

Take note too of the `--with-pydebug` option (a debug build), which likewise turns assertions on.

Added in version 3.6.

[Subject index](INDEX.md) · [Previous source section](with-trace-refs.md) · [Following source section](with-valgrind.md)

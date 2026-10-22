# All interned strings are immortal

#### All interned strings are immortal

Across recent Python releases (from version 2.3 onward), interning a string — say through [`sys.intern()`](https://docs.python.org/3.14/library/sys.html#sys.intern) — doesn't render it immortal. Rather, once that string loses its final reference, it gets dropped from the interned string table. The free-threaded build behaves differently: every interned string turns immortal there and persists right up to interpreter shutdown.

[Subject index](INDEX.md) · [Previous source context](increased-memory-usage.md) · [Following source context](non-gc-objects-have-a-larger-object-header.md)

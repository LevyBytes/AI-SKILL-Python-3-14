# Python 3.12.0 alpha 1 / core and builtins / dis

[gh-95113](https://github.com/python/cpython/issues/95113): Swap every `EXTENDED_ARG_QUICK` instruction for a plain [`EXTENDED_ARG`](https://docs.python.org/3.14/library/dis.html#opcode-EXTENDED_ARG) instruction within unquickened code. Consumers of non-adaptive bytecode ought to be able to treat extended arguments just as they did in CPython 3.10 and earlier.

[gh-93911](https://github.com/python/cpython/issues/93911): Repair a problem that could keep [`LOAD_ATTR`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_ATTR) from specializing correctly while accessing properties.

[gh-97912](https://github.com/python/cpython/issues/97912): When deciding which instructions ought to take the [`LOAD_FAST_CHECK`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_FAST_CHECK) opcode, the compiler no longer behaves quadratically.

[gh-94163](https://github.com/python/cpython/issues/94163): Introduces [`BINARY_SLICE`](https://docs.python.org/3.14/library/dis.html#opcode-BINARY_SLICE) plus [`STORE_SLICE`](https://docs.python.org/3.14/library/dis.html#opcode-STORE_SLICE) instructions, which handle and specialize slicing operations more efficiently wherever the slice appears literally in the source.

[gh-91432](https://github.com/python/cpython/issues/91432): Specialized the [`FOR_ITER`](https://docs.python.org/3.14/library/dis.html#opcode-FOR_ITER) opcode by way of the PEP 659 machinery

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

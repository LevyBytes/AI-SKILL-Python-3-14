# Python 3.12.0 alpha 2 / core and builtins / dis

[gh-96793](https://github.com/python/cpython/issues/96793): Introduce a specialized form of [`FOR_ITER`](https://docs.python.org/3.14/library/dis.html#opcode-FOR_ITER) for generators. This trims several dispatch and check layers between the `FOR_ITER` instruction at the call site and the [`RESUME`](https://docs.python.org/3.14/library/dis.html#opcode-RESUME) within the generator.

[gh-96793](https://github.com/python/cpython/issues/96793): On loop termination, [`FOR_ITER`](https://docs.python.org/3.14/library/dis.html#opcode-FOR_ITER) now keeps the iterator sitting on the stack. The goal here is to make specializing generator loops easier.

[gh-98686](https://github.com/python/cpython/issues/98686): Fold the adaptive opcode logic into every instruction's unquickened variant, and fold what `EXTENDED_ARG_QUICK` did into [`EXTENDED_ARG`](https://docs.python.org/3.14/library/dis.html#opcode-EXTENDED_ARG). After these changes, the quickening performed at code object creation handles only the initialization of warmup counters and the insertion of superinstructions.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

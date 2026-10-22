# Python 3.12.0 alpha 1 / library / dis

[gh-92932](https://github.com/python/cpython/issues/92932): Both [`dis()`](https://docs.python.org/3.14/library/dis.html#dis.dis) and [`get_instructions()`](https://docs.python.org/3.14/library/dis.html#dis.get_instructions) now cope with operand values on instructions that carry an `EXTENDED_ARG_QUICK` prefix. Sam Gross and Donghee Na supplied the patch.

[gh-94216](https://github.com/python/cpython/issues/94216): The [`dis`](https://docs.python.org/3.14/library/dis.html#module-dis) module now carries opcodes for pseudo instructions (the ones the compiler relies on during code generation but later strips out or swaps for real opcodes before final bytecode emission).

[gh-91389](https://github.com/python/cpython/issues/91389): Address a problem where [`dis`](https://docs.python.org/3.14/library/dis.html#module-dis) helpers might emit absent or wrong position data whenever `CACHE` entries were present.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

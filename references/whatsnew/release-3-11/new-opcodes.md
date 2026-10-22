# What's New In Python 3.11 / New opcodes — dis

### New opcodes

- `ASYNC_GEN_WRAP`, [`RETURN_GENERATOR`](https://docs.python.org/3.14/library/dis.html#opcode-RETURN_GENERATOR) and [`SEND`](https://docs.python.org/3.14/library/dis.html#opcode-SEND), applied within generators and co-routines.

- [`COPY_FREE_VARS`](https://docs.python.org/3.14/library/dis.html#opcode-COPY_FREE_VARS), which removes the need for dedicated caller-side handling of closures.

- [`JUMP_BACKWARD_NO_INTERRUPT`](https://docs.python.org/3.14/library/dis.html#opcode-JUMP_BACKWARD_NO_INTERRUPT), meant for particular loops in which servicing interrupts is unwanted.

- [`MAKE_CELL`](https://docs.python.org/3.14/library/dis.html#opcode-MAKE_CELL), which builds [Cell Objects](https://docs.python.org/3.14/c-api/cell.html#cell-objects).

- [`CHECK_EG_MATCH`](https://docs.python.org/3.14/library/dis.html#opcode-CHECK_EG_MATCH) and `PREP_RERAISE_STAR`, supporting the freshly-added exception groups and except* from [**PEP 654**](https://peps.python.org/pep-0654/).

- [`PUSH_EXC_INFO`](https://docs.python.org/3.14/library/dis.html#opcode-PUSH_EXC_INFO), employed inside exception handlers.

- [`RESUME`](https://docs.python.org/3.14/library/dis.html#opcode-RESUME), a no-op serving internal tracing, debugging and optimization checks.

[Subject index](INDEX.md) · [Previous source section](cpython-bytecode-changes.md) · [Next source section](replaced-opcodes.md) · [Release/subject declaration](summary-release-highlights.md)

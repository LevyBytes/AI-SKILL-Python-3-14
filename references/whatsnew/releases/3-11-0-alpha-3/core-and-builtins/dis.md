# Python 3.11.0 alpha 3 / core and builtins / dis

[bpo-44525](https://bugs.python.org/issue?@action=redirect&bpo=44525): Introduces a fresh [`COPY_FREE_VARS`](https://docs.python.org/3.14/library/dis.html#opcode-COPY_FREE_VARS) opcode, making the copying of free variables from function into frame explicit. This aids optimization of calls into Python functions.

[bpo-45636](https://bugs.python.org/issue?@action=redirect&bpo=45636): Streamline the [`BINARY_OP`](https://docs.python.org/3.14/library/dis.html#opcode-BINARY_OP) implementation by indexing an array of function pointers, rather than dispatching via a switch on the oparg.

[bpo-45636](https://bugs.python.org/issue?@action=redirect&bpo=45636): Swap every numeric `BINARY_*` and `INPLACE_*` instruction for one unified [`BINARY_OP`](https://docs.python.org/3.14/library/dis.html#opcode-BINARY_OP) implementation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

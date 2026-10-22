# Python 3.11.0 alpha 5 / core and builtins / dis

[bpo-46528](https://bugs.python.org/issue?@action=redirect&bpo=46528): A number of stack-shuffling opcodes (`DUP_TOP`, `DUP_TOP_TWO`, `ROT_TWO`, `ROT_THREE`, `ROT_FOUR`, and `ROT_N`) are swapped out for the fresh [`COPY`](https://docs.python.org/3.14/library/dis.html#opcode-COPY) and [`SWAP`](https://docs.python.org/3.14/library/dis.html#opcode-SWAP) instructions.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

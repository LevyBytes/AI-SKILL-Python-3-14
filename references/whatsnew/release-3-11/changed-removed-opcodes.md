# What's New In Python 3.11 / Changed/removed opcodes — dis

### Changed/removed opcodes

- Reworked [`MATCH_CLASS`](https://docs.python.org/3.14/library/dis.html#opcode-MATCH_CLASS) and [`MATCH_KEYS`](https://docs.python.org/3.14/library/dis.html#opcode-MATCH_KEYS) so they stop pushing an extra boolean flagging success/failure. On a miss, `None` now goes onto the stack where the tuple of pulled-out values would have sat.

- Reworked the opcodes dealing with exceptions to match the shift toward a single stack item rather than three (refer to [gh-89874](https://github.com/python/cpython/issues/89874)).

- Dropped `COPY_DICT_WITHOUT_KEYS`, `GEN_START`, `POP_BLOCK`, `SETUP_FINALLY` and `YIELD_FROM`.

[Subject index](INDEX.md) · [Previous source section](replaced-opcodes.md) · [Next source section](deprecated.md) · [Release/subject declaration](summary-release-highlights.md)

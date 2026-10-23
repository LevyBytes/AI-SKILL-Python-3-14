# What’s New In Python 3.12 / CPython bytecode changes - dis

### CPython bytecode changes

- The `LOAD_METHOD` instruction has been dropped, folded into [`LOAD_ATTR`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_ATTR). Should the low bit of its oparg be set, `LOAD_ATTR` will henceforth act as the former `LOAD_METHOD` instruction did. (Contributed by Ken Jin in [gh-93429](https://github.com/python/cpython/issues/93429).)

- Both the `JUMP_IF_FALSE_OR_POP` and `JUMP_IF_TRUE_OR_POP` instructions have been dropped. (Contributed by Irit Katriel in [gh-102859](https://github.com/python/cpython/issues/102859).)

- The `PRECALL` instruction has been dropped. (Contributed by Mark Shannon in [gh-92925](https://github.com/python/cpython/issues/92925).)

- A pair of new instructions, [`BINARY_SLICE`](https://docs.python.org/3.14/library/dis.html#opcode-BINARY_SLICE) and [`STORE_SLICE`](https://docs.python.org/3.14/library/dis.html#opcode-STORE_SLICE), have arrived. (Contributed by Mark Shannon in [gh-94163](https://github.com/python/cpython/issues/94163).)

- The [`CALL_INTRINSIC_1`](https://docs.python.org/3.14/library/dis.html#opcode-CALL_INTRINSIC_1) instructions have been added. (Contributed by Mark Shannon in [gh-99005](https://github.com/python/cpython/issues/99005).)

- The [`CALL_INTRINSIC_2`](https://docs.python.org/3.14/library/dis.html#opcode-CALL_INTRINSIC_2) instruction has been added. (Contributed by Irit Katriel in [gh-101799](https://github.com/python/cpython/issues/101799).)

- The [`CLEANUP_THROW`](https://docs.python.org/3.14/library/dis.html#opcode-CLEANUP_THROW) instruction has been added. (Contributed by Brandt Bucher in [gh-90997](https://github.com/python/cpython/issues/90997).)

- The `END_SEND` instruction has been added. (Contributed by Mark Shannon in [gh-103082](https://github.com/python/cpython/issues/103082).)

- Introduced under [**PEP 709**](https://peps.python.org/pep-0709/)'s implementation: the [`LOAD_FAST_AND_CLEAR`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_FAST_AND_CLEAR) instruction. Carl Meyer added it in [gh-101441](https://github.com/python/cpython/issues/101441).

- The [`LOAD_FAST_CHECK`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_FAST_CHECK) instruction has been added. (Contributed by Dennis Sweeney in [gh-93143](https://github.com/python/cpython/issues/93143).)

- The work behind [**PEP 695**](https://peps.python.org/pep-0695/) brings the [`LOAD_FROM_DICT_OR_DEREF`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_FROM_DICT_OR_DEREF), [`LOAD_FROM_DICT_OR_GLOBALS`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_FROM_DICT_OR_GLOBALS), and [`LOAD_LOCALS`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_LOCALS) opcodes. The `LOAD_CLASSDEREF` opcode is dropped, since pairing `LOAD_LOCALS` with `LOAD_FROM_DICT_OR_DEREF` covers its role. (Contributed by Jelle Zijlstra in [gh-103764](https://github.com/python/cpython/issues/103764).)

- The [`LOAD_SUPER_ATTR`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_SUPER_ATTR) instruction has been added. (Contributed by Carl Meyer and Vladimir Matveev in [gh-103497](https://github.com/python/cpython/issues/103497).)

- The `RETURN_CONST` instruction has been added. (Contributed by Wenyang Wang in [gh-101632](https://github.com/python/cpython/issues/101632).)

[Subject index](INDEX.md) · [Previous source section](optimizations.md) · [Next source section](demos-and-tools.md) · [Release/subject declaration](summary-release-highlights.md)

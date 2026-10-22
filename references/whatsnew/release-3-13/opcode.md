# What's New In Python 3.13 / opcode — dis

### opcode

- Relocate `opcode.ENABLE_SPECIALIZATION` to `_opcode.ENABLE_SPECIALIZATION`. Added during 3.12, this field was never documented and is not meant for outside consumption. (Contributed by Irit Katriel in [gh-105481](https://github.com/python/cpython/issues/105481).)

- Drop `opcode.is_pseudo()`, `opcode.MIN_PSEUDO_OPCODE`, and `opcode.MAX_PSEUDO_OPCODE`; introduced during Python 3.12, they were neither documented nor surfaced via [`dis`](https://docs.python.org/3.14/library/dis.html#module-dis), and were never meant for outside consumption. (Contributed by Irit Katriel in [gh-105481](https://github.com/python/cpython/issues/105481).)

[Subject index](INDEX.md) · [Previous source section](locale.md) · [Next source section](optparse.md) · [Release/subject declaration](summary-release-highlights.md)

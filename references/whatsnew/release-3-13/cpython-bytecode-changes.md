# What's New In Python 3.13 / CPython Bytecode Changes - dis

### CPython Bytecode Changes

- For [`YIELD_VALUE`](https://docs.python.org/3.14/library/dis.html#opcode-YIELD_VALUE), the oparg now holds `1` whenever the yield belongs to a yield-from or await, and `0` in all other cases. For [`RESUME`](https://docs.python.org/3.14/library/dis.html#opcode-RESUME), the oparg gained a bit signaling whether the except-depth equals 1, information required to optimize how generators are closed. (Contributed by Irit Katriel in [gh-111354](https://github.com/python/cpython/issues/111354).)

[Subject index](INDEX.md) · [Previous source section](pending-removal-in-future-versions-splituser.md) · [Next source section](c-api-changes-new-features.md) · [Release/subject declaration](summary-release-highlights.md)

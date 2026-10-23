# What’s New In Python 3.12 / dis - dis

### dis

- Pseudo instruction opcodes — the kind the compiler relies on yet that never show up in runnable bytecode — are now surfaced through the [`dis`](https://docs.python.org/3.14/library/dis.html#module-dis) module. While [`HAVE_ARGUMENT`](https://docs.python.org/3.14/library/dis.html#opcode-HAVE_ARGUMENT) still applies to genuine opcodes, it offers nothing for pseudo instructions. Reach for the new [`dis.hasarg`](https://docs.python.org/3.14/library/dis.html#dis.hasarg) collection in its place. (Contributed by Irit Katriel in [gh-94216](https://github.com/python/cpython/issues/94216).)

- Add the [`dis.hasexc`](https://docs.python.org/3.14/library/dis.html#dis.hasexc) collection that marks instructions establishing an exception handler. (Contributed by Irit Katriel in [gh-94216](https://github.com/python/cpython/issues/94216).)

[Subject index](INDEX.md) · [Previous source section](csv.md) · [Next source section](fractions.md) · [Release/subject declaration](summary-release-highlights.md)

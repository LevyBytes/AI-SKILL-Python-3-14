# What's New In Python 3.13 / locale

### locale

- Drop the `locale.resetlocale()` function, which carried a Python 3.11 deprecation. Reach for `locale.setlocale(locale.LC_ALL, "")` in its place. (Contributed by Victor Stinner in [gh-104783](https://github.com/python/cpython/issues/104783).)

[Subject index](INDEX.md) · [Previous source section](importlib-metadata.md) · [Next source section](opcode.md) · [Release/subject declaration](summary-release-highlights.md)

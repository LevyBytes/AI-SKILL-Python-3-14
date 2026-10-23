# What’s New In Python 3.12 / io - io

### io

- Drop the `io.OpenWrapper` and `_pyio.OpenWrapper` of [`io`](https://docs.python.org/3.14/library/io.html#module-io), deprecated back in Python 3.10: simply use [`open()`](https://docs.python.org/3.14/library/functions.html#open) instead. As a built-in, the `open()` ([`io.open()`](https://docs.python.org/3.14/library/io.html#io.open)) function is always available. From Python 3.10 on, `_pyio.open()` is additionally a static method. (Contributed by Victor Stinner in [gh-94169](https://github.com/python/cpython/issues/94169).)

[Subject index](INDEX.md) · [Previous source section](imp.md) · [Next source section](locale.md) · [Release/subject declaration](summary-release-highlights.md)

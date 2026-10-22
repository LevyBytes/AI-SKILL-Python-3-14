# What's New In Python 3.13 / Regression Test Changes

### Regression Test Changes

- A Python compiled with `configure` [`--with-pydebug`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-pydebug) now accepts a [`-X presite=package.module`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command-line option. When supplied, it names a module to import early in the interpreter's lifecycle, ahead of `site.py` running. (Contributed by Łukasz Langa in [gh-110769](https://github.com/python/cpython/issues/110769).)

[Subject index](INDEX.md) · [Previous source section](c-api-unraisable-exception-migration.md) · [Release/subject declaration](summary-release-highlights.md)

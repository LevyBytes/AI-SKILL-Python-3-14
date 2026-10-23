# What's New In Python 3.13 / configparser - configparser

### configparser

- [`ConfigParser`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser) henceforth supports unnamed sections, thereby permitting key-value pairs at the top level. Switch this on through the fresh *allow_unnamed_section* parameter. (Contributed by Pedro Sousa Lacerda in [gh-66449](https://github.com/python/cpython/issues/66449).)

### configparser

- Drop the undocumented `LegacyInterpolation` class, which the docstring marked deprecated as of Python 3.2 and which has been deprecated at runtime since Python 3.11. (Contributed by Hugo van Kemenade in [gh-104886](https://github.com/python/cpython/issues/104886).)

[Subject index](INDEX.md) · [Previous source section](concurrent-futures.md) · [Next source section](copy.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](builtins.md) · [Next source section](importlib-metadata.md)

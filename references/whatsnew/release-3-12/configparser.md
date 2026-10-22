# What’s New In Python 3.12 / configparser — configparser

### configparser

- A handful of [`configparser`](https://docs.python.org/3.14/library/configparser.html#module-configparser) names deprecated all the way back in 3.2 were dropped per [gh-89336](https://github.com/python/cpython/issues/89336):

  - [`configparser.ParsingError`](https://docs.python.org/3.14/library/configparser.html#configparser.ParsingError) has lost its `filename` attribute and argument. Switch to the `source` attribute and argument instead.

  - [`configparser`](https://docs.python.org/3.14/library/configparser.html#module-configparser) has dropped the `SafeConfigParser` class. Adopt the briefer [`ConfigParser`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser) name instead.

  - [`configparser.ConfigParser`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser) has dropped its `readfp` method. Use [`read_file()`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser.read_file) instead.

[Subject index](INDEX.md) · [Previous source section](asynchat-and-asyncore.md) · [Next source section](distutils.md) · [Release/subject declaration](summary-release-highlights.md)

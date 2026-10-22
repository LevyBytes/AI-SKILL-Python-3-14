# Python 3.13.0 alpha 5 / library / configparser

[gh-107625](https://github.com/python/cpython/issues/107625): The [`read()`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser.read) and [`read_file()`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser.read_file) methods on [`configparser.ConfigParser`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser) now raise [`configparser.ParsingError`](https://docs.python.org/3.14/library/configparser.html#configparser.ParsingError) whenever a key that lacks a matching value is continued, meaning an indented line follows it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

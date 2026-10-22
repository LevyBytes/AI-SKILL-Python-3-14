# Python 3.13.0 alpha 6 / library / configparser

[gh-116957](https://github.com/python/cpython/issues/116957): configparser: Stop leaving ConfigParser values in a broken state (held as a list rather than a str) once an earlier read has raised DuplicateSectionError or DuplicateOptionError.

[gh-66449](https://github.com/python/cpython/issues/66449): [`configparser.ConfigParser`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser), when set up for it, now permits unnamed sections ahead of named ones.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

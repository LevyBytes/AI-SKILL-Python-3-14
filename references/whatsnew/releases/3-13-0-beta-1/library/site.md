# Python 3.13.0 beta 1 / library / site

[gh-77102](https://github.com/python/cpython/issues/77102): The [`site`](https://docs.python.org/3.14/library/site.html#module-site) module now decodes a `.pth` file as UTF-8 first, falling back to the [locale encoding](https://docs.python.org/3.14/glossary.html#term-locale-encoding) should a `UnicodeDecodeError` occur. Previously only the locale encoding was supported.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

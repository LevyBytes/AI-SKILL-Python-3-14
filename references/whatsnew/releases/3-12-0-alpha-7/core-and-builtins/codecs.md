# Python 3.12.0 alpha 7 / core and builtins / codecs

[gh-102406](https://github.com/python/cpython/issues/102406): When [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs) encoding or decoding fails, the context detail (which operation, which codecs) now rides along as [**PEP 678**](https://peps.python.org/pep-0678/) notes rather than being chained onto a brand-new instance of the exception.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

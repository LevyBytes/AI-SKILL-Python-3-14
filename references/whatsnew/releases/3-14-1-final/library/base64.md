# Python 3.14.1 final / library / base64

[gh-138775](https://github.com/python/cpython/issues/138775): Running [`base64`](https://docs.python.org/3.14/library/base64.html#module-base64) by way of `python -m` was corrected so that input coming from a terminal is detected and EOF is recognized correctly.

[gh-141141](https://github.com/python/cpython/issues/141141): A thread safety defect in [`base64.b85decode()`](https://docs.python.org/3.14/library/base64.html#base64.b85decode) was addressed. Benel Tayar provided the contribution.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

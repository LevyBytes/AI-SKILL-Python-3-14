# Python 3.12.0 alpha 1 / library / email

[gh-95087](https://github.com/python/cpython/issues/95087): An IndexError thrown while parsing an invalid date inside the [`email`](https://docs.python.org/3.14/library/email.html#module-email) module is fixed.

[gh-93010](https://github.com/python/cpython/issues/93010): Under one quite unusual scenario, the email package attempted to append the missing `InvalidHeaderError` onto the defect list; the right one to use was `InvalidHeaderDefect`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

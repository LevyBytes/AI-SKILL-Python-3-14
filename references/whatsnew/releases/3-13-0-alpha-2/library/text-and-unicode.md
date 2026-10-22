# Python 3.13.0 alpha 2 / library / text and unicode

[gh-86826](https://github.com/python/cpython/issues/86826): The full span of values for the TZ string laid out by RFC 8536 is now handled by `zipinfo`, which also catches every invalid form. On bad data, the Python and C implementations now both raise exceptions of one type.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

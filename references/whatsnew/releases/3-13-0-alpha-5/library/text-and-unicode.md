# Python 3.13.0 alpha 5 / library / text and unicode

[bpo-31116](https://bugs.python.org/issue?@action=redirect&bpo=31116): Provide Z85 encoding within `base64`.

[gh-76511](https://github.com/python/cpython/issues/76511): Repair the UnicodeEncodeError raised by `email.Message.as_string()` when a message that purports to use the ascii character set in fact holds non-ascii characters. Those non-ascii characters now get swapped for the U+FFFD replacement character, just as the `replace` error handler does.

[gh-102389](https://github.com/python/cpython/issues/102389): Register `windows_31j` among the aliases of the `cp932` codec

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

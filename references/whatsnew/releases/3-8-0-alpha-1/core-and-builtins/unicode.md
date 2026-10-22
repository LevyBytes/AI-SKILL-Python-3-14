# Python 3.8.0 alpha 1 / core and builtins / unicode

[bpo-35552](https://bugs.python.org/issue?@action=redirect&bpo=35552): The format characters `%s` and `%V` in [`PyUnicode_FromFormat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormat) plus `%s` in [`PyBytes_FromFormat()`](https://docs.python.org/3.14/c-api/bytes.html#c.PyBytes_FromFormat) no longer read past the limit in memory when *precision* is given.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

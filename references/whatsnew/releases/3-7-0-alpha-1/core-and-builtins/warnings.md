# Python 3.7.0 alpha 1 / core and builtins / warnings

[bpo-29337](https://bugs.python.org/issue?@action=redirect&bpo=29337): A possible BytesWarning when comparing the code objects was fixed. Such warnings could surface at compile time.

[bpo-30465](https://bugs.python.org/issue?@action=redirect&bpo=30465): Within f-strings, the location data (`lineno` and `col_offset`) is now (for the most part) right. That keeps tools such as flake8 from flagging warnings against the wrong line (usually the file's opening line).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

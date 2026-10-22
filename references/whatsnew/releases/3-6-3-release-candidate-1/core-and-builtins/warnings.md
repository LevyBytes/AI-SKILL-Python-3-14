# Python 3.6.3 release candidate 1 / core and builtins / warnings

[bpo-30465](https://bugs.python.org/issue?@action=redirect&bpo=30465): Within f-strings the location data (`lineno` and `col_offset`) is now largely correct. As a result tools such as flake8 stop reporting warnings against the wrong line (commonly the file's first line).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

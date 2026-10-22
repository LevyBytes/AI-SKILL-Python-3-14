# Python 3.10.0 alpha 6 / core and builtins / text and unicode

[bpo-41972](https://bugs.python.org/issue?@action=redirect&bpo=41972): Substring search operations like `str1 in str2` and `str2.find(str1)` may now apply the "Two-Way" string comparison algorithm on occasion to sidestep quadratic behavior with long strings.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

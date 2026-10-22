# Python 3.11.0 alpha 6 / core and builtins / numeric

[bpo-46820](https://bugs.python.org/issue?@action=redirect&bpo=46820): Correct parsing of a numeric literal that is immediately (with no spaces) trailed by the "not in" keywords, as in `1not in x`. The parser now emits only a warning rather than a syntax error.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

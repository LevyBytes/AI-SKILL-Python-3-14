# Python 3.7.0 alpha 1 / core and builtins / tokenize

[bpo-25324](https://bugs.python.org/issue?@action=redirect&bpo=25324): The tokens required for parsing in Python were moved into C: `COMMENT`, `NL` and `ENCODING`. Consequently the tokens plus tok_names in the token module stay untouched when the tokenize module is imported.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

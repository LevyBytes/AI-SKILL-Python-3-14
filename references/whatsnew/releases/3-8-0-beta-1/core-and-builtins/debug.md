# Python 3.8.0 beta 1 / core and builtins / debug

[bpo-37050](https://bugs.python.org/issue?@action=redirect&bpo=37050): Sharpens the AST for “debug” f-strings, the ones that use ‘=’ to echo the source of the expression under evaluation. expr_text is dropped from the FormattedValue node; a Constant string node takes its place (perhaps fused with neighboring constant expressions within the f-string).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

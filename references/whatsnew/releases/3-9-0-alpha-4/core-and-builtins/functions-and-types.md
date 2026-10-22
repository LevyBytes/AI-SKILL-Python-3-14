# Python 3.9.0 alpha 4 / core and builtins / functions and types

[bpo-39579](https://bugs.python.org/issue?@action=redirect&bpo=39579): Adjust the ending column offset of `Attribute` nodes built within `ast_for_dotted_name` so it lands at the close of the current node rather than at the close of the final `NAME` node.

[bpo-39510](https://bugs.python.org/issue?@action=redirect&bpo=39510): Repair a segfault in the `readinto()` method when invoked on a closed BufferedReader.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.10.0 alpha 7 / core and builtins / compiler and parser

[bpo-27129](https://bugs.python.org/issue?@action=redirect&bpo=27129): Bumped the CPython bytecode magic number.

[bpo-27129](https://bugs.python.org/issue?@action=redirect&bpo=27129): Internally, the bytecode interpreter now works with instruction offsets rather than byte offsets. That cuts down on the EXTENDED_ARG instructions required and tidies instruction dispatch somewhat.

[bpo-43410](https://bugs.python.org/issue?@action=redirect&bpo=43410): Fixed a bug that crashed the parser when it produced syntax errors while reading input from stdin. Pablo Galindo supplied the patch

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

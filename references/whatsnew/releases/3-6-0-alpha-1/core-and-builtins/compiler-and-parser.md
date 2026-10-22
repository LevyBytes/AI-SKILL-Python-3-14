# Python 3.6.0 alpha 1 / core and builtins / compiler and parser

[bpo-25630](https://bugs.python.org/issue?@action=redirect&bpo=25630): Repair a possible segfault during argument parsing inside functions that take filesystem paths.

[bpo-25555](https://bugs.python.org/issue?@action=redirect&bpo=25555): Repair the parser and AST so that the lineno and col_offset of an "arg" node get filled in while compiling AST from Python objects.

[bpo-26146](https://bugs.python.org/issue?@action=redirect&bpo=26146): Introduce a new flavor of AST node, `ast.Constant`. External AST optimizers can rely on it, though the compiler itself never emits such a node directly.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

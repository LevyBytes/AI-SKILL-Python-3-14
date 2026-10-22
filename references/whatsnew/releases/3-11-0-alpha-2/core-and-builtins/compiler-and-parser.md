# Python 3.11.0 alpha 2 / core and builtins / compiler and parser

[bpo-45494](https://bugs.python.org/issue?@action=redirect&bpo=45494): Repair a parser crash that arose while reporting errors that involve invalid continuation characters. Pablo Galindo wrote the patch.

[bpo-45408](https://bugs.python.org/issue?@action=redirect&bpo=45408): Repair a parser crash that occurred while reporting tokenizer errors arising at the same moment that unclosed parentheses were spotted. Pablo Galindo wrote the patch.

[bpo-45367](https://bugs.python.org/issue?@action=redirect&bpo=45367): The `BINARY_MULTIPLY` opcode was specialized into `BINARY_MULTIPLY_INT` and `BINARY_MULTIPLY_FLOAT` via the PEP 659 machinery.

[bpo-44525](https://bugs.python.org/issue?@action=redirect&bpo=44525): Stand up the first specialization infrastructure for the `CALL_FUNCTION` opcode. Built initial specializations covering C function calls:

  - `CALL_FUNCTION_BUILTIN_O` for `METH_O` flag.

  - `CALL_FUNCTION_BUILTIN_FAST` for `METH_FASTCALL` flag without keywords.

  - `CALL_FUNCTION_LEN` for `len(o)`.

  - `CALL_FUNCTION_ISINSTANCE` for `isinstance(o, t)`.

[bpo-44511](https://bugs.python.org/issue?@action=redirect&bpo=44511): Better the bytecode produced for class and mapping patterns.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

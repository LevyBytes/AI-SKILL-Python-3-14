# Python 3.9.0 alpha 3 / core and builtins / compiler and parser

[bpo-39235](https://bugs.python.org/issue?@action=redirect&bpo=39235): Fix the AST end location for a lone generator expression sitting in a function call, for example f(i for i in a).

[bpo-39156](https://bugs.python.org/issue?@action=redirect&bpo=39156): The single COMPARE_OP bytecode instruction was divided into four separate instructions.

  - COMPARE_OP for rich comparisons

  - IS_OP for ‘is’ and ‘is not’ tests

  - CONTAINS_OP for ‘in’ and ‘is not’ tests

  - JUMP_IF_NOT_EXC_MATCH for checking exceptions in ‘try-except’ statements.

The interpreter becomes clearer as a result, and a small performance gain is expected.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

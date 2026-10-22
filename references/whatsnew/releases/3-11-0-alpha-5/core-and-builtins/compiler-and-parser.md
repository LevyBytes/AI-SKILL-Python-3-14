# Python 3.11.0 alpha 5 / core and builtins / compiler and parser

[bpo-43683](https://bugs.python.org/issue?@action=redirect&bpo=43683): Introduce the ASYNC_GEN_WRAP opcode, which wraps each value an async generator is about to yield. This drops the special-casing of async generators that the `YIELD_VALUE` instruction previously required.

[bpo-46409](https://bugs.python.org/issue?@action=redirect&bpo=46409): Introduce a fresh `RETURN_GENERATOR` bytecode for building generators. This streamlines how the VM invokes Python functions, since generator functions no longer need any special handling.

A `JUMP_NO_INTERRUPT` bytecode is also added; it behaves like `JUMP_ABSOLUTE` except that it skips the interrupt check.

[bpo-45773](https://bugs.python.org/issue?@action=redirect&bpo=45773): Take out two unsound ?peephole? optimizations from the bytecode compiler.

[bpo-46458](https://bugs.python.org/issue?@action=redirect&bpo=46458): Shuffle the code the compiler emits for a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try)-[`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) block so the [`else`](https://docs.python.org/3.14/reference/compound_stmts.html#else) block's code follows straight after the `try` body (no jump in between). That suits the happy path better.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

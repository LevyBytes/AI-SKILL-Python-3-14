# Python 3.11.0 alpha 4 / core and builtins / compiler and parser

[bpo-45923](https://bugs.python.org/issue?@action=redirect&bpo=45923): Introduce the RESUME opcode. As a logical no-op, the compiler emits it at every point where a Python function may begin execution. The interpreter relies on it to run tracing as well as optimizer checks.

[bpo-46009](https://bugs.python.org/issue?@action=redirect&bpo=46009): Delete the `GEN_START` opcode.

[bpo-46110](https://bugs.python.org/issue?@action=redirect&bpo=46110): Introduce a recursion ceiling in the PEG parser so a stack overflow is prevented. Pablo Galindo wrote the patch.

[bpo-44525](https://bugs.python.org/issue?@action=redirect&bpo=44525): Swap the four call bytecode instructions for one pre-call instruction together with two call instructions.

Removes `CALL_FUNCTION`, `CALL_FUNCTION_KW`, `CALL_METHOD` and `CALL_METHOD_KW`.

Adds `CALL_NO_KW` and `CALL_KW` call instructions, and `PRECALL_METHOD` prefix for pairing with `LOAD_METHOD`.

[bpo-46054](https://bugs.python.org/issue?@action=redirect&bpo=46054): Correct a parser failure that occurred while reading non-utf8 characters within source files. Pablo Galindo wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

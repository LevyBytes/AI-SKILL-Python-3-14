# Python 3.11.0 alpha 6 / core and builtins / functions and types

[bpo-46329](https://bugs.python.org/issue?@action=redirect&bpo=46329): Introduce the `PUSH_NULL` instruction. It serves as a prefix ahead of evaluating a callable, giving the stack an identical layout for methods as for other call forms. The two opcodes `PRECALL_FUNCTION` and `PRECALL_METHOD` collapse together into one `PRECALL` instruction.

Semantics stay the same.

[bpo-46724](https://bugs.python.org/issue?@action=redirect&bpo=46724): Guarantee that every backwards jump emits a `JUMP_ABSOLUTE` instruction, in place of `JUMP_FORWARD` carrying an argument of `(2**32)+offset`.

[bpo-46329](https://bugs.python.org/issue?@action=redirect&bpo=46329): Shift `KW_NAMES` ahead of the `PRECALL` instruction within the call sequence. Adjust the `operand` of `CALL` so it matches `PRECALL`, easing specialization.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

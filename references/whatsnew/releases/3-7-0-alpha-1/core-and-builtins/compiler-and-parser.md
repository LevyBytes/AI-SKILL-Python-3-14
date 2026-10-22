# Python 3.7.0 alpha 1 / core and builtins / compiler and parser

[bpo-30501](https://bugs.python.org/issue?@action=redirect&bpo=30501): For involved condition expressions, the compiler now emits tighter code inside the "if", "while" and "assert" statement, the "if" expression, plus generator expressions and comprehensions.

[bpo-28665](https://bugs.python.org/issue?@action=redirect&bpo=28665): Make the STORE_DEREF opcode run 40% quicker.

[bpo-28517](https://bugs.python.org/issue?@action=redirect&bpo=28517): Corrected an of-by-one error within the peephole optimizer that left unreachable code in place.

[bpo-24098](https://bugs.python.org/issue?@action=redirect&bpo=24098): Repaired a possible crash that arose whenever the AST got altered while it was being compiled.

[bpo-25677](https://bugs.python.org/issue?@action=redirect&bpo=25677): Fix where the syntax error caret sits for indented blocks. Michael Layzell contributed the underlying patch.

[bpo-31344](https://bugs.python.org/issue?@action=redirect&bpo=31344): To give testers finer control over tracing while exercising the interpreter, two new frame attributes were introduced that govern whether certain trace events fire: `f_trace_lines` (`True` by default) lets you suppress per-line trace events; and `f_trace_opcodes` (`False` by default) lets you enable per-opcode trace events.

[bpo-30721](https://bugs.python.org/issue?@action=redirect&bpo=30721): For people relying on Python 2 redirection syntax, `print` now displays the right usage hint. Sanyam Khurana provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

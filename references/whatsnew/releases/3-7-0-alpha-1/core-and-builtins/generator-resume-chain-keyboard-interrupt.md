# Python 3.7.0 alpha 1 / core and builtins / should keyboardinterrupt land while interpreter partway through resuming chain

[bpo-30039](https://bugs.python.org/issue?@action=redirect&bpo=30039): Should a KeyboardInterrupt land while the interpreter is partway through resuming a chain of nested 'yield from' or 'await' calls, it now arrives correctly at the innermost frame.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

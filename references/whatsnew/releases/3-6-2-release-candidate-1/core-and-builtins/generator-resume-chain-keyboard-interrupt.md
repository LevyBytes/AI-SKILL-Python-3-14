# Python 3.6.2 release candidate 1 / core and builtins / should keyboardinterrupt land while interpreter partway through resuming series

[bpo-30039](https://bugs.python.org/issue?@action=redirect&bpo=30039): Should a KeyboardInterrupt land while the interpreter is partway through resuming a series of nested "yield from" or "await" calls, it now arrives correctly at the innermost frame.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.9.0 alpha 2 / tests / compiler and parser

[bpo-38965](https://bugs.python.org/issue?@action=redirect&bpo=38965): Repair test_faulthandler on GCC 10. Apply the "volatile" keyword within `faulthandler._stack_overflow()` so tail call optimization is blocked on every compiler, instead of depending on a compiler specific pragma.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

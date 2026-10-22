# Python 3.13.0 alpha 6 / core and builtins / hashlib

[gh-99108](https://github.com/python/cpython/issues/99108): Refreshed the [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) built-in [HACL* project](https://github.com/hacl-star/hacl-star) C code from the upstream source we draw on for numerous implementations whenever OpenSSL does not supply them in a particular build. Doing so also sidesteps the uncommon chance of a C symbol name one definition rule linking problem.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

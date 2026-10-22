# Python 3.12.0 alpha 3 / library / binary

[gh-98253](https://github.com/python/cpython/issues/98253): The typing module's implementation is now better hardened against reference leaks within binary extension modules.

Formerly, a reference leak inside a typed C API-based extension module had the potential to leak typing-module internals, which in turn could seed leaks across virtually any other package that carried typed function signatures. The typing package isn't the root cause, yet such non-local dependences make debugging large-scale projects harder, so the implementation was revised to limit the damage through stronger isolation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.12.0 alpha 4 / core and builtins / functions and types

[gh-98522](https://github.com/python/cpython/issues/98522): Code objects gained an internal version counter so that inner functions and comprehensions version more accurately, which in turn lets those functions specialize better. Neither Python nor C extensions can observe this change.

[gh-100357](https://github.com/python/cpython/issues/100357): Migrate `vars`, `dir`, `next`, `getattr`, and `iter` to argument clinic.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

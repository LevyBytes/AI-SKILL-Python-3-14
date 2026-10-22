# Python 3.13.0 alpha 1 / core and builtins / because runtime cannot promise extensions will leave immortal objects

[gh-105587](https://github.com/python/cpython/issues/105587): Because the runtime cannot promise that Extensions will leave immortal objects unmutated, this adjusts _PyStaticObject_CheckRefcnt to issue a warning rather than assert.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

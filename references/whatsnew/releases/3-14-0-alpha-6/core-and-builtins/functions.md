# Python 3.14.0 alpha 6 / core and builtins / functions

[gh-128396](https://github.com/python/cpython/issues/128396): A crash triggered by calling [`locals()`](https://docs.python.org/3.14/library/functions.html#locals) within an inline comprehension that reuses the same local variable as the enclosing frame scope, where that variable is a free or cell var, has been fixed.

[gh-125331](https://github.com/python/cpython/issues/125331): `from __future__ import barry_as_FLUFL` now functions across more situations: inside files, with the `-c` flag, and in the REPL even when several statements sit on one line. Before, it only took effect on later lines in the REPL and when the right flags went straight to [`compile()`](https://docs.python.org/3.14/library/functions.html#compile). Pablo Galindo supplied the patch.

[gh-121464](https://github.com/python/cpython/issues/121464): Running several iterations over one [`enumerate()`](https://docs.python.org/3.14/library/functions.html#enumerate) iterator at the same time is now safe under free-threading. Consult [Strategy for Iterators in Free Threading](https://github.com/python/cpython/issues/124397).

[gh-87790](https://github.com/python/cpython/issues/87790): Underscore and comma are now accepted as thousands separators within the fractional part for floating-point presentation types in new-style string formatting (via [`format()`](https://docs.python.org/3.14/library/functions.html#format) or [f-strings](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings)). Sergey B Kirpichev supplied the patch.

[gh-120608](https://github.com/python/cpython/issues/120608): [`reversed()`](https://docs.python.org/3.14/library/functions.html#reversed) was adapted for the free-threading build. The `reversed()` remains non-thread-safe in that simultaneous iterations might observe the same object, yet they will not corrupt the interpreter state.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

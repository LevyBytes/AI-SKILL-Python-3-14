# Python 3.14.0 alpha 5 / core and builtins / collections and iteration

[gh-125723](https://github.com/python/cpython/issues/125723): Resolved a crash involving `gi_frame.f_locals` for cases where generator frames stay alive longer than their generator. Mikhail Efimov authored the fix.

[gh-128714](https://github.com/python/cpython/issues/128714): Close the potential races in the get/set dunder methods `__annotations__`, `__annotate__` and `__type_params__` on function objects, and supply matching tests.

[gh-126703](https://github.com/python/cpython/issues/126703): Make iterating over lists and tuples quicker by drawing the iterator objects from a freelist.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

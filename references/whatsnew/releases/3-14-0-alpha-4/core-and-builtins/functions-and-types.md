# Python 3.14.0 alpha 4 / core and builtins / functions and types

[gh-127274](https://github.com/python/cpython/issues/127274): Introduce a fresh `CO_METHOD` flag on [`co_flags`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_flags) so it is possible to tell whether the code object came from a function declared inside a class scope.

[gh-127773](https://github.com/python/cpython/issues/127773): Skip the type attribute cache whenever a type has an incompatible [MRO](https://docs.python.org/3.14/glossary.html#term-MRO).

[gh-127809](https://github.com/python/cpython/issues/127809): Repair a case where the experimental JIT could deduce the wrong result type for exponentiation (`**` and `**=`), which led to crashes or other bugs.

[gh-126703](https://github.com/python/cpython/issues/126703): Boosted class-method performance by leaning on a freelist.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.0 alpha 7 / core and builtins / functions and types

[gh-128632](https://github.com/python/cpython/issues/128632): Forbids `__classdict__` as a type parameter name. Earlier, that name could crash the interpreter under certain conditions.

[gh-126703](https://github.com/python/cpython/issues/126703): Makes builtin methods faster through a freelist.

[gh-131798](https://github.com/python/cpython/issues/131798): The JIT can now drop a surplus `_TO_BOOL_BOOL` instruction following `_CONTAINS_OP_SET` by fixing the return type to bool.

[gh-131998](https://github.com/python/cpython/issues/131998): Fixed a crash arising from the use of an unbound method [descriptor](https://docs.python.org/3.14/glossary.html#term-descriptor) object within a function where a bound method descriptor had been used.

[gh-130924](https://github.com/python/cpython/issues/130924): Referring to a name within a function-scope annotation no longer forces a cell to be created for that variable. This addresses a regression seen in earlier alphas of Python 3.14.

[gh-131800](https://github.com/python/cpython/issues/131800): Strengthened the experimental JIT's capacity to strip type checks from certain subscripting operations.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

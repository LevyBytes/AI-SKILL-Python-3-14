# Python 3.13.0 beta 1 / core and builtins / functions and types

[gh-118492](https://github.com/python/cpython/issues/118492): Repair a case where the type cache could surface an attribute accessed earlier once a finalizer executes.

[gh-118160](https://github.com/python/cpython/issues/118160): [Annotation scopes](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes) inside classes may now hold comprehensions. Even so, those comprehensions do not get inlined into their enclosing scope at runtime. Jelle Zijlstra contributed the patch.

[gh-117958](https://github.com/python/cpython/issues/117958): A `get_jit_code()` method was added for reaching the JIT-compiled machine code on the UOp Executor while the experimental JIT is switched on. Anthony Shaw contributed the patch.

[gh-109118](https://github.com/python/cpython/issues/109118): An [annotation scope](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes) nested in class scopes may now hold lambdas.

[gh-116129](https://github.com/python/cpython/issues/116129): Deliver [**PEP 696**](https://peps.python.org/pep-0696/), which brings defaults for type parameters. Jelle Zijlstra contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

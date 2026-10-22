# Python 3.13.0 alpha 1 / core and builtins / functions

[gh-98963](https://github.com/python/cpython/issues/98963): Bring back the option for a subclass of [`property`](https://docs.python.org/3.14/library/functions.html#property) to declare `__slots__` or otherwise stay dict-less, achieved by overlooking failures to assign a docstring on such a class. This conduct had regressed back in 3.12beta1. Code already in existence found the introduction of a previously absent [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) disruptive.

[gh-105035](https://github.com/python/cpython/issues/105035): Repair [`super()`](https://docs.python.org/3.14/library/functions.html#super) calls on types that supply a custom [`tp_getattro`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_getattro) implementation (for instance, meta-types.)

[gh-106917](https://github.com/python/cpython/issues/106917): Repair classmethod-style [`super()`](https://docs.python.org/3.14/library/functions.html#super) method invocations (that is, cases where `super()`'s second argument, or the second argument implied from `self/cls` for zero-arg super, is a type) whenever the call's target is not a classmethod.

[gh-108113](https://github.com/python/cpython/issues/108113): The [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) built-in now takes a new flag, `ast.PyCF_OPTIMIZED_AST`, much like `ast.PyCF_ONLY_AST` save that the returned `AST` is optimized according to the value of the `optimize` argument.

In addition, [`ast.parse()`](https://docs.python.org/3.14/library/ast.html#ast.parse) now takes an optional `optimize` argument, which it forwards to the [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) built-in. This lets you obtain an optimized `AST`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

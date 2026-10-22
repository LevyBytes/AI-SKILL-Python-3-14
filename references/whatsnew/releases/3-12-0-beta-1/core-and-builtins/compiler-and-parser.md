# Python 3.12.0 beta 1 / core and builtins / compiler and parser

[gh-97933](https://github.com/python/cpython/issues/97933): [**PEP 709**](https://peps.python.org/pep-0709/): list, dict and set comprehensions are now inlined, boosting performance and shrinking bytecode size.

[gh-103763](https://github.com/python/cpython/issues/103763): Implement [**PEP 695**](https://peps.python.org/pep-0695/), which brings syntactic support for generic classes, generic functions, and type aliases.

A fresh `type X = ...` syntax serves type aliases; at runtime it produces an instance of the new class `typing.TypeAliasType`. Its value is evaluated lazily and reachable via the `.__value__` attribute. The implementation introduces a new AST node `ast.TypeAlias`.

Fresh syntax (`class X[T]: ...`, `def func[T](): ...`) covers the definition of generic functions and classes. It surfaces as a new `type_params` attribute on the AST nodes for classes and functions. That node carries instances of the new AST classes `ast.TypeVar`, `ast.ParamSpec`, and `ast.TypeVarTuple`.

`typing.TypeVar`, `typing.ParamSpec`, `typing.ParamSpecArgs`, `typing.ParamSpecKwargs`, `typing.TypeVarTuple`, and `typing.Generic` are henceforth written in C instead of Python.

Three new bytecode instructions — `LOAD_LOCALS`, `LOAD_CLASSDICT_OR_GLOBAL`, and `LOAD_CLASSDICT_OR_DEREF` — exist to resolve names within class namespaces correctly.

Eric Traut, Larry Hastings, and Jelle Zijlstra wrote the patch.

[gh-104482](https://github.com/python/cpython/issues/104482): Repair three error-handling defects in the way ast.c validates pattern matching statements.

[gh-104405](https://github.com/python/cpython/issues/104405): Resolve a case where certain [bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode) instructions might disregard [**PEP 523**](https://peps.python.org/pep-0523/) during call "inlining".

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.13.0 alpha 1 / library / ast

[gh-104799](https://github.com/python/cpython/issues/104799): Repositioned the (refer to [**PEP 695**](https://peps.python.org/pep-0695/)) `type_params` field across [`ast.ClassDef`](https://docs.python.org/3.14/library/ast.html#ast.ClassDef), [`ast.AsyncFunctionDef`](https://docs.python.org/3.14/library/ast.html#ast.AsyncFunctionDef), and [`ast.FunctionDef`](https://docs.python.org/3.14/library/ast.html#ast.FunctionDef) to hold backward compatibility better. Jelle Zijlstra authored this

[gh-108843](https://github.com/python/cpython/issues/108843): Corrected a problem in [`ast.unparse()`](https://docs.python.org/3.14/library/ast.html#ast.unparse) while unparsing f-strings that contain many quote types.

[gh-108469](https://github.com/python/cpython/issues/108469): [`ast.unparse()`](https://docs.python.org/3.14/library/ast.html#ast.unparse) now handles the new [f-string](https://docs.python.org/3.14/glossary.html#term-f-string) syntax that arrived in Python 3.12. Be aware that, for simplicity, the f-string quotes get reselected under the new syntax. (Steven Sun wrote the patch)

[gh-104799](https://github.com/python/cpython/issues/104799): Let [`ast.unparse()`](https://docs.python.org/3.14/library/ast.html#ast.unparse) unparse function and class definitions built without the fresh `type_params` field out of [**PEP 695**](https://peps.python.org/pep-0695/). Jelle Zijlstra wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

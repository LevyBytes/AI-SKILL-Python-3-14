# Python 3.7.0 alpha 1 / core and builtins / ast

[bpo-29463](https://bugs.python.org/issue?@action=redirect&bpo=29463): Give the Module, ClassDef, FunctionDef, and AsyncFunctionDef ast nodes a `docstring` field. The docstring is no longer the first stmt in their body. This changes the `co_firstlineno` and `co_lnotab` of the code object for module and class. (Reverted in [bpo-32911](https://bugs.python.org/issue?@action=redirect&bpo=32911).)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

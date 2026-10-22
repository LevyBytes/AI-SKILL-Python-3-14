# Python 3.8.0 alpha 1 / core and builtins / ast

[bpo-32911](https://bugs.python.org/issue?@action=redirect&bpo=32911): Because unexpected compatibility problems surfaced during downstream beta testing, [bpo-29463](https://bugs.python.org/issue?@action=redirect&bpo=29463) was reverted. The `docstring` field, added in 3.7a1, is dropped from the Module, ClassDef, FunctionDef, and AsyncFunctionDef ast nodes. The docstring expression returns as the first statement within their body. Based on a patch by Inada Naoki.

[bpo-31902](https://bugs.python.org/issue?@action=redirect&bpo=31902): Corrected the `col_offset` attribute on the ast nodes `ast.AsyncFor`, `ast.AsyncFunctionDef`, and `ast.AsyncWith`. Beforehand, `col_offset` referred to the keyword following `async`.

[bpo-35766](https://bugs.python.org/issue?@action=redirect&bpo=35766): Add the ability to parse PEP 484 type comments within the ast module. (Disabled by default.) This brings in the core functionality of its third party fork, [typed_ast](https://github.com/python/typed_ast).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

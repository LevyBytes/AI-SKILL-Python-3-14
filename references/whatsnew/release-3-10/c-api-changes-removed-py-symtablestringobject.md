# What's New In Python 3.10 / C API Changes / Removed — ast, symtable

`Py_SymtableStringObject()`

The `Py_SymtableString()` function had ended up in the stable ABI by mistake, yet it was unusable, since the `symtable.h` header file had been left out of the limited C API.

Turn to the Python [`symtable`](https://docs.python.org/3.14/library/symtable.html#module-symtable) module instead. (Contributed by Victor Stinner in [bpo-43244](https://bugs.python.org/issue?@action=redirect&bpo=43244).)

- Remove [`PyOS_ReadlineFunctionPointer()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyOS_ReadlineFunctionPointer) out of the limited C API headers and out of `python3.dll`, the library furnishing the stable ABI on Windows. Given that the function takes a `FILE*` argument, no guarantee can be made about its ABI stability. (Contributed by Petr Viktorin in [bpo-43868](https://bugs.python.org/issue?@action=redirect&bpo=43868).)

- Remove `ast.h`, `asdl.h`, and `Python-ast.h` header files. Those functions were undocumented as well as excluded from the limited C API. The bulk of names defined by these header files lacked a `Py` prefix and thus could spawn name conflicts. As one example, `Python-ast.h` defined a `Yield` macro that clashed with the `Yield` name relied on by the Windows `<winbase.h>` header. Turn to the Python [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) module instead. (Contributed by Victor Stinner in [bpo-43244](https://bugs.python.org/issue?@action=redirect&bpo=43244).)

- Remove the compiler and parser functions that use `struct _mod` type, given that the public AST C API was removed:

  - `PyAST_Compile()`

  - `PyAST_CompileEx()`

  - `PyAST_CompileObject()`

  - `PyFuture_FromAST()`

  - `PyFuture_FromASTObject()`

  - `PyParser_ASTFromFile()`

  - `PyParser_ASTFromFileObject()`

  - `PyParser_ASTFromFilename()`

  - `PyParser_ASTFromString()`

  - `PyParser_ASTFromStringObject()`

Those functions were undocumented as well as excluded from the limited C API. (Contributed by Victor Stinner in [bpo-43244](https://bugs.python.org/issue?@action=redirect&bpo=43244).)

- Remove the `pyarena.h` header file along with functions:

  - `PyArena_New()`

  - `PyArena_Free()`

  - `PyArena_Malloc()`

  - `PyArena_AddPyObject()`

[Subject index](INDEX.md) · [Previous source section](c-api-changes-removed-removed.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-pep-652-maintaining-the-stable-abi.md) · [Release/subject declaration](c-api-changes-removed-removed.md) · [Following release/subject continuation](removed-compiler-helper-apis.md)

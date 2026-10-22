# Python 3.10.0 alpha 7 / c api / compiler and parser

[bpo-43244](https://bugs.python.org/issue?@action=redirect&bpo=43244): Delete the `PyAST_Validate()` function. Constructing an AST object (`mod_ty` type) through the public C API is no longer feasible. That function had already been kept out of the limited C API ([**PEP 384**](https://peps.python.org/pep-0384/)). Victor Stinner wrote the patch.

[bpo-43244](https://bugs.python.org/issue?@action=redirect&bpo=43244): Delete the `pyarena.h` header file along with its functions:

  - `PyArena_New()`

  - `PyArena_Free()`

  - `PyArena_Malloc()`

  - `PyArena_AddPyObject()`

None of these functions were documented, all were kept out of the limited C API, and they served only the compiler internally. Victor Stinner wrote the patch.

[bpo-43244](https://bugs.python.org/issue?@action=redirect&bpo=43244): Delete the compiler and parser functions that depend on the `struct _mod` type, since the public AST C API is gone:

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

These functions went undocumented and stayed outside the limited C API. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

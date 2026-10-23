# ast - Compiler flags

### Compiler flags

You can hand the flags listed below to [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) to alter how a program gets compiled:

 ast.PyCF_ALLOW_TOP_LEVEL_AWAIT

Enables support for top-level `await`, `async for`, `async with` and async comprehensions.

Added in version 3.8.

 ast.PyCF_ONLY_AST

Builds and hands back an abstract syntax tree rather than a compiled code object.

 ast.PyCF_OPTIMIZED_AST

The returned AST is optimized according to the *optimize* argument in [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) or `ast.parse()`.

Added in version 3.13.

 ast.PyCF_TYPE_COMMENTS

Enables support for [**PEP 484**](https://peps.python.org/pep-0484/) and [**PEP 526**](https://peps.python.org/pep-0526/) style type comments (`# type: <type>`, `# type: ignore <stuff>`).

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](ast-dump-to-ast-compare.md) · [Continue](command-line-usage.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md)

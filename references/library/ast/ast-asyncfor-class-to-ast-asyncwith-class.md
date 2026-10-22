# ast: `ast.AsyncFor`, `ast.AsyncWith`

*class *ast.AsyncFor(*target*, *iter*, *body*, *orelse*, *type_comment*)

 *class *ast.AsyncWith(*items*, *body*, *type_comment*)

`async for` loops and `async with` context managers. Their fields are the same as those of `For` and `With`, in that order. Valid solely inside the body of an `AsyncFunctionDef`.

Note

Whenever `ast.parse()` parses a string, operator nodes (subclasses of `ast.operator`, `ast.unaryop`, `ast.cmpop`, `ast.boolop` and `ast.expr_context`) on the tree it returns are going to be singletons. A change to one of them shows up in every other appearance of that same value (take `ast.Add` as an example).

[Subject index](INDEX.md) · [Previous](ast-await-class.md) · [Continue](ast-parse.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Async and await](ast-asyncfunctiondef-class.md)

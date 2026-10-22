# ast: `ast.AST`

### Node classes

 *class *ast.AST

Every AST node class descends from this base. The concrete node classes themselves are generated out of the `Parser/Python.asdl` file shown above, declared in the `_ast` C module, and then re-exported through `ast`.

For every left-hand side symbol in the abstract grammar there is exactly one class (think `ast.stmt` or `ast.expr`). On top of that, each right-hand side constructor gets its own class, and those classes subclass the left-hand side trees they belong to. As an illustration, `ast.BinOp` derives from `ast.expr`. Where a production rule offers alternatives (so-called "sums"), the left-hand side class stays abstract: you only ever get instances of the particular constructor nodes.

[Subject index](INDEX.md) · [Previous](asdl-operators-patterns-and-type-parameters.md) · [Continue](node-classes.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md)

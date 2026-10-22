# ast: `ast.FunctionDef`

### Function and class definitions

 *class *ast.FunctionDef(*name*, *args*, *body*, *decorator_list*, *returns*, *type_comment*, *type_params*)

A function definition.

- `name` is a raw string of the function name.

- `args` is an `arguments` node.

- `body` is the list of nodes inside the function.

- `decorator_list` holds the decorators to apply, kept outermost first (so the one heading the list gets applied last).

- `returns` is the return annotation.

- `type_params` is a list of type parameters.

[Subject index](INDEX.md) · [Previous](ast-typevartuple-class.md) · [Continue](function-and-class-definitions.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md)

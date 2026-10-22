# ast: `ast.arguments`

*class *ast.arguments(*posonlyargs*, *args*, *vararg*, *kwonlyargs*, *kw_defaults*, *kwarg*, *defaults*)

The arguments for a function.

- `posonlyargs`, `args` and `kwonlyargs` are lists of `arg` nodes.

- `vararg` and `kwarg` are single `arg` nodes, pointing at the `*args, **kwargs` parameters.

- `kw_defaults` lists the default values for keyword-only arguments. Where one of them is `None`, its matching argument is mandatory.

- `defaults` lists the default values for arguments that may be supplied positionally. Where the defaults run short, they line up with the trailing n arguments.

[Subject index](INDEX.md) · [Previous](ast-lambda-class.md) · [Continue](ast-arg-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Function and class definitions](ast-functiondef-class.md)

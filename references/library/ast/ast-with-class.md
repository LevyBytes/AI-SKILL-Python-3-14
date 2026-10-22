# ast: `ast.With`

*class *ast.With(*items*, *body*, *type_comment*)

Represents a `with` block. The `items` field is a list of `withitem` nodes standing for the context managers, and `body` is the indented block held inside the context.

 type_comment

The `type_comment` field is an optional string carrying the type annotation written as a comment.

[Subject index](INDEX.md) · [Previous](ast-excepthandler-class.md) · [Continue](ast-withitem-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Control flow](ast-if-class.md)

# ast: `ast.Assign`

### Statements

 *class *ast.Assign(*targets*, *value*, *type_comment*)

Represents an assignment. The `targets` field is a list of nodes, whereas `value` is one node.

Having several nodes in `targets` means the same value is bound to each of them. Placing a `Tuple` or `List` inside `targets` expresses unpacking.

[Subject index](INDEX.md) · [Previous](ast-comprehension-class.md) · [Continue](statements.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md)

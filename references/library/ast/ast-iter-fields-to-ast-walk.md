# ast: `ast.iter_fields()`, `ast.iter_child_nodes()`, `ast.walk()`

ast.iter_fields(*node*)

For every field named in `node._fields` that actually exists on *node*, produce a `(fieldname, value)` tuple.

 ast.iter_child_nodes(*node*)

Produce each immediate child of *node* — meaning every field that holds a node, plus every element of fields whose value is a list of nodes.

 ast.walk(*node*)

Walk the tree rooted at *node* and produce every descendant it contains (*node* included), with no ordering guaranteed. This helps when all you intend is to alter nodes where they sit and the surrounding context is irrelevant.

[Subject index](INDEX.md) · [Previous](ast-unparse-to-ast-copy-location.md) · [Continue](ast-nodevisitor-class-to-ast-nodevisitor-visit-constant.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: `ast` helpers](ast-parse.md)

# ast: `ast.NodeVisitor`, `visit()`, `generic_visit()`, `visit_Constant()`

*class *ast.NodeVisitor

A base class for node visitors that traverses the abstract syntax tree and runs a visitor function against each node it encounters. Whatever that function returns is passed straight through by the `visit()` method.

You are expected to derive from this class, with your subclass contributing the visitor methods.

 visit(*node*)

Visit a node. Out of the box, it dispatches to the method named `self.visit_*classname*`, with *classname* being the node class’s name, falling back to `generic_visit()` whenever no such method is defined.

 generic_visit(*node*)

This visitor calls `visit()` on all children of the node.

Keep in mind that when a node has its own dedicated visitor method, that node’s children stay unvisited unless your visitor explicitly invokes `generic_visit()` or reaches them on its own.

 visit_Constant(*node*)

Handles all constant nodes.

Steer clear of `NodeVisitor` whenever your goal is to mutate nodes as you traverse. A purpose-built visitor (`NodeTransformer`) handles that and permits modifications.

Deprecated since version 3.8, removed in version 3.14: From Python 3.14 onward, the `visit_Num()`, `visit_Str()`, `visit_Bytes()`, `visit_NameConstant()` and `visit_Ellipsis()` methods no longer get invoked. Supply a `visit_Constant()` method in their place to cover every constant node.

[Subject index](INDEX.md) · [Previous](ast-iter-fields-to-ast-walk.md) · [Continue](ast-nodetransformer-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: `ast` helpers](ast-parse.md)

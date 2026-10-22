# ast: `ast.NodeTransformer`

*class *ast.NodeTransformer

A subclass of `NodeVisitor` that traverses the abstract syntax tree while permitting nodes to be changed.

As `NodeTransformer` traverses the AST, it takes whatever a visitor method returns and uses it to swap out or drop the existing node. A visitor method returning `None` causes the node to be deleted from its spot; any other return value takes the node’s place. That return value can even be the original node, in which event nothing is swapped at all.

The transformer below illustrates the idea by turning every name lookup (`foo`) into `data['foo']`:

```python
class RewriteName(NodeTransformer):

    def visit_Name(self, node):
        return Subscript(
            value=Name(id='data', ctx=Load()),
            slice=Constant(value=node.id),
            ctx=node.ctx
        )

```

Remember that should the node under your hand carry children, you are obliged either to transform those children yourself or to run the node’s `generic_visit()` method beforehand.

When a node belonged to a sequence of statements (which covers all statement nodes), your visitor is allowed to give back a list of nodes in place of one lone node.

Should `NodeTransformer` bring in fresh nodes (ones absent from the original tree) that lack location data like `lineno`, run `fix_missing_locations()` over the new sub-tree to work the location data out again:

```python
tree = ast.parse('foo', mode='eval')
new_tree = fix_missing_locations(RewriteName().visit(tree))

```

Usually you use the transformer like this:

```python
node = YourTransformer().visit(node)

```

[Subject index](INDEX.md) · [Previous](ast-nodevisitor-class-to-ast-nodevisitor-visit-constant.md) · [Continue](ast-dump-to-ast-compare.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: `ast` helpers](ast-parse.md)

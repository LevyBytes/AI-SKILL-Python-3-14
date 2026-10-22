# ast: `ast.parse()`

### `ast` helpers

Beyond the node classes, the `ast` module supplies these utility functions and classes for walking abstract syntax trees:

 ast.parse(*source*, *filename='&lt;unknown&gt;'*, *mode='exec'*, ***, *type_comments=False*, *feature_version=None*, *optimize=-1*)

Parse the source into an AST node. The same as `compile(source, filename, mode, flags=FLAGS_VALUE, optimize=optimize)`, in which `FLAGS_VALUE` is `ast.PyCF_ONLY_AST` when `optimize <= 0` and `ast.PyCF_OPTIMIZED_AST` in every other case.

When `type_comments=True` is supplied, the parser changes so that it checks and hands back type comments as laid out in [**PEP 484**](https://peps.python.org/pep-0484/) and [**PEP 526**](https://peps.python.org/pep-0526/). This amounts to adding `ast.PyCF_TYPE_COMMENTS` to the flags handed to [`compile()`](https://docs.python.org/3.14/library/functions.html#compile). Syntax errors get reported for type comments that sit in the wrong place. Lacking this flag, type comments are disregarded, and on the AST nodes that carry it the `type_comment` field stays `None` at all times. On top of that, the spots of `# type: ignore` comments come back as the `type_ignores` attribute on `Module` (which is otherwise forever an empty list).

On top of that, when `mode` is `'func_type'`, the input syntax shifts to line up with [**PEP 484**](https://peps.python.org/pep-0484/) "signature type comments", for instance `(str, int) -> List[str]`.

[Subject index](INDEX.md) · [Previous](ast-asyncfor-class-to-ast-asyncwith-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Required continuation of the source contract](ast-unparse-to-ast-copy-location.md)

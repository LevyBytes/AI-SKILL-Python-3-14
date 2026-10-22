# ast — `ast` — Abstract syntax trees

### `ast` — Abstract syntax trees

**Source code:** [Lib/ast.py](https://github.com/python/cpython/tree/3.14/Lib/ast.py)

---

Working with trees built from Python's abstract syntax grammar is what the `ast` module supports. Because that abstract syntax may be revised in any given Python release, the module gives you a programmatic way to discover the shape of the grammar that is in effect right now.

To build an abstract syntax tree, hand `ast.PyCF_ONLY_AST` as a flag to the [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) built-in, or call the module's own `parse()` helper. What you get back is a tree whose object classes all derive from `ast.AST`. Feeding such a tree to the built-in `compile()` function turns it into a Python code object.

[Subject index](INDEX.md) · [Continue](abstract-grammar-section-introduction-and-initial-examples.md)

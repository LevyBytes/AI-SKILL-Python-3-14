# 6.2.6. List displays

### 6.2.6. List displays

A list display is a series of expressions ? possibly empty ? surrounded by square brackets:

```text

list_display: "[" [flexible_expression_list | comprehension] "]"
```

A list display produces a brand-new list object whose contents come from either a list of expressions or a comprehension. Given a comma-separated list of expressions, the elements are evaluated left to right and dropped into the list object in that same order. Given a comprehension, the list is assembled from whatever elements the comprehension yields.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Previous source section](displays-for-lists-sets-and-dictionaries.md) · [Following source section](set-displays.md)

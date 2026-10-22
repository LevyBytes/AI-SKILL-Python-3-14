# 6.2.7. Set displays

### 6.2.7. Set displays

A set display is written with curly braces and is told apart from dictionary displays by having no colons dividing keys from values:

```text

set_display: "{" (flexible_expression_list | comprehension) "}"
```

A set display produces a new mutable set object whose contents are given by either a sequence of expressions or a comprehension. Given a comma-separated list of expressions, each element is evaluated left to right and inserted into the set object. Given a comprehension, the set is assembled from the elements the comprehension yields.

You cannot make an empty set using `{}`; that literal builds an empty dictionary instead.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Previous source section](list-displays.md) · [Following source section](dictionary-displays.md)

# 7.2.2. Annotated assignment statements

### 7.2.2. Annotated assignment statements

[Annotation](https://docs.python.org/3.14/glossary.html#term-variable-annotation) assignment merges, inside one statement, a variable or attribute annotation together with an optional assignment statement:

```text

annotated_assignment_stmt: augtarget ":" expression
                           "=" ([starred_expression | yield_expression)]
```

What sets this apart from ordinary Assignment statements is that just one target is permitted.

The assignment target counts as ?simple? when it is a single name not surrounded by parentheses. For simple assignment targets, when within class or module scope, the annotations are collected within a lazily evaluated [annotation scope](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes). Those annotations may be evaluated by way of the [`__annotations__`](https://docs.python.org/3.14/reference/datamodel.html#object.__annotations__) attribute of a class or module, or through the facilities in the [`annotationlib`](https://docs.python.org/3.14/library/annotationlib.html#module-annotationlib) module.

When the assignment target is not simple (an attribute, a subscript node, or a parenthesized name), the annotation is never evaluated.

When a name receives an annotation in a function scope, that name becomes local to that scope. Within function scopes, annotations are never evaluated nor stored.

When the right hand side is supplied, an annotated assignment carries out the actual assignment exactly as though no annotation were present. When the right hand side is absent for an expression target, the interpreter evaluates the target apart from the final [`__setitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setitem__) or [`__setattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setattr__) call.

See also

[**PEP 526**](https://peps.python.org/pep-0526/) - Syntax for Variable Annotations

The proposal that introduced syntax for marking up the types of variables (covering both class variables and instance variables), rather than conveying them by way of comments.

[**PEP 484**](https://peps.python.org/pep-0484/) - Type hints

The proposal that introduced the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module so as to supply a uniform syntax for type annotations usable by IDEs and static analysis tools.

Changed in version 3.8: Annotated assignments now permit, on their right hand side, every expression that regular assignments accept. Before this, certain expressions (such as un-parenthesized tuple expressions) triggered a syntax error.

Changed in version 3.14: Annotations are henceforth evaluated lazily within a distinct [annotation scope](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes). Should the assignment target fail to be simple, the annotations go unevaluated.

[Subject index](INDEX.md) · [Owning language section](simple-statements.md) · [Owning language section](assignment-statements.md) · [Previous source section](augmented-assignment-statements.md) · [Following source section](the-assert-statement.md)

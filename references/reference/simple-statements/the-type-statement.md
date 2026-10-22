# 7.14. The `type` statement

### 7.14. The `type` statement

```text

type_stmt: 'type' identifier [type_params] "=" expression
```

A type alias — an instance of [`typing.TypeAliasType`](https://docs.python.org/3.14/library/typing.html#typing.TypeAliasType) — is declared by the `type` statement.

To illustrate, the statement below builds a type alias:

```python
type Point = tuple[float, float]

```

Roughly speaking, that code amounts to:

```python
annotation-def VALUE_OF_Point():
    return tuple[float, float]
Point = typing.TypeAliasType("Point", VALUE_OF_Point())

```

What `annotation-def` marks is an [annotation scope](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes), which acts for the most part like a function aside from a few minor distinctions.

Evaluation of the type alias's value happens within the annotation scope. That evaluation does not occur as the type alias is built, but solely once the value is reached by way of the type alias's `__value__` attribute (consult [Lazy evaluation](https://docs.python.org/3.14/reference/executionmodel.html#lazy-evaluation)). Thanks to this, the type alias is able to mention names not yet defined.

You can turn type aliases generic by appending a [type parameter list](https://docs.python.org/3.14/reference/compound_stmts.html#type-params) behind the name. Turn to [Generic type aliases](https://docs.python.org/3.14/reference/compound_stmts.html#generic-type-aliases) for additional detail.

`type` counts as a [soft keyword](https://docs.python.org/3.14/reference/lexical_analysis.html#soft-keywords).

Added in version 3.12.

See also

[**PEP 695**](https://peps.python.org/pep-0695/) - Type Parameter Syntax

Brought in the `type` statement plus syntax covering generic classes and functions.

[Subject index](INDEX.md) · [Owning language section](simple-statements.md) · [Previous source section](the-nonlocal-statement.md)

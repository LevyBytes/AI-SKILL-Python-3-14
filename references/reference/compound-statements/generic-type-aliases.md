# 8.10.3. Generic type aliases

### 8.10.3. Generic type aliases

The [`type`](https://docs.python.org/3.14/reference/simple_stmts.html#type) statement can also serve to build a generic type alias:

```python
type ListOrSet[T] = list[T] | set[T]

```

Apart from the [lazy evaluation](https://docs.python.org/3.14/reference/executionmodel.html#lazy-evaluation) of the value, this is equivalent to:

```python
annotation-def TYPE_PARAMS_OF_ListOrSet():
    T = typing.TypeVar("T")

    annotation-def VALUE_OF_ListOrSet():
        return list[T] | set[T]
    # In reality, the value is lazily evaluated
    return typing.TypeAliasType("ListOrSet", VALUE_OF_ListOrSet(), type_params=(T,))
ListOrSet = TYPE_PARAMS_OF_ListOrSet()

```

Here, `annotation-def` (not a genuine keyword) marks an [annotation scope](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes). The capitalized names like `TYPE_PARAMS_OF_ListOrSet` are not actually bound at runtime.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](type-parameter-lists.md) · [Previous source section](generic-classes.md) · [Following source section](annotations.md)

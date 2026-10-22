# 8.10.2. Generic classes

### 8.10.2. Generic classes

Generic classes are declared as follows:

```python
class Bag[T]: ...

```

This syntax is equivalent to:

```python
annotation-def TYPE_PARAMS_OF_Bag():
    T = typing.TypeVar("T")
    class Bag(typing.Generic[T]):
        __type_params__ = (T,)
        ...
    return Bag
Bag = TYPE_PARAMS_OF_Bag()

```

Once more `annotation-def` (not a genuine keyword) marks an [annotation scope](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes), and the name `TYPE_PARAMS_OF_Bag` is in fact never bound at runtime.

Generic classes implicitly inherit from [`typing.Generic`](https://docs.python.org/3.14/library/typing.html#typing.Generic). A generic class’s base classes and keyword arguments are evaluated inside the type scope for the type parameters, while its decorators are evaluated outside that scope. The following example demonstrates this:

```python
@decorator
class Bag(Base[T], arg=T): ...

```

This is equivalent to:

```python
annotation-def TYPE_PARAMS_OF_Bag():
    T = typing.TypeVar("T")
    class Bag(Base[T], typing.Generic[T], arg=T):
        __type_params__ = (T,)
        ...
    return Bag
Bag = decorator(TYPE_PARAMS_OF_Bag())

```

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](type-parameter-lists.md) · [Previous source section](generic-functions.md) · [Following source section](generic-type-aliases.md)

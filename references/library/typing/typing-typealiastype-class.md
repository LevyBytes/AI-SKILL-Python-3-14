# typing: `typing.TypeAliasType`

*class *typing.TypeAliasType(*name*, *value*, ***, *type_params=()*)

The type of type aliases created through the [`type`](https://docs.python.org/3.14/reference/simple_stmts.html#type) statement.

Example:

```pycon
>>> type Alias = int
>>> type(Alias)
<class 'typing.TypeAliasType'>

```

Added in version 3.12.

 __name__

The name of the type alias:

```pycon
>>> type Alias = int
>>> Alias.__name__
'Alias'

```

 __module__

The name of the module in which the type alias was defined:

```python
>>> type Alias = int
>>> Alias.__module__
'__main__'

```

 __type_params__

The alias's type parameters; for a non-generic alias this is instead an empty tuple:

```pycon
>>> type ListOrSet[T] = list[T] | set[T]
>>> ListOrSet.__type_params__
(T,)
>>> type NotGeneric = int
>>> NotGeneric.__type_params__
()

```

 __value__

The value held by the type alias. Because it is [lazily evaluated](https://docs.python.org/3.14/reference/executionmodel.html#lazy-evaluation), any names appearing in the alias definition stay unresolved until something reads the `__value__` attribute:

```pycon
>>> type Mutually = Recursive
>>> type Recursive = Mutually
>>> Mutually
Mutually
>>> Recursive
Recursive
>>> Mutually.__value__
Recursive
>>> Recursive.__value__
Mutually

```

[Subject index](INDEX.md) · [Previous](typing-paramspecargs-class-to-typing-paramspeckwargs-class.md) · [Continue](typing-typealiastype-evaluate-value.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Building generic types and type aliases](typing-generic-class.md)

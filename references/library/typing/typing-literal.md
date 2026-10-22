# typing: `typing.Literal`

typing.Literal

Special typing form to define "literal types".

`Literal` lets you tell type checkers that the annotated object holds a value matching one of the literals you list.

For example:

```python
def validate_simple(data: Any) -> Literal[True]:  # always returns True
    ...

type Mode = Literal['r', 'rb', 'w', 'wb']
def open_helper(file: str, mode: Mode) -> str:
    ...

open_helper('/some/path', 'r')      # Passes type check
open_helper('/other/path', 'typo')  # Error in type checker

```

`Literal[...]` cannot be subclassed. When the program runs, any value at all is accepted as a type argument to `Literal[...]`, although type checkers may enforce their own limits. See [**PEP 586**](https://peps.python.org/pep-0586/) for more details about literal types.

Additional details:

- Each argument has to be a literal value, and you need to supply one or more.

- Nested `Literal` types are flattened, e.g.:

```python
assert Literal[Literal[1, 2], 3] == Literal[1, 2, 3]

```

This behavior is suspended, though, for `Literal` types reached by way of a type alias, so as not to compel evaluation of the `TypeAliasType` beneath:

```python
type A = Literal[1, 2]
assert Literal[A, 3] != Literal[1, 2, 3]

```

- Redundant arguments are skipped, e.g.:

```python
assert Literal[1, 2, 1] == Literal[1, 2]

```

- When comparing literals, the argument order is ignored, e.g.:

```python
assert Literal[1, 2] == Literal[2, 1]

```

- You cannot subclass or instantiate a `Literal`.

- You cannot write `Literal[X][Y]`.

Added in version 3.8.

Changed in version 3.9.1: `Literal` now strips duplicate parameters. Comparing `Literal` objects for equality no longer depends on order. A `Literal` object will now throw a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception when checked for equality if any of its parameters is not [hashable](https://docs.python.org/3.14/glossary.html#term-hashable).

[Subject index](INDEX.md) · [Previous](typing-optional-to-typing-concatenate.md) · [Continue](typing-classvar-to-typing-notrequired.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Special forms](typing-union-class.md)

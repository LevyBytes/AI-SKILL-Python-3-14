# typing: `typing.is_typeddict()`

typing.is_typeddict(*tp*)

Check if a type is a `TypedDict`.

For example:

```python
class Film(TypedDict):
    title: str
    year: int

assert is_typeddict(Film)
assert not is_typeddict(list | str)

# TypedDict is a factory for creating typed dicts,
# not a typed dict itself
assert not is_typeddict(TypedDict)

```

True is returned by this function solely for `TypedDict` classes, never for [generic aliases](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias) built from them:

```python
class GenericFilm[T](TypedDict):
    title: str
    year: T

assert not is_typeddict(GenericFilm[int])

```

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](typing-get-args-to-typing-is-protocol.md) · [Continue](typing-forwardref-class.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Introspection helpers](typing-get-type-hints-to-typing-get-origin.md)

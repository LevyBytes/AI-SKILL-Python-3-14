# typing: `typing.get_args()`, `typing.get_protocol_members()`, `typing.is_protocol()`

typing.get_args(*tp*)

Get type arguments once every substitution has been applied: given a typing object shaped like `X[Y, Z, ...]`, yield `(Y, Z, ...)`.

When `X` is a union or `Literal` nested inside another generic type, type caching can leave the order of `(Y, Z, ...)` differing from the order in the original arguments `[Y, Z, ...]`. For objects that are not supported, `()` comes back.

Examples:

```python
assert get_args(int) == ()
assert get_args(Dict[int, str]) == (int, str)
assert get_args(Union[int, str]) == (int, str)

```

Added in version 3.8.

 typing.get_protocol_members(*tp*)

Return the set of members defined in a `Protocol`.

```pycon
>>> from typing import Protocol, get_protocol_members
>>> class P(Protocol):
...     def a(self) -> str: ...
...     b: int
>>> get_protocol_members(P) == frozenset({'a', 'b'})
True

```

Raise [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) for arguments that are not Protocols.

Added in version 3.13.

 typing.is_protocol(*tp*)

Determine if a type is a `Protocol`.

For example:

```python
class P(Protocol):
    def a(self) -> str: ...
    b: int

assert is_protocol(P)
assert not is_protocol(int)

```

True is returned by this function solely for `Protocol` classes, never for [generic aliases](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias) built from them:

```python
class GenericP[T](Protocol):
    def a(self) -> T: ...
    b: int

assert not is_protocol(GenericP[int])

```

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](typing-get-type-hints-to-typing-get-origin.md) · [Continue](typing-is-typeddict.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Introspection helpers](typing-get-type-hints-to-typing-get-origin.md)

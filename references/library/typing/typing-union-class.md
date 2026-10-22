# typing: `typing.Union`

#### Special forms

The following may serve as types within annotations. Every one of them supports subscription via `[]`, though each carries its own distinct syntax.

 *class *typing.Union

Union type; `Union[X, Y]` is equivalent to `X | Y` and means either X or Y.

To build a union, write for instance `Union[int, str]` or the shorter form `int | str`. The shorter form is what we recommend. Details:

- Each argument has to be a type, and you need to supply one or more.

- Unions of unions are flattened, e.g.:

```python
Union[Union[int, str], float] == Union[int, str, float]

```

This behavior is suspended, though, for unions reached by way of a type alias, so as not to compel evaluation of the `TypeAliasType` beneath:

```python
type A = Union[int, str]
Union[A, float] != Union[int, str, float]

```

- Unions of a single argument vanish, e.g.:

```python
Union[int] == int  # The constructor actually returns int

```

- Redundant arguments are skipped, e.g.:

```python
Union[int, str, int] == Union[int, str] == int | str

```

- When comparing unions, the argument order is ignored, e.g.:

```python
Union[int, str] == Union[str, int]

```

- You cannot subclass or instantiate a `Union`.

- You cannot write `Union[X][Y]`.

Changed in version 3.7: Keep explicit subclasses inside unions at runtime instead of stripping them out.

Changed in version 3.10: A union may now take the form `X | Y`. See [union type expressions](https://docs.python.org/3.14/library/stdtypes.html#types-union).

Changed in version 3.14: [`types.UnionType`](https://docs.python.org/3.14/library/types.html#types.UnionType) now aliases `Union`, so that `Union[int, str]` along with `int | str` both yield instances of one and the same class. If you need to test at runtime whether some object is a `Union`, apply `isinstance(obj, Union)`. To stay compatible with older Python releases, apply `get_origin(obj) is typing.Union or get_origin(obj) is types.UnionType`.

[Subject index](INDEX.md) · [Previous](typing-typealias.md) · [Continue](typing-optional-to-typing-concatenate.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md)

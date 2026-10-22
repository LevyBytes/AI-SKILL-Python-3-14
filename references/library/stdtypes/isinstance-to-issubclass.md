# stdtypes / Generic Alias, Union / Union Type: `isinstance()`, `issubclass()`

isinstance(obj, union_object)

 issubclass(obj, union_object)

A union object is likewise accepted by calls to [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) and [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass):

```python
>>> isinstance("", int | str)
True

```

That said, you cannot run checks against parameterized generics inside union objects:

```python
>>> isinstance(1, int | list[int])  # short-circuit evaluation
True
>>> isinstance([1], int | list[int])
Traceback (most recent call last):
  ...
TypeError: isinstance() argument 2 cannot be a parameterized generic

```

The type that the union object exposes to users is reachable from [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union) and works in [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) checks:

```python
>>> import typing
>>> isinstance(int | str, typing.Union)
True
>>> typing.Union()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot create 'typing.Union' instances

```

Note

To enable the `X | Y` syntax, the `__or__()` method got added for type objects. When a metaclass supplies `__or__()`, that may take precedence over the Union:

```pycon
>>> class M(type):
...     def __or__(self, other):
...         return "Hello"
...
>>> class C(metaclass=M):
...     pass
...
>>> C | int
'Hello'
>>> int | C
int | C

```

See also

[**PEP 604**](https://peps.python.org/pep-0604/) – The PEP that put forward the `X | Y` syntax along with the Union type.

Added in version 3.10.

Changed in version 3.14: Union objects have become instances of [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union). Earlier they were instances of [`types.UnionType`](https://docs.python.org/3.14/library/types.html#types.UnionType), which stays an alias for `typing.Union`.

[Subject index](INDEX.md) · [Previous](union-type.md) · [Continue](other-built-in-types.md) · [Owning module, declaration or section: Union Type](union-type.md)

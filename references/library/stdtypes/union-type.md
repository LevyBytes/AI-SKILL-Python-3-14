# stdtypes: Union type construction and type-test behavior

### Union Type

A union object carries the result of applying the `|` (bitwise or) operation across several type objects. Such types serve mainly for [type annotations](https://docs.python.org/3.14/glossary.html#term-annotation). Writing a union type expression gives you tidier type-hinting syntax than subscripting [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union) does.

 X | Y | ...

Builds a union object that carries the types *X*, *Y*, and any others. `X | Y` stands for either X or Y. This is the same as `typing.Union[X, Y]`. To illustrate, the function below anticipates an argument typed as [`int`](https://docs.python.org/3.14/library/functions.html#int) or [`float`](https://docs.python.org/3.14/library/functions.html#float):

```python
def square(number: int | float) -> int | float:
    return number ** 2

```

Note

You cannot rely on the `|` operand at runtime to build unions in which one or more members is a forward reference. To illustrate, `int | "Foo"`, where `"Foo"` points at a class that has not yet been defined, breaks at runtime. When a union needs to take in forward references, write the entire expression as a string, for instance `"int | Foo"`.

 union_object == other

You can check union objects for equality against other union objects. The specifics:

- Nested unions get flattened out:

```python
(int | str) | float == int | str | float

```

- Duplicate types are dropped:

```python
int | str | int == int | str

```

- Ordering plays no part when unions are compared:

```python
int | str == str | int

```

- It produces instances of [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union):

```python
int | str == typing.Union[int, str]
type(int | str) is typing.Union

```

- You can write optional types as a union together with `None`:

```python
str | None == typing.Optional[str]

```

[Subject index](INDEX.md) · [Previous](genericalias-origin-to-genericalias-unpacked.md) · [Continue](isinstance-to-issubclass.md)

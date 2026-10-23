# typing - Building generic types and type aliases - Code example: a = concatenate('one', 'two')

```python
a = concatenate('one', 'two')
reveal_type(a)  # revealed type is str

b = concatenate(StringSubclass('one'), StringSubclass('two'))
reveal_type(b)  # revealed type is str, despite StringSubclass being passed in

c = concatenate('one', b'two')  # error: type variable 'A' can be either str or bytes in a function call, but not both

```

While running, `isinstance(x, T)` will raise [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

[Subject index](INDEX.md) · [Previous](typing-typevar-class.md) · [Continue](typing-typevar-evaluate-bound-to-typing-typevar-has-default.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: typing.TypeVar](typing-typevar-class.md) · [Owning module, declaration or section: Building generic types and type aliases](typing-generic-class.md)

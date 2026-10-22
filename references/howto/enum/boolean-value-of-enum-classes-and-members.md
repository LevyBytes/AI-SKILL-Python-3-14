# Boolean value of `Enum` classes and members

### Boolean value of `Enum` classes and members

Enum classes mixed with non-[`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) types (for example [`int`](https://docs.python.org/3.14/library/functions.html#int), [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), etc.) follow the boolean rules of the mixed-in type; in every other case, all members evaluate as [`True`](https://docs.python.org/3.14/library/constants.html#True). If you want your own enum’s boolean result to hinge on the member’s value, add this to your class:

```python
def __bool__(self):
    return bool(self.value)

```

Bare [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) classes invariably evaluate as [`True`](https://docs.python.org/3.14/library/constants.html#True).

[Subject index](INDEX.md) · [Previous source context](creating-members-that-are-mixed-with-other-data-types.md) · [Following source context](enum-classes-with-methods.md)

# What's New In Python 3.2 / reprlib — reprlib

### reprlib

Authors of a [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) method on a custom container frequently overlook the situation in which one of the members points back at the container. The builtin types in Python, including [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) and [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), cope with self-reference by printing — at the recursive position of the representation string.

To ease the job of writing those [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) methods, [`reprlib`](https://docs.python.org/3.14/library/reprlib.html#module-reprlib) now ships a decorator named [`recursive_repr()`](https://docs.python.org/3.14/library/reprlib.html#reprlib.recursive_repr), which spots recursive invocations of `__repr__()` and swaps in a placeholder string in their place:

```python
>>> class MyList(list):
...     @recursive_repr()
...     def __repr__(self):
...         return '<' + '|'.join(map(repr, self)) + '>'
...
>>> m = MyList('abc')
>>> m.append(m)
>>> m.append('x')
>>> print(m)
<'a'|'b'|'c'|...|'x'>

```

(Contributed by Raymond Hettinger in [bpo-9826](https://bugs.python.org/issue?@action=redirect&bpo=9826) and [bpo-9840](https://bugs.python.org/issue?@action=redirect&bpo=9840).)

[Subject index](INDEX.md) · [Previous source section](io.md) · [Next source section](logging.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)

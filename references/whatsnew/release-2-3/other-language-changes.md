# What’s New in Python 2.3 / Other Language Changes - types

### Other Language Changes

What follows are all the changes Python 2.3 introduces to the core Python language.

- As covered in this document's PEP 255: Simple Generators section, the [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) statement is now always a keyword.

- A fresh built-in function [`enumerate()`](https://docs.python.org/3.14/library/functions.html#enumerate) arrived, covered in this document's PEP 279: enumerate() section.

- Alongside the built-in [`bool`](https://docs.python.org/3.14/library/functions.html#bool) type, two new constants — [`True`](https://docs.python.org/3.14/library/constants.html#True) and [`False`](https://docs.python.org/3.14/library/constants.html#False) — were added, as this document's PEP 285: A Boolean Type section describes.

- Rather than raising an [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) when a string or floating-point number won't fit into an integer, the [`int()`](https://docs.python.org/3.14/library/functions.html#int) type constructor now hands back a long integer instead. The odd upshot is that `isinstance(int(expression), int)` can come out false, though that's unlikely to cause anyone real trouble.

- The built-in types now accept the extended slicing syntax, as this document's Extended Slices section describes.

- A new built-in function, `sum(iterable, start=0)`, totals the numeric items in the iterable object and returns the result. [`sum()`](https://docs.python.org/3.14/library/functions.html#sum) takes numbers only, so you can't lean on it to join a pile of strings together. (Contributed by Alex Martelli.)

- When *pos* was negative, `list.insert(pos, value)` previously stuck *value* at the front of the list. That behavior is now lined up with slice indexing, so a *pos* of -1 inserts the value just before the final element, and so on.

- `list.index(value)`, which hunts for *value* in the list and returns where it sits, now accepts optional *start* and *stop* arguments to confine the search to a portion of the list.

- A new dictionary method, `pop(key[, *default*])`, returns the value tied to *key* and drops that key/value pair from the dictionary. When the asked-for key is missing, *default* comes back if you supplied it and otherwise [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised.

```python
>>> d = {1:2}
>>> d
{1: 2}
>>> d.pop(4)
Traceback (most recent call last):
  File "stdin", line 1, in ?
KeyError: 4
>>> d.pop(1)
2
>>> d.pop(1)
Traceback (most recent call last):
  File "stdin", line 1, in ?
KeyError: 'pop(): dictionary is empty'
>>> d
{}
>>>

```

A new class method, `dict.fromkeys(iterable, value)`, also exists; it builds a dictionary whose keys come from the given iterator *iterable* with every value set to *value*, which defaults to `None`.

(Patches contributed by Raymond Hettinger.)

On top of that, the [`dict()`](https://docs.python.org/3.14/library/stdtypes.html#dict) constructor now takes keyword arguments to make assembling small dictionaries easier:

```python
>>> dict(red=1, blue=2, green=3, black=4)
{'blue': 2, 'black': 4, 'green': 3, 'red': 1}

```

(Contributed by Just van Rossum.)

- Because the [`assert`](https://docs.python.org/3.14/reference/simple_stmts.html#assert) statement no longer consults the `__debug__` flag, assigning to `__debug__` won't switch assertions off anymore. Running Python under the [`-O`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-O) switch still produces code that skips every assertion.

- Since most type objects are now callable, you can employ them to make new objects — functions, classes, and modules among them. (Consequently the `new` module could be deprecated in some future Python release, given that you can now reach for the type objects in the [`types`](https://docs.python.org/3.14/library/types.html#module-types) module.) For instance, the following code spins up a new module object:

[Subject index](INDEX.md) · [Previous source section](extended-slices-fakeseq.md) · [Next source section](pending-deprecation-warnings.md) · [Release/subject declaration](standard-set-type.md)

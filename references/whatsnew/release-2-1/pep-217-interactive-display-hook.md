# What’s New in Python 2.1 / PEP 217: Interactive Display Hook — sys

### PEP 217: Interactive Display Hook

When you work with the Python interpreter interactively, command output is shown via the built-in [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) function. Under Python 2.1, the [`sys.displayhook()`](https://docs.python.org/3.14/library/sys.html#sys.displayhook) variable can be assigned a callable object that gets called in place of `repr()`. You might, for example, point it at a special pretty-printing function:

```python
>>> # Create a recursive data structure
... L = [1,2,3]
>>> L.append(L)
>>> L # Show Python's default output
[1, 2, 3, [...]]
>>> # Use pprint.pprint() as the display function
... import sys, pprint
>>> sys.displayhook = pprint.pprint
>>> L
[1, 2, 3,  <Recursion on list with id=135143996>]
>>>

```

See also

[**PEP 217**](https://peps.python.org/pep-0217/) - Display Hook for Interactive Use

Written and implemented by Moshe Zadka.

[Subject index](INDEX.md) · [Previous source section](pep-235-importing-modules-on-case-insensitive-platforms.md) · [Next source section](pep-208-new-coercion-model.md) · [Release/subject declaration](introduction.md)

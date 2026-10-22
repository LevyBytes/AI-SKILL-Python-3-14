# What’s New in Python 2.6 / PEP 3105: `print` As a Function

### PEP 3105: `print` As a Function

Within Python 3.0 the `print` statement turns into the [`print()`](https://docs.python.org/3.14/library/functions.html#print) function. Once `print()` is a function, you gain the ability to swap it out with `def print(...)` or to pull in a replacement function from elsewhere.

Python 2.6 ships a `__future__` import that strips `print` from the language grammar, allowing you to adopt the functional spelling in its place. Here is one example:

```python
>>> from __future__ import print_function
>>> print('# of entries', len(dictionary), file=sys.stderr)

```

This is the new function's signature:

```python
def print(*args, sep=' ', end='\n', file=None)

```

Each parameter does the following:

- *args*: positional arguments whose values get printed.

- *sep*: the separator that gets printed in between arguments.

- *end*: the trailing text that gets printed once every argument has been emitted.

- *file*: the file object the output is directed to.

See also

[**PEP 3105**](https://peps.python.org/pep-3105/) - Make print a function

PEP written by Georg Brandl.

[Subject index](INDEX.md) · [Previous source section](pep-3101-advanced-string-formatting-d-to.md) · [Next source section](pep-3110-exception-handling-changes.md) · [Release/subject declaration](python-3-0.md)

# What’s New in Python 2.3 / PEP 279: enumerate()

### PEP 279: enumerate()

Certain loops read more cleanly thanks to a new built-in function, [`enumerate()`](https://docs.python.org/3.14/library/functions.html#enumerate). Given `enumerate(thing)`, where *thing* is some iterator or sequence, you get back an iterator yielding `(0, thing[0])`, `(1, thing[1])`, `(2, thing[2])`, on through the rest.

Here is a frequent pattern for altering every entry in a list:

```python
for i in range(len(L)):
    item = L[i]
    # ... compute some result based on item ...
    L[i] = result

```

With [`enumerate()`](https://docs.python.org/3.14/library/functions.html#enumerate) that turns into:

```python
for i, item in enumerate(L):
    # ... compute some result based on item ...
    L[i] = result

```

See also

[**PEP 279**](https://peps.python.org/pep-0279/) - The enumerate() built-in function

Written and implemented by Raymond D. Hettinger.

[Subject index](INDEX.md) · [Previous source section](pep-278-universal-newline-support.md) · [Next source section](pep-282-the-logging-package.md) · [Release/subject declaration](standard-set-type.md)

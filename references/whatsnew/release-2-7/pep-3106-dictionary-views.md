# What’s New in Python 2.7 / PEP 3106: Dictionary Views

Altering what [`keys()`](https://docs.python.org/3.14/library/stdtypes.html#dict.keys), [`values()`](https://docs.python.org/3.14/library/stdtypes.html#dict.values), and [`items()`](https://docs.python.org/3.14/library/stdtypes.html#dict.items) hand back was off the table for Python 2.7, since the breakage across existing code would have been enormous. The 3.x behavior was therefore exposed instead under fresh names: `viewkeys()`, `viewvalues()`, and `viewitems()`.

```python
>>> d = dict((i*10, chr(65+i)) for i in range(26))
>>> d
{0: 'A', 130: 'N', 10: 'B', 140: 'O', 20: ..., 250: 'Z'}
>>> d.viewkeys()
dict_keys([0, 130, 10, 140, 20, 150, 30, ..., 250])

```

You can loop over a view, and the key and item views additionally act like sets. Intersection is done with the `&` operator, while `|` yields a union:

```python
>>> d1 = dict((i*10, chr(65+i)) for i in range(26))
>>> d2 = dict((i**.5, i) for i in range(1000))
>>> d1.viewkeys() & d2.viewkeys()
set([0.0, 10.0, 20.0, 30.0])
>>> d1.viewkeys() | range(0, 30)
set([0, 1, 130, 3, 4, 5, 6, ..., 120, 250])

```

A view stays linked to its dictionary, so it reflects whatever changes are made to that dictionary:

```python
>>> vk = d.viewkeys()
>>> vk
dict_keys([0, 130, 10, ..., 250])
>>> d[260] = '&'
>>> vk
dict_keys([0, 130, 260, 10, ..., 250])

```

Be aware, though, that inserting or dropping keys is not permitted while a loop over the view is in progress:

```python
>>> for k in vk:
...     d[k*2] = k
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: dictionary changed size during iteration

```

Feel free to call the view methods from Python 2.x source; the 2to3 converter will rewrite them into the usual [`keys()`](https://docs.python.org/3.14/library/stdtypes.html#dict.keys), [`values()`](https://docs.python.org/3.14/library/stdtypes.html#dict.values), and [`items()`](https://docs.python.org/3.14/library/stdtypes.html#dict.items) calls.

See also

[**PEP 3106**](https://peps.python.org/pep-3106/) - Revamping dict.keys(), .values() and .items()

The PEP itself was authored by Guido van Rossum; the 2.7 back-port was the work of Alexandre Vassalotti, tracked at [bpo-1967](https://bugs.python.org/issue?@action=redirect&bpo=1967).

### PEP 3106: Dictionary Views

In Python 3.x the dictionary methods [`keys()`](https://docs.python.org/3.14/library/stdtypes.html#dict.keys), [`values()`](https://docs.python.org/3.14/library/stdtypes.html#dict.values), and [`items()`](https://docs.python.org/3.14/library/stdtypes.html#dict.items) behave differently. Instead of a fully materialized list, they hand back an object termed a *view*.

[Subject index](INDEX.md) · [Next source section](pep-3137-the-memoryview-object.md) · [Release/subject declaration](the-future-for-python-2-x.md) · [Previous source section](pep-391-dictionary-based-configuration-for-logging.md)

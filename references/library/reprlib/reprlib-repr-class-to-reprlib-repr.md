# reprlib — `reprlib` — Alternate `repr()` implementation

## reprlib — Alternate repr() implementation

### `reprlib` — Alternate [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) implementation

**Source code:** [Lib/reprlib.py](https://github.com/python/cpython/tree/3.14/Lib/reprlib.py)

---

A way to build object representations whose resulting strings stay within size limits is offered by the `reprlib` module. The Python debugger leans on this, and it can prove handy in other settings too.

This module supplies a class, an instance, and a function:

 *class *reprlib.Repr(***, *maxlevel=6*, *maxtuple=6*, *maxlist=6*, *maxarray=5*, *maxdict=4*, *maxset=6*, *maxfrozenset=6*, *maxdeque=6*, *maxstring=30*, *maxlong=40*, *maxother=30*, *fillvalue='...'*, *indent=None*)

A class that offers formatting helpers handy for writing functions akin to the built-in [`repr()`](https://docs.python.org/3.14/library/functions.html#repr); to keep representations from getting excessively long, size limits per object type are included.

You can treat the constructor's keyword arguments as a shortcut for assigning the attributes of the `Repr` instance. So the following initialization:

```python
aRepr = reprlib.Repr(maxlevel=3)

```

Is equivalent to:

```python
aRepr = reprlib.Repr()
aRepr.maxlevel = 3

```

Refer to the section Repr Objects for further details about `Repr` attributes.

Changed in version 3.12: Permit keyword arguments as a way to assign attributes.

 reprlib.aRepr

This is an instance of `Repr` that backs the `repr()` function covered below. If you change this object's attributes, you affect the size limits that `repr()` and the Python debugger apply.

 reprlib.repr(*obj*)

This is the `repr()` method belonging to `aRepr`. It hands back a string resembling what the built-in function of the same name returns, except most sizes are capped.

Beyond size-limiting helpers, the module also ships a decorator that catches recursive calls into [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) and puts a placeholder string in their place.

 @reprlib.recursive_repr(*fillvalue='...'*)

A decorator for [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) methods that spots recursive calls inside one thread. When a recursive call happens, the *fillvalue* is handed back; otherwise the regular `__repr__()` call proceeds. Take this example:

```pycon
>>> from reprlib import recursive_repr
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

Added in version 3.2.

[Subject index](INDEX.md) · [Continue](repr-fillvalue-to-repr-maxother.md)

# What’s New in Python 2.3 / PEP 285: A Boolean Type

The main reason Booleans landed in Python was readability. Suppose you're studying some function and run across `return 1` — you'd have no way to tell whether that `1` stands for a Boolean truth value, an index into something, or a coefficient applied to another quantity. Swap in `return True` and the intent of the returned value becomes obvious.

Strict type-checking was *not* the motivation behind Python's Booleans. A rigidly typed language like Pascal would, for instance, block you from doing arithmetic on Booleans and would insist that any [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if) statement's expression resolve to a Boolean. Python does not enforce that and won't in the future, a point [**PEP 285**](https://peps.python.org/pep-0285/) makes outright. As a result, any expression at all remains valid in an `if` statement, including ones yielding a list, a tuple, or some arbitrary object. Because the Boolean type derives from the [`int`](https://docs.python.org/3.14/library/functions.html#int) class, arithmetic involving a Boolean continues to function.

```python
>>> True + 1
2
>>> False + 1
1
>>> False * 75
0
>>> True * 75
75

```

Stating it briefly: [`True`](https://docs.python.org/3.14/library/constants.html#True) and [`False`](https://docs.python.org/3.14/library/constants.html#False) are simply different spellings for the integers 1 and 0, the sole distinction being that [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) and [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) hand back the strings `'True'` and `'False'` rather than `'1'` and `'0'`.

See also

[**PEP 285**](https://peps.python.org/pep-0285/) - Adding a bool type

Written and implemented by GvR.

### PEP 285: A Boolean Type

Python 2.3 picked up a Boolean type. The `__builtin__` module gained two new constants, [`True`](https://docs.python.org/3.14/library/constants.html#True) and [`False`](https://docs.python.org/3.14/library/constants.html#False). (Although `True` and `False` constants had already entered the built-ins back in Python 2.2.1, those 2.2.1 versions merely take the integer values 1 and 0 and do not form a separate type.)

[`bool`](https://docs.python.org/3.14/library/functions.html#bool) is the name of the type object representing this new type; its constructor accepts any Python value and turns it into either [`True`](https://docs.python.org/3.14/library/constants.html#True) or [`False`](https://docs.python.org/3.14/library/constants.html#False).

```python
>>> bool(1)
True
>>> bool(0)
False
>>> bool([])
False
>>> bool( (1,) )
True

```

The majority of the standard library modules along with the built-in functions were adjusted to hand back Booleans.

```python
>>> obj = []
>>> hasattr(obj, 'append')
True
>>> isinstance(obj, list)
True
>>> isinstance(obj, tuple)
False

```

[Subject index](INDEX.md) · [Next source section](pep-293-codec-error-handling-callbacks.md) · [Release/subject declaration](standard-set-type.md) · [Previous source section](pep-282-the-logging-package.md)

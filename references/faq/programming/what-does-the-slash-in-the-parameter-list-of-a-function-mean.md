# What does the slash(/) in the parameter list of a function mean?

### What does the slash(/) in the parameter list of a function mean?

When a slash appears in a function's argument list, it signals that the parameters preceding it are positional-only. Such positional-only parameters lack any name that callers can use externally. When you invoke a function that takes positional-only parameters, the arguments bind to parameters purely by their position. As an illustration, [`divmod()`](https://docs.python.org/3.14/library/functions.html#divmod) is a function whose parameters are positional-only. Here is what its documentation shows:

```python
>>> help(divmod)
Help on built-in function divmod in module builtins:

divmod(x, y, /)
    Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.

```

Having the slash at the close of the parameter list indicates that both parameters are positional-only. Consequently, invoking [`divmod()`](https://docs.python.org/3.14/library/functions.html#divmod) with keyword arguments produces an error:

```python
>>> divmod(x=3, y=4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: divmod() takes no keyword arguments

```

[Subject index](INDEX.md)

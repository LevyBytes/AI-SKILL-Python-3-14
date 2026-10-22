# What’s New In Python 3.8 / Positional-only parameters — collections, statistics

### Positional-only parameters

A new parameter-list marker, `/`, signals that certain function parameters can only be passed by position and may not be supplied as keyword arguments. That very notation already turns up in the `help()` output for C functions wired through Larry Hastings’ [Argument Clinic](https://devguide.python.org/development-tools/clinic/) tool.

Below, parameters *a* and *b* accept positional arguments only; *c* or *d* work either positionally or by keyword; and *e* or *f* must arrive as keywords:

```python
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

```

This call works fine:

```python
f(10, 20, 30, d=40, e=50, f=60)

```

By contrast, the next two calls fail:

```python
f(10, b=20, c=30, d=40, e=50, f=60)   # b cannot be a keyword argument
f(10, 20, 30, 40, 50, f=60)           # e must be a keyword argument

```

Why reach for this marker? It lets functions written in pure Python reproduce, exactly, how existing C-coded functions behave. Take the built-in [`divmod()`](https://docs.python.org/3.14/library/functions.html#divmod) function, which rejects keyword arguments:

```python
def divmod(a, b, /):
    "Emulate the built in divmod() function"
    return (a // b, a % b)

```

It also helps when a parameter name carries no useful meaning, so you may as well forbid passing it by keyword. The builtin [`len()`](https://docs.python.org/3.14/library/functions.html#len) function, for instance, carries the signature `len(obj, /)`, which blocks clumsy invocations like:

```python
len(obj='hello')  # The "obj" keyword argument impairs readability

```

There is a further upside: once a parameter is positional-only, you can rename it later without endangering anybody’s calling code. Consider the [`statistics`](https://docs.python.org/3.14/library/statistics.html#module-statistics) module, whose parameter named *dist* might get a different name down the road. The following signature is what makes that flexibility safe:

```python
def quantiles(dist, /, *, n=4, method='exclusive')
    ...

```

Because anything sitting left of `/` is never surfaced as a keyword, those parameter names stay free to reappear inside `**kwargs`:

```python
>>> def f(a, b, /, **kwargs):
...     print(a, b, kwargs)
...
>>> f(10, 20, a=1, b=2, c=3)         # a and b are used in two ways
10 20 {'a': 1, 'b': 2, 'c': 3}

```

That makes writing functions and methods that must swallow arbitrary keyword arguments far less painful. As an illustration, look at this snippet lifted from the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module:

```python
class Counter(dict):

    def __init__(self, iterable=None, /, **kwds):
        # Note "iterable" is a possible keyword argument

```

A complete write-up appears in [**PEP 570**](https://peps.python.org/pep-0570/).

(Pablo Galindo landed this feature in [bpo-36540](https://bugs.python.org/issue?@action=redirect&bpo=36540).)

[Subject index](INDEX.md) · [Previous source section](assignment-expressions.md) · [Next source section](parallel-filesystem-cache-for-compiled-bytecode-files.md) · [Release/subject declaration](assignment-expressions.md)

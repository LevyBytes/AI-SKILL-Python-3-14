# What’s New In Python 3.1 / Porting to Python 3.1

### Porting to Python 3.1

Below is a roundup of the earlier-noted adjustments, along with additional fixes, that could oblige you to update your own source:

- Reworked rendering of floating-point values as strings may invalidate doctests you already have. Consider this case:

```python
def e():
    '''Compute the base of natural logarithms.

    >>> e()
    2.7182818284590451

    '''
    return sum(1/math.factorial(x) for x in reversed(range(30)))

doctest.testmod()

**********************************************************************
Failed example:
    e()
Expected:
    2.7182818284590451
Got:
    2.718281828459045
**********************************************************************

```

- Because the pickle module silently remaps names under protocol 2 and below, pickles produced by Python 3.1 may fail to load on Python 3.0. You can address this either by switching to protocol 3, or by turning the *fix_imports* option to `False`. Refer to the earlier explanation for fuller coverage.

[Subject index](INDEX.md) · [Previous source section](build-and-c-api-changes.md) · [Release/subject declaration](pep-372-ordered-dictionaries.md)

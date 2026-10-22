# doctest — `doctest` — Test interactive Python examples — Section introduction and initial examples

### `doctest` — Test interactive Python examples

**Source code:** [Lib/doctest.py](https://github.com/python/cpython/tree/3.14/Lib/doctest.py)

---

The `doctest` module hunts through text for fragments resembling interactive Python sessions, then runs each one to confirm it behaves precisely the way the example claims. People typically reach for doctest in a handful of ways:

- Confirm that a module's docstrings remain current, by re-running every interactive example to ensure it still behaves as documented.

- Carry out regression testing, checking that the interactive examples drawn from a test file or test object behave the way they should.

- Compose tutorial-style documentation for a package, generously seasoned with input-output examples. Whether the spotlight falls on the examples or on the explanatory prose, the result feels like either "literate testing" or "executable documentation".

What follows is a complete, though compact, example module:

```python
"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()

```

Invoke `example.py` straight from the command line and `doctest` quietly does its job:

[Subject index](INDEX.md) · [Continue](interactive-example-testing-command.md)

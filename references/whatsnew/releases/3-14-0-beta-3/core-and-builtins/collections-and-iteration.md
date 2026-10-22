# Python 3.14.0 beta 3 / core and builtins / collections and iteration

[gh-135171](https://github.com/python/cpython/issues/135171): For async generator expressions created from an object lacking an __aiter__ method, the behavior is reverted to the pre-3.13 behavior of raising a TypeError.

[gh-135171](https://github.com/python/cpython/issues/135171): For generator expressions created from a non-iterable, the behavior is reverted to the pre-3.13 behavior of raising a TypeError. Crashing the debugger by mutating the generator expression’s local variables is no longer possible. This works by shifting the `GET_ITER` instruction back to where the generator expression is created and inserting an extra check into `FOR_ITER`.

[gh-127682](https://github.com/python/cpython/issues/127682): Stop invoking `__iter__` a second time within list comprehensions. List comprehensions now match how the rest of Python's iteration forms behave

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

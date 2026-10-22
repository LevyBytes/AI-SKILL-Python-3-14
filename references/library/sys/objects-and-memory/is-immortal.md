# sys._is_immortal

sys._is_immortal(*op*)

Return [`True`](https://docs.python.org/3.14/library/constants.html#True) when the supplied object is [immortal](https://docs.python.org/3.14/glossary.html#term-immortal), and [`False`](https://docs.python.org/3.14/library/constants.html#False) when it is not.

Note

Objects that are immortal today (and therefore yield `True` when handed to this function) carry no guarantee of remaining immortal in later versions, and the same caveat applies in reverse for mortal objects.

Added in version 3.14.

**CPython implementation detail:** Reserve this function for specialized purposes alone. There is no guarantee that it exists across every Python implementation.

[API family](INDEX.md) · [sys context index](../INDEX.md).

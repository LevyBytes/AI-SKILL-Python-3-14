# sys._is_gil_enabled

sys._is_gil_enabled()

Hand back [`True`](https://docs.python.org/3.14/library/constants.html#True) when the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) is enabled and [`False`](https://docs.python.org/3.14/library/constants.html#False) when it is disabled.

Added in version 3.13.

**CPython implementation detail:** There is no guarantee that it exists across every Python implementation.

[API family](INDEX.md) · [sys context index](../INDEX.md).

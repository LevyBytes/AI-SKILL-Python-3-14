# Python 3.13.0 alpha 3 / core and builtins / functions

[gh-90350](https://github.com/python/cpython/issues/90350): Sped up the builtin functions [`min()`](https://docs.python.org/3.14/library/functions.html#min) and [`max()`](https://docs.python.org/3.14/library/functions.html#max).

[gh-74616](https://github.com/python/cpython/issues/74616): [`input()`](https://docs.python.org/3.14/library/functions.html#input) will now raise a ValueError, rather than quietly truncating, when writing to the terminal and the prompt holds embedded null characters.

[gh-113212](https://github.com/python/cpython/issues/113212): Made the [`super`](https://docs.python.org/3.14/library/functions.html#super) error messages clearer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

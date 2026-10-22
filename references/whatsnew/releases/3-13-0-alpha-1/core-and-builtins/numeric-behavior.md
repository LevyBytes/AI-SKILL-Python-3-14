# Python 3.13.0 alpha 1 / core and builtins / numeric behavior

[gh-109923](https://github.com/python/cpython/issues/109923): A line number is now assigned to the `POP_TOP` that comes after a `RETURN_GENERATOR`.

[gh-109369](https://github.com/python/cpython/issues/109369): The internal eval_breaker plus its supporting flags, along with the monitoring version, were folded into one atomic integer to make the checks quicker.

[gh-105549](https://github.com/python/cpython/issues/105549): Emit `NUMBER` and `NAME` tokens as separate, unambiguous tokens. Pablo Galindo supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

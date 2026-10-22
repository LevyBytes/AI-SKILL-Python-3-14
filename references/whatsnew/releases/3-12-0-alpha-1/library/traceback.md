# Python 3.12.0 alpha 1 / library / traceback

[gh-87822](https://github.com/python/cpython/issues/87822): While invoked using `capture_locals=True`, the [`traceback`](https://docs.python.org/3.14/library/traceback.html#module-traceback) module routines now absorb exceptions thrown by `repr()` calls on frames' local variables. The point is to favor the original exception ahead of rendering failures. A note about the failure prints where the absent value would sit. (Simon-Martin Schroeder wrote the patch).

[gh-97008](https://github.com/python/cpython/issues/97008): The pure Python [`traceback`](https://docs.python.org/3.14/library/traceback.html#module-traceback) module now also emits the [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) and [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) spelling suggestions added under [gh-82711](https://github.com/python/cpython/issues/82711). Their tests now run against both implementations to verify they match. Carl Friedrich Bolz-Tereick and ??ukasz Langa wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

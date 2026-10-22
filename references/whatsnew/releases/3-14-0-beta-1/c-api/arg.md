# Python 3.14.0 beta 1 / c api / arg

[gh-132987](https://github.com/python/cpython/issues/132987): Within [`PyArg_Parse()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_Parse), the `k` and `K` formats have gained support for the [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) special method, putting them on par with the remaining integer formats.

[gh-132909](https://github.com/python/cpython/issues/132909): An overflow that occurred while processing the [K](https://docs.python.org/3.14/c-api/arg.html#capi-py-buildvalue-format-k) format within [`Py_BuildValue()`](https://docs.python.org/3.14/c-api/arg.html#c.Py_BuildValue) is now fixed. Bénédikt Tran supplied the patch.

[gh-112068](https://github.com/python/cpython/issues/112068): [Reverted in [gh-136991](https://github.com/python/cpython/issues/136991)] Nullable arguments are now accepted by [`PyArg_Parse()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_Parse) and related functions. Appending `?` after any format unit lets `None` be taken as a value.

[gh-50333](https://github.com/python/cpython/issues/50333): Passing non-tuple sequences as the argument for the `(items)` format unit inside [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) and the other [argument parsing](https://docs.python.org/3.14/c-api/arg.html#arg-parsing) functions is now deprecated whenever *items* holds format units that retain a [borrowed buffer](https://docs.python.org/3.14/c-api/arg.html#c-arg-borrowed-buffer) or a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

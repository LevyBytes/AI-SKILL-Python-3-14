# Python 3.13.0 alpha 3 / c api / arg

[gh-112438](https://github.com/python/cpython/issues/112438): Make the format units "es", "et", "es#", and "et#" work inside nested tuples passed to [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple)-like functions.

[gh-65210](https://github.com/python/cpython/issues/65210): Revise how the *keywords* parameter is declared on [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTupleAndKeywords) and [`PyArg_VaParseTupleAndKeywords()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_VaParseTupleAndKeywords) to play more nicely with C++.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

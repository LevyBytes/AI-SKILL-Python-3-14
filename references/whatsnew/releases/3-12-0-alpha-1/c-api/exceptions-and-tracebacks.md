# Python 3.12.0 alpha 1 / c api / exceptions and tracebacks

[gh-93466](https://github.com/python/cpython/issues/93466): A PyType_Spec may not list the same Slot ID twice, and the docs were amended to say so. In certain repeated-slot scenarios, PyType_FromSpec and its companions will now raise an exception.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

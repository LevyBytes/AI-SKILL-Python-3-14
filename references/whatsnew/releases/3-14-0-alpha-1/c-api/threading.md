# Python 3.14.0 alpha 1 / c api / threading

[gh-119247](https://github.com/python/cpython/issues/119247): Added the `Py_BEGIN_CRITICAL_SECTION_SEQUENCE_FAST` and `Py_END_CRITICAL_SECTION_SEQUENCE_FAST` macros so the PySequence_Fast APIs can be used safely under free-threading, and reworked str.join to run GIL-free through them.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

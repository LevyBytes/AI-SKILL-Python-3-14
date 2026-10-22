# Python 3.12.0 alpha 1 / c api / provide c overloads py cast impl cope null letting c extensions

[gh-93442](https://github.com/python/cpython/issues/93442): Provide C++ overloads of _Py_CAST_impl() that cope with 0/NULL, letting C++ extensions that feed 0 or NULL into macros built on _Py_CAST() keep compiling.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

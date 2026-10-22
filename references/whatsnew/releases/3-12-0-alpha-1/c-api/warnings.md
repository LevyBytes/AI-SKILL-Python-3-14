# Python 3.12.0 alpha 1 / c api / warnings

[gh-92898](https://github.com/python/cpython/issues/92898): Silence the C++ compiler warnings produced when function arguments are cast to `PyObject*`. Serge Guelton wrote the patch.

[gh-94731](https://github.com/python/cpython/issues/94731): Under a C++ compiler, Python once more applies C-style casts to the majority of cast operations. That can set off compiler warnings where the `-Wold-style-cast` or `-Wzero-as-null-pointer-constant` options are turned on for `g++`, for instance.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

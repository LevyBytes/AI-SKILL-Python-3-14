# Python 3.13.0 beta 1 / c api / intro

[gh-118124](https://github.com/python/cpython/issues/118124): Correct [`Py_BUILD_ASSERT`](https://docs.python.org/3.14/c-api/intro.html#c.Py_BUILD_ASSERT) plus [`Py_BUILD_ASSERT_EXPR`](https://docs.python.org/3.14/c-api/intro.html#c.Py_BUILD_ASSERT_EXPR) so non-constant expressions work: on C11 and later they rely on `static_assert()`. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

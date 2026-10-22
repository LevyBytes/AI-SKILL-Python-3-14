# Python 3.12.0 alpha 3 / c api / stable

[gh-98680](https://github.com/python/cpython/issues/98680): The `PyBUF_*` constants were flagged as belonging to the Limited API of Python 3.11+. They shipped in 3.11.0 with [`Py_LIMITED_API`](https://docs.python.org/3.14/c-api/stable.html#c.Py_LIMITED_API) set for 3.11, and the buffer API can't be used without them.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

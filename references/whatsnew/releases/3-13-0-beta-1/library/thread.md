# Python 3.13.0 beta 1 / library / thread

[gh-76785](https://github.com/python/cpython/issues/76785): The low-level `_interpreters` module has been surfaced to support the PyPI implementation of [**PEP 734**](https://peps.python.org/pep-0734/). At times it had been reachable as the `_xxsubinterpreters` module and previously served testing only. Generally it ought to be treated as internal, alongside `_thread` and `_imp`. Refer to [https://discuss.python.org/t/pep-734-multiple-interpreters-in-the-stdlib/41147/26](https://discuss.python.org/t/pep-734-multiple-interpreters-in-the-stdlib/41147/26).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

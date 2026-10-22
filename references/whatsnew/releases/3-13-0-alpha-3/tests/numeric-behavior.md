# Python 3.13.0 alpha 3 / tests / numeric behavior

[gh-111801](https://github.com/python/cpython/issues/111801): Drop the recursion ceiling inside `test_isinstance` for `test_infinitely_many_bases()`, which stops a stack overflow on a WASI pydebug build.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.0 alpha 2 / core and builtins / leave tally peek items out pyuop num popped

[gh-126222](https://github.com/python/cpython/issues/126222): Leave the tally of "peek" items out of `_PyUop_num_popped`. Doing so guarantees the right count of items is popped off the stack whenever a micro-op exits carrying an error.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

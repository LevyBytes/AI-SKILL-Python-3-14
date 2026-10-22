# Python 3.12.0 alpha 5 / core and builtins / dis

[gh-100762](https://github.com/python/cpython/issues/100762): Store the (virtual) exception block depth inside the oparg of [`YIELD_VALUE`](https://docs.python.org/3.14/library/dis.html#opcode-YIELD_VALUE). That lets us skip the costly `throw()` when shutting down generators (and coroutines) that close trivially.

[gh-100923](https://github.com/python/cpython/issues/100923): Drop the `mask` cache entry belonging to the [`COMPARE_OP`](https://docs.python.org/3.14/library/dis.html#opcode-COMPARE_OP) instruction and fold the mask straight into the oparg.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

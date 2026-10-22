# Python 3.13.0 alpha 2 / core and builtins / dis

[gh-111354](https://github.com/python/cpython/issues/111354): For [`YIELD_VALUE`](https://docs.python.org/3.14/library/dis.html#opcode-YIELD_VALUE), the oparg is `1` whenever the instruction belongs to a yield-from or await, and `0` otherwise.

The SUSPENDED frame state has been divided into `SUSPENDED` and `SUSPENDED_YIELD_FROM`. That streamlines the `_PyGen_yf` code.

[gh-111354](https://github.com/python/cpython/issues/111354): Drop `oparg` from [`YIELD_VALUE`](https://docs.python.org/3.14/library/dis.html#opcode-YIELD_VALUE). Adjust the `oparg` of [`RESUME`](https://docs.python.org/3.14/library/dis.html#opcode-RESUME) to carry except-depth information. With these changes, the code within generator close can be simplified.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

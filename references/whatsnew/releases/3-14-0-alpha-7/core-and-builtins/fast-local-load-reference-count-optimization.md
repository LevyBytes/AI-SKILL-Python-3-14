# Python 3.14.0 alpha 7 / core and builtins / tunes load fast together superinstruction variant reference counting costs less

[gh-130704](https://github.com/python/cpython/issues/130704): Tunes `LOAD_FAST` together with its superinstruction variant so that reference counting costs less. Swapped in are quicker versions that push borrowed references onto the operand stack whenever it can be shown that the frame's reference outlasts the one placed on the stack.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

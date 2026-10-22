# Python 3.14.0 alpha 1 / core and builtins / dis

[gh-122160](https://github.com/python/cpython/issues/122160): Drop the `BUILD_CONST_KEY_MAP` opcode. Reach for [`BUILD_MAP`](https://docs.python.org/3.14/library/dis.html#opcode-BUILD_MAP) in its place.

[gh-123048](https://github.com/python/cpython/issues/123048): Address a defect where pattern matching code might emit a [`JUMP_FORWARD`](https://docs.python.org/3.14/library/dis.html#opcode-JUMP_FORWARD) carrying no source location.

[gh-118093](https://github.com/python/cpython/issues/118093): Provide three specializations for [`CALL_KW`](https://docs.python.org/3.14/library/dis.html#opcode-CALL_KW):

  - `CALL_KW_PY` for calls to Python functions

  - `CALL_KW_BOUND_METHOD` for calls to bound methods

  - `CALL_KW_NON_PY` for all other calls

[gh-120507](https://github.com/python/cpython/issues/120507): Drop the `BEFORE_WITH` and `BEFORE_ASYNC_WITH` instructions. Bring in the new [`LOAD_SPECIAL`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_SPECIAL) instruction. Use that new instruction when generating code for `with` and `async with` statements.

[gh-119180](https://github.com/python/cpython/issues/119180): Swap the `LOAD_ASSERTION_ERROR` opcode for [`LOAD_COMMON_CONSTANT`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_COMMON_CONSTANT), plus add backing for [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

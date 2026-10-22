# Python 3.13.0 alpha 1 / core and builtins / dis

[gh-109216](https://github.com/python/cpython/issues/109216): A possible memory leak in [`BUILD_MAP`](https://docs.python.org/3.14/library/dis.html#opcode-BUILD_MAP) is now fixed.

[gh-105848](https://github.com/python/cpython/issues/105848): A fresh [`CALL_KW`](https://docs.python.org/3.14/library/dis.html#opcode-CALL_KW) opcode was added for calls that include keyword arguments. A possible crash while stepping over method calls in a debugger was also fixed.

[gh-104909](https://github.com/python/cpython/issues/104909): Break the [`LOAD_GLOBAL`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_GLOBAL) specializations apart into micro-ops.

[gh-100288](https://github.com/python/cpython/issues/100288): Specialize [`LOAD_ATTR`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_ATTR) for non-descriptors residing on the class. This brings in `LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES` along with `LOAD_ATTR_NONDESCRIPTOR_NO_DICT`.

[gh-105775](https://github.com/python/cpython/issues/105775): [`LOAD_CLOSURE`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_CLOSURE) has become a pseudo-op.

[gh-106003](https://github.com/python/cpython/issues/106003): Introduce a fresh [`TO_BOOL`](https://docs.python.org/3.14/library/dis.html#opcode-TO_BOOL) instruction that carries out boolean conversions on behalf of [`POP_JUMP_IF_TRUE`](https://docs.python.org/3.14/library/dis.html#opcode-POP_JUMP_IF_TRUE), [`POP_JUMP_IF_FALSE`](https://docs.python.org/3.14/library/dis.html#opcode-POP_JUMP_IF_FALSE), and [`UNARY_NOT`](https://docs.python.org/3.14/library/dis.html#opcode-UNARY_NOT) (every one of which henceforth requires exact [`bool`](https://docs.python.org/3.14/library/functions.html#bool) values). On top of that, adjust the oparg of [`COMPARE_OP`](https://docs.python.org/3.14/library/dis.html#opcode-COMPARE_OP) so it can carry an optional "boolean conversion" flag.

[gh-104635](https://github.com/python/cpython/issues/104635): Remove redundant [`STORE_FAST`](https://docs.python.org/3.14/library/dis.html#opcode-STORE_FAST) instructions from the compiler. Donghee Na and Carl Meyer prepared the patch.

[gh-107901](https://github.com/python/cpython/issues/107901): A missing line number on [`JUMP_BACKWARD`](https://docs.python.org/3.14/library/dis.html#opcode-JUMP_BACKWARD) at the tail of a for loop is now fixed.

[gh-105848](https://github.com/python/cpython/issues/105848): The bytecode was changed so the real callable for a [`CALL`](https://docs.python.org/3.14/library/dis.html#opcode-CALL) sits at a consistent stack position (whether or not bound-method-calling optimizations are in effect).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

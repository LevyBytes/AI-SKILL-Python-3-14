# Python 3.12.0 alpha 2 / core and builtins / veryhigh

[gh-96421](https://github.com/python/cpython/issues/96421): Whenever C code enters Python code by way of [`PyEval_EvalFrameEx()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyEval_EvalFrameEx) or some related C-API function, a shim frame gets pushed onto the call stack. That happens inside the `_PyEval_EvalFrameDefault()` function. While the additional frame stays hidden from all Python and from the majority of C extensions, profilers and debuggers operating out-of-process must account for it. You can spot such shim frames by testing `frame->owner == FRAME_OWNED_BY_CSTACK`.

Extensions that build their own interpreters via PEP 523 have to account for this shim frame as well as the revised semantics of [`RETURN_VALUE`](https://docs.python.org/3.14/library/dis.html#opcode-RETURN_VALUE), [`YIELD_VALUE`](https://docs.python.org/3.14/library/dis.html#opcode-YIELD_VALUE), and [`RETURN_GENERATOR`](https://docs.python.org/3.14/library/dis.html#opcode-RETURN_GENERATOR), all of which now clear the frame.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

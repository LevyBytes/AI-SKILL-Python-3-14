# Python 3.12.0 alpha 4 / core and builtins / compiler and parser

[gh-100146](https://github.com/python/cpython/issues/100146): The `BUILD_LIST` opcode is improved to behave like the `BUILD_TUPLE` opcode: it grabs references off the stack directly rather than driving stack operations over and over to assign each list slot. The mechanics live in a fresh private API, `_PyList_FromArraySteal()`.

[gh-99554](https://github.com/python/cpython/issues/99554): During bytecode compilation, the debugging location tables are now packed in a more compact way.

[gh-100222](https://github.com/python/cpython/issues/100222): Recast the `_Py_CODEUNIT` typedef as a union so its layout is spelled out for the C compiler, sidestepping type punning and reading more clearly.

[gh-99955](https://github.com/python/cpython/issues/99955): The internal compiler functions in compile.c now uniformly hand back -1 upon error and 0 upon success.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

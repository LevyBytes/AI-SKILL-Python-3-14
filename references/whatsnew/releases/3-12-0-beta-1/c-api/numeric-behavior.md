# Python 3.12.0 beta 1 / c api / numeric behavior

[gh-96803](https://github.com/python/cpython/issues/96803): Within the limited API, add unstable C-API calls for retrieving the code object, lasti, and line number out of the internal `_PyInterpreterFrame`. Those functions are:

  - `PyCodeObject * PyUnstable_InterpreterFrame_GetCode(struct _PyInterpreterFrame *frame)`

  - `int PyUnstable_InterpreterFrame_GetLasti(struct _PyInterpreterFrame *frame)`

  - `int PyUnstable_InterpreterFrame_GetLine(struct _PyInterpreterFrame *frame)`

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

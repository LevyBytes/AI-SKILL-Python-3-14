# frame objects C API: `PyUnstable_InterpreterFrame_GetCode()`, `PyUnstable_InterpreterFrame_GetLasti()`, `PyUnstable_InterpreterFrame_GetLine()`

struct _PyInterpreterFrame

How the interpreter represents a frame internally.

Added in version 3.11.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnstable_InterpreterFrame_GetCode(struct _PyInterpreterFrame *frame);

 *Counts as [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). Minor releases may alter it with no advance notice.*

>

Hand back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) pointing at the frame's code object.

Added in version 3.12.

 int PyUnstable_InterpreterFrame_GetLasti(struct _PyInterpreterFrame *frame);

 *Counts as [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). Minor releases may alter it with no advance notice.*

Hand back the byte offset reaching into the most recently executed instruction.

Added in version 3.12.

 int PyUnstable_InterpreterFrame_GetLine(struct _PyInterpreterFrame *frame);

 *Counts as [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). Minor releases may alter it with no advance notice.*

Hand back the line number running at present, or -1 where no line number exists.

Added in version 3.12.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyframeobject-to-pyframe-getgenerator.md) · [Owning C API section and shared conditions](internal-frames.md)

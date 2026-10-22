# inspect: `inspect.getinnerframes()`, `inspect.currentframe()`, `inspect.stack()`, `inspect.trace()`

inspect.getinnerframes(*traceback*, *context=1*)

Obtain a list of `FrameInfo` objects spanning a traceback’s frame plus all the frames nested within it. Those frames stand for calls triggered as a downstream effect of *frame*. The opening element of the list corresponds to *traceback*, and the closing one corresponds to the spot where the exception got raised.

Changed in version 3.5: What comes back is a list of [named tuples](https://docs.python.org/3.14/glossary.html#term-named-tuple), each shaped as `FrameInfo(frame, filename, lineno, function, code_context, index)`.

Changed in version 3.11: The result is now a list of `FrameInfo` objects.

 inspect.currentframe()

Hand back the frame object belonging to the caller’s own stack frame.

**CPython implementation detail:** This routine depends on the interpreter offering Python stack frame support, something that not every Python implementation is promised to provide. Should it run under an implementation lacking Python stack frame support, the call yields `None`.

 inspect.stack(*context=1*)

Hand back a list of `FrameInfo` objects describing the caller’s stack. The leading element of the returned list maps to the caller, while the trailing one maps to the outermost call sitting on the stack.

Changed in version 3.5: What comes back is a list of [named tuples](https://docs.python.org/3.14/glossary.html#term-named-tuple), each shaped as `FrameInfo(frame, filename, lineno, function, code_context, index)`.

Changed in version 3.11: The result is now a list of `FrameInfo` objects.

 inspect.trace(*context=1*)

Hand back a list of `FrameInfo` objects covering the stack that lies between the current frame and the frame where an exception now being handled was originally raised. The leading element of the list maps to the caller, while the trailing one maps to the place the exception was raised.

Changed in version 3.5: What comes back is a list of [named tuples](https://docs.python.org/3.14/glossary.html#term-named-tuple), each shaped as `FrameInfo(frame, filename, lineno, function, code_context, index)`.

Changed in version 3.11: The result is now a list of `FrameInfo` objects.

[Subject index](INDEX.md) · [Previous](inspect-getouterframes.md) · [Continue](inspect-getattr-static.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md) · [Owning module, declaration or section: The interpreter stack](inspect-frameinfo-class.md)

# Python 3.13.0 beta 1 / core and builtins / frame

[gh-74929](https://github.com/python/cpython/issues/74929): Realize PEP 667: [`FrameType.f_locals`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_locals) along with [`PyFrame_GetLocals()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLocals) were changed to hand back a write-through proxy object whenever the frame points at a function or comprehension.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.12.0 alpha 1 / c api / frame

[gh-93937](https://github.com/python/cpython/issues/93937): These frame functions and the frame type can now be reached straight from `#include <Python.h>`, so pulling in `#include <frameobject.h>` is no longer required:

  - [`PyFrame_Check()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_Check)

  - [`PyFrame_GetBack()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetBack)

  - [`PyFrame_GetBuiltins()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetBuiltins)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

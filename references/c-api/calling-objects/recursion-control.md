# Recursion Control

### Recursion Control

With *tp_call* in play, the callee has no [recursion](https://docs.python.org/3.14/c-api/exceptions.html#recursion) concerns: for any call routed through *tp_call*, CPython itself wraps things with [`Py_EnterRecursiveCall()`](https://docs.python.org/3.14/c-api/exceptions.html#c.Py_EnterRecursiveCall) and [`Py_LeaveRecursiveCall()`](https://docs.python.org/3.14/c-api/exceptions.html#c.Py_LeaveRecursiveCall).

To stay efficient, vectorcall calls skip that automatic handling, so the callee itself ought to invoke *Py_EnterRecursiveCall* and *Py_LeaveRecursiveCall* where appropriate.

[Subject index](INDEX.md) · [Previous source contract](pyobject.md) · [Following source contract](pyvectorcall-nargs-to-pyvectorcall-call.md)

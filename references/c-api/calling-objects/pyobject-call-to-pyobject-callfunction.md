# calling objects C API: `PyObject_Call()`, `PyObject_CallNoArgs()`, `PyObject_CallOneArg()`, `PyObject_CallObject()`, `PyObject_CallFunction()`

### Object Calling API

A range of functions exists for invoking a Python object. Every one of them adapts its arguments into a convention the target object handles — *tp_call* or else vectorcall. To minimize how much conversion happens, choose whichever one aligns best with the shape of data you already hold.

What follows is a table recapping the functions on offer; consult each function's own documentation for the specifics.

| Function | callable | args | kwargs |
| --- | --- | --- | --- |
| `PyObject_Call()` | `PyObject *` | tuple | dict/`NULL` |
| `PyObject_CallNoArgs()` | `PyObject *` | — | — |
| `PyObject_CallOneArg()` | `PyObject *` | 1 object | — |
| `PyObject_CallObject()` | `PyObject *` | tuple/`NULL` | — |
| `PyObject_CallFunction()` | `PyObject *` | format | — |
| `PyObject_CallMethod()` | obj + `char*` | format | — |
| `PyObject_CallFunctionObjArgs()` | `PyObject *` | variadic | — |
| `PyObject_CallMethodObjArgs()` | obj + name | variadic | — |
| `PyObject_CallMethodNoArgs()` | obj + name | — | — |
| `PyObject_CallMethodOneArg()` | obj + name | 1 object | — |
| `PyObject_Vectorcall()` | `PyObject *` | vectorcall | vectorcall |
| `PyObject_VectorcallDict()` | `PyObject *` | vectorcall | dict/`NULL` |
| `PyObject_VectorcallMethod()` | arg + name | vectorcall | vectorcall |

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_Call([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *callable, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *args, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *kwargs)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Invoke the callable Python object *callable*, where the tuple *args* supplies the arguments and the dictionary *kwargs* supplies the named ones.

Here *args* may not be *NULL*; pass an empty tuple when nothing is required. Should no named arguments be needed, *kwargs* is allowed to be *NULL*.

On success the call's result comes back; should it fail, an exception is raised and *NULL* is returned.

This is the equivalent of the Python expression: `callable(*args, **kwargs)`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_CallNoArgs([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *callable)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Invoke the callable Python object *callable* passing nothing at all. For invoking such an object argument-free, no faster route exists.

On success the call's result comes back; should it fail, an exception is raised and *NULL* is returned.

Added in version 3.9.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_CallOneArg([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *callable, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *arg)

*Return value: New reference.*

Invoke the callable Python object *callable* handing it precisely 1 positional argument *arg* while omitting keyword arguments.

On success the call's result comes back; should it fail, an exception is raised and *NULL* is returned.

Added in version 3.9.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_CallObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *callable, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *args)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Invoke the callable Python object *callable*, with the tuple *args* furnishing its arguments. When no arguments are wanted, *args* is permitted to be *NULL*.

On success the call's result comes back; should it fail, an exception is raised and *NULL* is returned.

This is the equivalent of the Python expression: `callable(*args)`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_CallFunction([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *callable, const char *format, ...)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Invoke the callable Python object *callable* while supplying a varying count of C arguments. You spell out those C arguments through a [`Py_BuildValue()`](https://docs.python.org/3.14/c-api/arg.html#c.Py_BuildValue) -style format string. A *NULL* format signals that no arguments are being passed.

On success the call's result comes back; should it fail, an exception is raised and *NULL* is returned.

This is the equivalent of the Python expression: `callable(*args)`.

Bear in mind that when your arguments are solely [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)* values, `PyObject_CallFunctionObjArgs()` runs faster.

Changed in version 3.4: The *format* type, formerly `char *`, was revised.

[Subject index](INDEX.md) · [Previous source contract](pyvectorcall-nargs-to-pyvectorcall-call.md) · [Following source contract](pyobject-callmethod-to-pyobject-vectorcallmethod.md)

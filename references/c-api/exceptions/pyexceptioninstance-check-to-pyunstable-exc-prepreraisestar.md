# Exception Objects

### Exception Objects

 int PyExceptionInstance_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

Hand back true when *op* is an instance of [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException), and false otherwise. This function always succeeds.

 PyExceptionInstance_Class(op)

The same as [`Py_TYPE(op)`](https://docs.python.org/3.14/c-api/structures.html#c.Py_TYPE).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyException_GetTraceback([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ex)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the traceback tied to the exception as a new reference, the same one reachable from Python through the [`__traceback__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__traceback__) attribute. When no traceback is tied to it, this hands back `NULL`.

 int PyException_SetTraceback([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ex, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *tb)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Attach *tb* as the traceback tied to the exception. Pass `Py_None` to clear it.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyException_GetContext([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ex)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the context (a separate exception instance during whose handling *ex* was raised) tied to the exception as a new reference, the same one reachable from Python through the [`__context__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__context__) attribute. When no context is tied to it, this hands back `NULL`.

 void PyException_SetContext([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ex, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ctx)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Attach *ctx* as the context tied to the exception. Pass `NULL` to clear it. No type check is performed to confirm that *ctx* is an exception instance. This steals a reference to *ctx*.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyException_GetCause([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ex)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the cause (either an exception instance, or `None`, established via `raise ... from ...`) tied to the exception as a new reference, the same one reachable from Python through the [`__cause__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__cause__) attribute.

 void PyException_SetCause([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ex, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *cause)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Attach *cause* as the cause tied to the exception. Pass `NULL` to clear it. Whether *cause* happens to be `None` or an exception instance goes unverified by any type check. This steals a reference to *cause*.

The [`__suppress_context__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__suppress_context__) attribute is set implicitly to `True` by this function.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyException_GetArgs([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ex)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

Hand back the [`args`](https://docs.python.org/3.14/library/exceptions.html#BaseException.args) of exception *ex*.

 void PyException_SetArgs([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ex, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *args)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

Assign *args* as the [`args`](https://docs.python.org/3.14/library/exceptions.html#BaseException.args) of exception *ex*.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnstable_Exc_PrepReraiseStar([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *orig, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *excs)

 *This is [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). It may change without warning in minor releases.*

Carry out part of how the interpreter implements `except*`. Here *orig* is the original caught exception, and *excs* is the list of exceptions awaiting being raised. That list holds the unhandled portion of *orig*, if there is one, together with the exceptions raised from the `except*` clauses (which therefore carry a traceback distinct from *orig*) and those reraised (which therefore share the traceback of *orig*). Hand back the [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup) that ultimately needs reraising, or `None` when there is nothing to reraise.

Added in version 3.12.

[Subject index](INDEX.md) · [Previous source contract](pyerr-newexception-to-pyexceptionclass-name.md) · [Following source contract](unicode-exception-objects.md)

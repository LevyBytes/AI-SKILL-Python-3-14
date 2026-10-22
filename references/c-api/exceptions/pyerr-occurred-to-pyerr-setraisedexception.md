# exceptions C API: `PyErr_Occurred()`, `PyErr_ExceptionMatches()`, `PyErr_GivenExceptionMatches()`, `PyErr_GetRaisedException()`, `PyErr_SetRaisedException()`

### Querying the error indicator

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_Occurred()

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Check whether the error indicator has been set. When it has, hand back the exception *type* (the first argument from the most recent call to a `PyErr_Set*` function or to `PyErr_Restore()`). Otherwise hand back `NULL`. The reference to the returned value is not yours, so there is no need to [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) it.

An [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is required of the caller.

Note

Don't match the returned value against a particular exception; reach for `PyErr_ExceptionMatches()` instead, as illustrated below. (Such a direct comparison may readily go wrong, because the exception could be an instance rather than a class when the exception is a class one, or it might be a subclass of the one you expected.)

 int PyErr_ExceptionMatches([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The same as `PyErr_GivenExceptionMatches(PyErr_Occurred(), exc)`. Only invoke this while an exception is genuinely set; otherwise a memory access violation results because no exception has been raised.

 int PyErr_GivenExceptionMatches([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *given, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back true whenever the *given* exception lines up with the exception type held in *exc*. Should *exc* be a class object, the result is also true when *given* is an instance of one of its subclasses. Should *exc* be a tuple, every exception type within that tuple (and, recursively, within nested subtuples) is checked for a match.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_GetRaisedException(void)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

Hand back whichever exception is presently being raised, while at the same time clearing the error indicator. Hand back `NULL` should the error indicator not be set.

Code that has to trap exceptions, or that has to temporarily stash and later restore the error indicator, relies on this function.

For example:

```c
{
   PyObject *exc = PyErr_GetRaisedException();

   /* ... code that might produce other errors ... */

   PyErr_SetRaisedException(exc);
}

```

See also

`PyErr_GetHandledException()`, to save the exception currently being handled.

Added in version 3.12.

 void PyErr_SetRaisedException([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

Make *exc* the exception that is presently being raised, discarding any existing exception that is already set.

Warning

This call appropriates a reference to *exc*, and that *exc* has to be a valid exception.

Added in version 3.12.

[Subject index](INDEX.md) · [Previous source contract](pyerr-warnformat-to-pyerr-resourcewarning.md) · [Following source contract](pyerr-fetch-to-pyerr-sethandledexception.md)

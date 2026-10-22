# exceptions C API: `PyErr_Fetch()`, `PyErr_Restore()`, `PyErr_NormalizeException()`, `PyErr_GetHandledException()`, `PyErr_SetHandledException()`

void PyErr_Fetch([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **ptype, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **pvalue, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **ptraceback)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Deprecated since version 3.12: Use `PyErr_GetRaisedException()` instead.

Pull the error indicator out into the three variables whose addresses you supply. When the error indicator is unset, all three variables are set to `NULL`. When it is set, it gets cleared and you hold a reference to every object pulled out. Even where the type object is not `NULL`, the value and traceback object can still be `NULL`.

Note

Typically only legacy code reaches for this function, where that code has to trap exceptions or briefly stash and reinstate the error indicator.

For example:

```c
{
   PyObject *type, *value, *traceback;
   PyErr_Fetch(&type, &value, &traceback);

   /* ... code that might produce other errors ... */

   PyErr_Restore(type, value, traceback);
}

```

 void PyErr_Restore([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *type, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *traceback)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Deprecated since version 3.12: Use `PyErr_SetRaisedException()` instead.

Build the error indicator from the trio of objects *type*, *value*, and *traceback*, discarding any existing exception that is already set. Should the objects be `NULL`, the error indicator gets cleared. Never supply a `NULL` type together with a non-`NULL` value or traceback. The exception type ought to be a class. Never supply an invalid exception type or value. (Breaking these rules leads to subtle problems down the line.) This call takes away a reference to each object: you must hold a reference to each object going in, and once the call returns you no longer hold those references. (If this is unclear to you, steer clear of this function. I warned you.)

Note

Typically only legacy code reaches for this function, where that code has to briefly stash and reinstate the error indicator. Reach for `PyErr_Fetch()` to stash the present error indicator.

 void PyErr_NormalizeException([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **exc, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **val, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **tb)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Deprecated since version 3.12: To steer clear of any potential de-normalization, reach for `PyErr_GetRaisedException()` instead.

In some situations the values handed back by `PyErr_Fetch()` below may be "unnormalized", which is to say `*exc` is a class object yet `*val` is not an instance of that same class. In such a case this function can instantiate the class. When the values are already normalized, it does nothing. This deferred normalization exists for performance reasons.

Note

On the exception value, this function *does not* implicitly assign the [`__traceback__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__traceback__) attribute. Where you want the traceback set correctly, this extra snippet becomes necessary:

```c
if (tb != NULL) {
  PyException_SetTraceback(val, tb);
}

```

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_GetHandledException(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Fetch the active exception instance, the same one that [`sys.exception()`](https://docs.python.org/3.14/library/sys.html#sys.exception) would yield. This points at an exception that was *already caught*, not one that has just been raised. Hands back a new reference to the exception, or `NULL`. Leaves the interpreter's exception state untouched.

Note

Code aiming to handle exceptions does not usually call this function. It is instead handy where code has to briefly stash and reinstate the exception state. Reach for `PyErr_SetHandledException()` to reinstate or clear that exception state.

Added in version 3.11.

 void PyErr_SetHandledException([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Establish the active exception, the one reported by `sys.exception()`. This points at an exception that was *already caught*, not one that has just been raised. Hand in `NULL` to clear the exception state.

Note

Code aiming to handle exceptions does not usually call this function. It is instead handy where code has to briefly stash and reinstate the exception state. Reach for `PyErr_GetHandledException()` to read that exception state.

Added in version 3.11.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyerr-occurred-to-pyerr-setraisedexception.md) · [Following source contract](pyerr-getexcinfo-to-pyerr-setexcinfo.md)

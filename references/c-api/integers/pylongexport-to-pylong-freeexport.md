# integers C API: `PyLongExport`, `PyLong_Export()`, `PyLong_FreeExport()`

struct PyLongExport

The export form of a Python [`int`](https://docs.python.org/3.14/library/functions.html#int) object.

There are two cases:

- Where `digits` holds `NULL`, rely on the `value` member alone.

- Where `digits` is something other than `NULL`, draw on the `negative`, `ndigits` and `digits` members.

 int64_t value

The exported [`int`](https://docs.python.org/3.14/library/functions.html#int) object's native integer value. This holds good only where `digits` is `NULL`.

 uint8_t negative

Set to `1` when the number is negative and `0` when it is not. This holds good only where `digits` is something other than `NULL`.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) ndigits

How many digits the `digits` array contains. This holds good only where `digits` is something other than `NULL`.

 const void *digits

An unsigned-digit array that is read-only. It is permitted to be `NULL`.

 int PyLong_Export([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, PyLongExport *export_long)

Carry out the export of a Python [`int`](https://docs.python.org/3.14/library/functions.html#int) object.

*export_long* is required to reference a `PyLongExport` structure that the caller has allocated, and it cannot be `NULL`.

When it succeeds, populate `*export_long` and return `0`. When something goes wrong, set an exception and return `-1`.

Once you no longer need the export, you have to call `PyLong_FreeExport()`.

>

**CPython implementation detail:** As long as *obj* is a Python [`int`](https://docs.python.org/3.14/library/functions.html#int) object or a subclass, this function never fails.

 void PyLong_FreeExport(PyLongExport *export_long)

Free the export *export_long* that `PyLong_Export()` produced.

**CPython implementation detail:** Where *export_long->digits* is `NULL`, the call to `PyLong_FreeExport()` is not required.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pylonglayout-to-pylong-getnativelayout.md) · [Following source contract](pylongwriter-api.md)

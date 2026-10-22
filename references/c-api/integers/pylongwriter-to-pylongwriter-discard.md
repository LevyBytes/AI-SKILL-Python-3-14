# integers C API: `PyLongWriter`, `PyLongWriter_Create()`, `PyLongWriter_Finish()`, `PyLongWriter_Discard()`

struct PyLongWriter

An instance of a Python [`int`](https://docs.python.org/3.14/library/functions.html#int) writer.

Disposal of the instance has to go through `PyLongWriter_Finish()` or `PyLongWriter_Discard()`.

 PyLongWriter *PyLongWriter_Create(int negative, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) ndigits, void **digits)

Create a `PyLongWriter`.

When it succeeds, allocate `*digits` and return a writer. When something goes wrong, set an exception and return `NULL`.

*negative* takes the value `1` when the number is negative, or else `0`.

*ndigits* gives how many digits the *digits* array holds, and it has to exceed 0.

*digits* must not be NULL.

Once this function has been called successfully, the caller is expected to populate the digits array *digits* and afterward call `PyLongWriter_Finish()` to obtain a Python [`int`](https://docs.python.org/3.14/library/functions.html#int). How *digits* is laid out is set out by `PyLong_GetNativeLayout()`.

Each digit has to fall within the range [`0`; `(1 << bits_per_digit) - 1`] (here `bits_per_digit` denotes how many bits each digit carries). Whatever most significant digits go unused have to be set to `0`.

As another option, call `PyLongWriter_Discard()` to tear down the writer instance while producing no [`int`](https://docs.python.org/3.14/library/functions.html#int) object at all.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyLongWriter_Finish(PyLongWriter *writer)

*Return value: New reference.*

Conclude a `PyLongWriter` that `PyLongWriter_Create()` produced.

When it succeeds, hand back a Python [`int`](https://docs.python.org/3.14/library/functions.html#int) object. When something goes wrong, set an exception and hand back `NULL`.

Normalizing the digits is handled by the function, which also turns the object into a compact integer where that is called for.

Both the writer instance and the *digits* array cease to be valid once the call returns.

 void PyLongWriter_Discard(PyLongWriter *writer)

Throw away a `PyLongWriter` that `PyLongWriter_Create()` produced.

Should *writer* be `NULL`, nothing at all is done.

After the call has returned, the writer instance along with the *digits* array are no longer valid.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pylongwriter-api.md) · [Following source contract](pylong-shift-to-pylong-mask.md)

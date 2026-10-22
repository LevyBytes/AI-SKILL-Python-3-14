# unicode C API: `PyUnicode_Count()`, `PyUnicode_Replace()`, `PyUnicode_Compare()`, `PyUnicode_Equal()`, `PyUnicode_EqualToUTF8AndSize()`, `PyUnicode_EqualToUTF8()`, `PyUnicode_CompareWithASCIIString()`

[Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyUnicode_Count([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *substr, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) start, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) end)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back a count of how many times *substr* appears, without overlap, throughout `unicode[start:end]`. Should something go wrong, `-1` comes back instead.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_Replace([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *substr, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *replstr, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) maxcount)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Swap up to *maxcount* appearances of *substr* inside *unicode* for *replstr*, handing back the Unicode object that results. Passing *maxcount* == `-1` tells it to swap every one.

 int PyUnicode_Compare([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *left, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *right)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Weigh one string against another, handing back `-1`, `0`, or `1` to mark the first as smaller, equal, or larger in turn.

Since a failure also produces `-1` from this routine, lean on [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to tell whether an error actually happened.

See also

The `PyUnicode_Equal()` function.

 int PyUnicode_Equal([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *a, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *b)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.14.*

Test if two strings are equal:

- Return `1` if *a* is equal to *b*.

- Return `0` if *a* is not equal to *b*.

- Should either *a* or *b* fail to be a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object, raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception and hand back `-1`.

Provided *a* and *b* are both [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects, the call can never fail.

Subclasses of [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) are handled too, though any custom `__eq__()` method on them goes ignored.

See also

The `PyUnicode_Compare()` function.

Added in version 3.14.

 int PyUnicode_EqualToUTF8AndSize([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, const char *string, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Match a Unicode object against a char buffer that is read as UTF-8- or ASCII-encoded data, yielding true (`1`) on equality and false (`0`) otherwise. Where the Unicode object holds surrogate code points (`U+D800` - `U+DFFF`), or the C string fails to be valid UTF-8, the answer is false (`0`).

No exceptions are raised by this call.

Added in version 3.13.

 int PyUnicode_EqualToUTF8([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, const char *string)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Behaves like `PyUnicode_EqualToUTF8AndSize()`, except the *string* length is worked out via `strlen()`. Where the Unicode object carries null characters, the result is false (`0`).

Added in version 3.13.

 int PyUnicode_CompareWithASCIIString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, const char *string)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Set the Unicode object *unicode* beside *string*, returning `-1`, `0`, or `1` to denote that it ranks below, level with, or above. Ideally you feed in only ASCII-encoded text, yet should non-ASCII characters appear, the routine reads the supplied string as ISO-8859-1.

Exceptions are never raised here.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyunicode-concat-to-pyunicode-tailmatch.md) · [Previous source contract](pyunicode-findchar.md) · [Following source contract](pyunicode-richcompare-to-pyunicode-check-interned.md)

# object protocol C API: Object dictionaries, attribute deletion and representation

int PyObject_DelAttr([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *attr_name)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Remove the attribute named *attr_name* from object *o*. On failure `-1` is returned. The behavior matches the Python statement `del o.attr_name`.

 int PyObject_DelAttrString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, const char *attr_name)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Identical to `PyObject_DelAttr()`, save that *attr_name* is given as a const char* UTF-8 encoded bytes string instead of a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

Keep the count of distinct attribute names handed to this function low, generally by relying on a statically allocated string for *attr_name*. When attribute names aren't available at compile time, it is better to call [`PyUnicode_FromString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromString) followed by `PyObject_DelAttr()` directly. Further information appears under [`PyUnicode_InternFromString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_InternFromString), which the implementation may use internally to build a key object for lookup.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_GenericGetDict([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, void *context)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

A generic implementation backing the getter of a `__dict__` descriptor. It builds the dictionary when one is needed.

You may also call this function to retrieve the [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) of the object *o*. Supply `NULL` for *context* when you do so. Because this function might have to allocate memory for the dictionary, calling `PyObject_GetAttr()` to reach an attribute on the object can be more efficient.

On failure, `NULL` is returned with an exception set.

Added in version 3.3.

 int PyObject_GenericSetDict([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value, void *context)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

A generic implementation backing the setter of a `__dict__` descriptor. This implementation forbids deleting the dictionary.

Added in version 3.3.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **_PyObject_GetDictPtr([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Hand back a pointer to the [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) of the object *obj*. When no `__dict__` exists, `NULL` is returned and no exception is set.

Because this function might have to allocate memory for the dictionary, calling `PyObject_GetAttr()` to reach an attribute on the object can be more efficient.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_RichCompare([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2, int opid)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Compare *o1* against *o2* with the operation named by *opid*, which has to be one of [`Py_LT`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_LT), [`Py_LE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_LE), [`Py_EQ`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_EQ), [`Py_NE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_NE), [`Py_GT`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_GT), or [`Py_GE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_GE), which map to `<`, `<=`, `==`, `!=`, `>`, or `>=` in turn. The behavior matches the Python expression `o1 op o2`, with `op` standing for the operator that goes with *opid*. On success the comparison's value is returned, or `NULL` on failure.

 int PyObject_RichCompareBool([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2, int opid)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Compare *o1* against *o2* with the operation named by *opid*, the way `PyObject_RichCompare()` does, except it returns `-1` on error, `0` when the result is false, and `1` otherwise.

Note

When *o1* and *o2* are the very same object, `PyObject_RichCompareBool()` always returns `1` for [`Py_EQ`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_EQ) and `0` for [`Py_NE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_NE).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_Format([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *format_spec)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Format *obj* according to *format_spec*. This matches the Python expression `format(obj, format_spec)`.

*format_spec* is allowed to be `NULL`, in which case the call matches `format(obj)`. The formatted string comes back on success, and `NULL` on failure.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_Repr([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Produce a string representation of object *o*. The string representation comes back on success, and `NULL` on failure. The behavior matches the Python expression `repr(o)`. Invoked by the [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) built-in function.

When the argument is `NULL`, the string `'<NULL>'` is returned.

Changed in version 3.4: A debug assertion is now built into this function to help confirm that it does not quietly drop a live exception.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_ASCII([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Like `PyObject_Repr()`, this produces a string representation of object *o*, yet within the string that `PyObject_Repr()` returns it escapes the non-ASCII characters using `\x`, `\u` or `\U` escapes. The output resembles what `PyObject_Repr()` produced in Python 2. Invoked by the [`ascii()`](https://docs.python.org/3.14/library/functions.html#ascii) built-in function.

When the argument is `NULL`, the string `'<NULL>'` is returned.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-getconstant-to-pyobject-hasattrstringwitherror.md) · [Previous source contract](pyobject-hasattr-to-pyobject-genericsetattr.md) · [Following source contract](pyobject-str-to-pyobject-isinstance.md)

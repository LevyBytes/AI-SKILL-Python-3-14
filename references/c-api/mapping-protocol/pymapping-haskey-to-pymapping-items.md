# mapping protocol C API: `PyMapping_HasKey()`, `PyMapping_HasKeyString()`, `PyMapping_Keys()`, `PyMapping_Values()`, `PyMapping_Items()`

int PyMapping_HasKey([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Gives `1` when the mapping contains *key* and `0` if it does not, matching the meaning of the Python expression `key in o`. There is no failure path for this call.

Note

Any exception triggered while this routine invokes the [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) method is quietly discarded. When you need to handle errors correctly, reach for `PyMapping_HasKeyWithError()`, `PyMapping_GetOptionalItem()` or [`PyObject_GetItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetItem) instead.

 int PyMapping_HasKeyString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, const char *key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Functions exactly like `PyMapping_HasKey()`, except that here *key* is passed as a const char* UTF-8 encoded byte string in place of a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

Note

Should an exception arise either as this routine calls the [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) method or as it builds the throwaway [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object, it is swallowed without notice. For dependable error handling, turn to `PyMapping_HasKeyStringWithError()`, `PyMapping_GetOptionalItemString()` or `PyMapping_GetItemString()` instead.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyMapping_Keys([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

When it works, you get back a list holding the keys of object *o*; otherwise the result is `NULL`.

Changed in version 3.7: Prior versions might have produced a tuple rather than a list here.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyMapping_Values([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On a successful call this returns a list of object *o*'s values; a failure yields `NULL` instead.

Changed in version 3.7: In earlier releases the call could hand back either a list or a tuple.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyMapping_Items([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

When successful, it produces a list of object *o*'s items, with every entry being a tuple that pairs a key with its value; on failure the return is `NULL`.

Changed in version 3.7: Older builds of this routine returned either a tuple or a list.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pymapping-check-to-pymapping-haskeystringwitherror.md) · [Following source contract](../data-marshalling-support/py-marshal-version-to-pymarshal-readobjectfromstring.md)

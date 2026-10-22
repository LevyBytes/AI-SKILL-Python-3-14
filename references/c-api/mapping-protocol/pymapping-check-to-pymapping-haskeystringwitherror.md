# mapping protocol C API: Mapping access, assignment and key-error handling

# Mapping, Marshal

## Overview

Covers: Mapping Protocol; Data marshalling support.

## Mapping Protocol

### Mapping Protocol

See also [`PyObject_GetItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetItem), [`PyObject_SetItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_SetItem) and [`PyObject_DelItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_DelItem).

 int PyMapping_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields `1` when the given object exposes the mapping protocol or permits slicing; in every other case the result is `0`. Be aware that a Python class defining a [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) method also yields `1`, because there is generally no way to know which key types such a class accepts. The call can never fail.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyMapping_Size([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyMapping_Length([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success this reports how many keys live in object *o*; should it fail, the value `-1` comes back instead. It mirrors what the Python expression `len(o)` would give you.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyMapping_GetItemString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, const char *key)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Behaves identically to [`PyObject_GetItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetItem), except here *key* arrives as a const char* holding a UTF-8 encoded byte string instead of being passed as a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

 int PyMapping_GetOptionalItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **result)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

A variation on [`PyObject_GetItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetItem) that stays quiet — no [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is thrown when the requested key is absent.

When the lookup locates the key, the function hands back `1` and points **result* at a fresh [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to that value. With no matching key, it returns `0`, leaves **result* as `NULL`, and suppresses the [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError). Any failure beyond a plain `KeyError` produces `-1` with **result* again set to `NULL`.

Added in version 3.13.

 int PyMapping_GetOptionalItemString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, const char *key, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **result)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Works just like `PyMapping_GetOptionalItem()`, the difference being that *key* comes in as a const char* UTF-8 encoded byte string rather than as a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

Added in version 3.13.

 int PyMapping_SetItemString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, const char *key, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *v)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Equivalent to [`PyObject_SetItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_SetItem), save that *key* is handed over as a const char* UTF-8 encoded byte string in place of a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

 int PyMapping_DelItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key)

Simply another name for [`PyObject_DelItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_DelItem).

 int PyMapping_DelItemString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, const char *key)

The same operation as [`PyObject_DelItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_DelItem), only with *key* provided as a const char* UTF-8 encoded byte string instead of a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

 int PyMapping_HasKeyWithError([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Hands back `1` whenever the mapping holds *key*, otherwise `0` — mirroring how the Python expression `key in o` behaves. Should something go wrong, `-1` is returned.

Added in version 3.13.

 int PyMapping_HasKeyStringWithError([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, const char *key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Identical in effect to `PyMapping_HasKeyWithError()`, with the one change that *key* is given as a const char* UTF-8 encoded byte string and not a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

Added in version 3.13.

[Subject index](INDEX.md) · [Following source contract](pymapping-haskey-to-pymapping-items.md)

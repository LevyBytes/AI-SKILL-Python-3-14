# object protocol C API: `Py_GetConstant()`, `Py_GetConstantBorrowed()`, `Py_NotImplemented`, `Py_RETURN_NOTIMPLEMENTED`, `Py_PRINT_RAW`, `PyObject_Print()`, `PyObject_HasAttrWithError()`, `PyObject_HasAttrStringWithError()`

### Object Protocol

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *Py_GetConstant(unsigned int constant_id)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Obtain a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to one of the predefined constants.

When *constant_id* is not valid, an exception is set and `NULL` comes back.

The *constant_id* argument has to match one of the following constant identifiers:

| Constant Identifier | Value | Returned object |
| --- | --- | --- |
| Py_CONSTANT_NONE?? | `0` | `None` |
| Py_CONSTANT_FALSE?? | `1` | `False` |
| Py_CONSTANT_TRUE?? | `2` | `True` |
| Py_CONSTANT_ELLIPSIS?? | `3` | `Ellipsis` |
| Py_CONSTANT_NOT_IMPLEMENTED?? | `4` | `NotImplemented` |
| Py_CONSTANT_ZERO?? | `5` | `0` |
| Py_CONSTANT_ONE?? | `6` | `1` |
| Py_CONSTANT_EMPTY_STR?? | `7` | `''` |
| Py_CONSTANT_EMPTY_BYTES?? | `8` | `b''` |
| Py_CONSTANT_EMPTY_TUPLE?? | `9` | `()` |

The numeric values are supplied solely for projects that are unable to reference the constant identifiers.

Added in version 3.13.

**CPython implementation detail:** Within CPython, every one of these constants is [immortal](https://docs.python.org/3.14/glossary.html#term-immortal).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *Py_GetConstantBorrowed(unsigned int constant_id)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Behaves like `Py_GetConstant()`, except that it yields a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference).

The main purpose of this function is backwards compatibility: for new code, `Py_GetConstant()` is the recommended choice.

The interpreter lends the reference, which stays valid right up until interpreter finalization.

Added in version 3.13.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *Py_NotImplemented

The `NotImplemented` singleton, which indicates that an operation has no implementation for the supplied combination of types.

 Py_RETURN_NOTIMPLEMENTED

Correctly manage the return of `Py_NotImplemented` out of a C function (in other words, build a fresh [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) and hand it back).

 Py_PRINT_RAW

A flag intended for several functions that print an object (such as `PyObject_Print()` and [`PyFile_WriteObject()`](https://docs.python.org/3.14/c-api/file.html#c.PyFile_WriteObject)). When supplied, those functions emit the [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) of the object rather than its [`repr()`](https://docs.python.org/3.14/library/functions.html#repr).

 int PyObject_Print([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, FILE *fp, int flags)

Write an object *o* out to file *fp*. On error it returns `-1`. The flags argument switches on particular printing behaviors. At present the lone available option is `Py_PRINT_RAW`; when supplied, the object's [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) is emitted in place of its [`repr()`](https://docs.python.org/3.14/library/functions.html#repr).

 int PyObject_HasAttrWithError([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *attr_name)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Yields `1` when *o* carries the attribute *attr_name*, and `0` when it does not. The behavior matches the Python expression `hasattr(o, attr_name)`. When something goes wrong, `-1` is returned.

Added in version 3.13.

 int PyObject_HasAttrStringWithError([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, const char *attr_name)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Identical to `PyObject_HasAttrWithError()`, save that *attr_name* is given as a const char* UTF-8 encoded bytes string instead of a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

Added in version 3.13.

[Subject index](INDEX.md) · [Following source contract](pyobject-hasattr-to-pyobject-genericsetattr.md)

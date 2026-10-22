# object protocol C API: Required and optional attribute access and assignment

int PyObject_HasAttr([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *attr_name)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields `1` when *o* carries the attribute *attr_name*, and `0` when it does not. This call never fails.

Note

Any exceptions raised while this invokes the [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) and [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__) methods are not propagated; they are routed instead to [`sys.unraisablehook()`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook). To handle errors correctly, reach for `PyObject_HasAttrWithError()`, `PyObject_GetOptionalAttr()` or `PyObject_GetAttr()` in its place.

 int PyObject_HasAttrString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, const char *attr_name)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Identical to `PyObject_HasAttr()`, save that *attr_name* is given as a const char* UTF-8 encoded bytes string instead of a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

Note

Any exceptions raised while this invokes the [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) and [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__) methods, or while building the temporary [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object, are quietly discarded. To handle errors correctly, reach for `PyObject_HasAttrStringWithError()`, `PyObject_GetOptionalAttrString()` or `PyObject_GetAttrString()` in its place.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_GetAttr([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *attr_name)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Fetch an attribute called *attr_name* from object *o*. On success the attribute value comes back, or `NULL` on failure. The behavior matches the Python expression `o.attr_name`.

When a missing attribute ought not to count as a failure, `PyObject_GetOptionalAttr()` is the alternative to use.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_GetAttrString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, const char *attr_name)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Identical to `PyObject_GetAttr()`, save that *attr_name* is given as a const char* UTF-8 encoded bytes string instead of a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

When a missing attribute ought not to count as a failure, `PyObject_GetOptionalAttrString()` is the alternative to use.

 int PyObject_GetOptionalAttr([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *attr_name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **result);

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

A flavor of `PyObject_GetAttr()` that withholds the [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) when the attribute can't be located.

Should the attribute be located, `1` is returned and **result* is set to a fresh [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) pointing at it. Should the attribute be missing, `0` is returned, **result* is set to `NULL`, and the [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) is suppressed. Should an error besides `AttributeError` occur, `-1` is returned and **result* is set to `NULL`.

Added in version 3.13.

 int PyObject_GetOptionalAttrString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, const char *attr_name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **result);

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Identical to `PyObject_GetOptionalAttr()`, save that *attr_name* is given as a const char* UTF-8 encoded bytes string instead of a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

Added in version 3.13.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_GenericGetAttr([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A general-purpose attribute getter designed to be assigned to a type object's `tp_getattro` slot. It searches for a descriptor among the dictionaries of the classes in the object's MRO and also for an attribute in the object's own [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) (when one exists). As covered in [Implementing Descriptors](https://docs.python.org/3.14/reference/datamodel.html#descriptors), data descriptors win out over instance attributes, whereas non-data descriptors do not. Failing all of that, an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) is raised.

 int PyObject_SetAttr([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *attr_name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *v)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Assign the value *v* to the attribute named *attr_name* on object *o*. On failure, raise an exception and return `-1`; on success, return `0`. The behavior matches the Python statement `o.attr_name = v`.

When *v* is `NULL`, the attribute gets deleted. That behaviour is deprecated in favour of `PyObject_DelAttr()`, although there are no current plans to drop it.

 int PyObject_SetAttrString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, const char *attr_name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *v)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Identical to `PyObject_SetAttr()`, save that *attr_name* is given as a const char* UTF-8 encoded bytes string instead of a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

When *v* is `NULL`, the attribute gets deleted, though this capability is deprecated in favour of `PyObject_DelAttrString()`.

Keep the count of distinct attribute names handed to this function low, generally by relying on a statically allocated string for *attr_name*. When attribute names aren't available at compile time, it is better to call [`PyUnicode_FromString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromString) followed by `PyObject_SetAttr()` directly. Further information appears under [`PyUnicode_InternFromString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_InternFromString), which the implementation may use internally to build a key object.

 int PyObject_GenericSetAttr([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A general-purpose attribute setter and deleter designed to be assigned to a type object's [`tp_setattro`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_setattro) slot. It searches for a data descriptor among the dictionaries of the classes in the object's MRO, and where one is found it takes priority over modifying or removing the attribute within the per-instance dictionary. Failing that, the attribute is set or deleted within the object's own [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) (when one exists). On success `0` comes back, and otherwise an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) is raised with `-1` returned.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-getconstant-to-pyobject-hasattrstringwitherror.md) · [Following source contract](pyobject-delattr-to-pyobject-ascii.md)

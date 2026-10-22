# object protocol C API: `PyObject_Str()`, `PyObject_Bytes()`, `PyObject_IsSubclass()`, `PyObject_IsInstance()`

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_Str([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Produce a string representation of object *o*. The string representation comes back on success, and `NULL` on failure. The behavior matches the Python expression `str(o)`. Invoked by the [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) built-in function and, as a result, by the [`print()`](https://docs.python.org/3.14/library/functions.html#print) function.

When the argument is `NULL`, the string `'<NULL>'` is returned.

Changed in version 3.4: A debug assertion is now built into this function to help confirm that it does not quietly drop a live exception.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_Bytes([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Produce a bytes representation of object *o*. On failure `NULL` is returned, and on success a bytes object. This matches the Python expression `bytes(o)`, provided *o* is not an integer. Differing from `bytes(o)`, a TypeError is raised when *o* is an integer rather than yielding a zero-initialized bytes object.

When the argument is `NULL`, the [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object `b'<NULL>'` is returned.

 int PyObject_IsSubclass([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *derived, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *cls)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Return `1` when the class *derived* is the same as, or descends from, the class *cls*; otherwise return `0`. Should an error arise, return `-1`.

When *cls* is a tuple, the check runs against each member of *cls*. The result is `1` if at least one of those checks returns `1`, and `0` otherwise.

When *cls* provides a [`__subclasscheck__()`](https://docs.python.org/3.14/reference/datamodel.html#type.__subclasscheck__) method, it is invoked to settle the subclass relationship as laid out in [**PEP 3119**](https://peps.python.org/pep-3119/). Failing that, *derived* counts as a subclass of *cls* if it is a direct or indirect subclass, that is, present in [`cls.__mro__`](https://docs.python.org/3.14/reference/datamodel.html#type.__mro__).

Ordinarily, only class objects, namely instances of [`type`](https://docs.python.org/3.14/library/functions.html#type) or a derived class, are treated as classes. Objects can nonetheless override this by carrying a [`__bases__`](https://docs.python.org/3.14/reference/datamodel.html#type.__bases__) attribute (which has to be a tuple of base classes).

 int PyObject_IsInstance([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *inst, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *cls)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Return `1` when *inst* is an instance of the class *cls* or of a subclass of *cls*, and `0` when it is not. On error, returns `-1` and sets an exception.

When *cls* is a tuple, the check runs against each member of *cls*. The result is `1` if at least one of those checks returns `1`, and `0` otherwise.

When *cls* provides a [`__instancecheck__()`](https://docs.python.org/3.14/reference/datamodel.html#type.__instancecheck__) method, it is invoked to settle the subclass relationship as laid out in [**PEP 3119**](https://peps.python.org/pep-3119/). Failing that, *inst* counts as an instance of *cls* whenever the class of *inst* is a subclass of *cls*.

An instance *inst* may override what counts as its class by carrying a [`__class__`](https://docs.python.org/3.14/reference/datamodel.html#object.__class__) attribute.

An object *cls* may override whether it counts as a class, and which base classes it has, by carrying a [`__bases__`](https://docs.python.org/3.14/reference/datamodel.html#type.__bases__) attribute (which has to be a tuple of base classes).

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-getconstant-to-pyobject-hasattrstringwitherror.md) · [Previous source contract](pyobject-delattr-to-pyobject-ascii.md) · [Following source contract](pyobject-hash.md)

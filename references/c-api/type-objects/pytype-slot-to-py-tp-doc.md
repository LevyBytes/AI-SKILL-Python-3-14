# type objects C API: Heap-type slot identifiers, offsets and restrictions

type PyType_Slot

* Included in the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable), all of its members too.*

A structure that captures optional capabilities of a type, holding both a slot ID and a value pointer.

 int slot

A slot ID.

A slot ID borrows the field name from one of the structures `PyTypeObject`, [`PyNumberMethods`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyNumberMethods), [`PySequenceMethods`](https://docs.python.org/3.14/c-api/typeobj.html#c.PySequenceMethods), [`PyMappingMethods`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyMappingMethods) and [`PyAsyncMethods`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyAsyncMethods), prefixed with `Py_`. To illustrate, use:

- [`Py_tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_tp_dealloc) for populating [`PyTypeObject.tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc)

- [`Py_nb_add`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_nb_add) for populating [`PyNumberMethods.nb_add`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyNumberMethods.nb_add)

- [`Py_sq_length`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_sq_length) for populating [`PySequenceMethods.sq_length`](https://docs.python.org/3.14/c-api/typeobj.html#c.PySequenceMethods.sq_length)

One extra slot is also allowed, one that maps to no `PyTypeObject` struct field:

- `Py_tp_token`

By way of `PyType_Slot`, these “offset” fields cannot be assigned:

- [`tp_weaklistoffset`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_weaklistoffset) (where feasible, reach for [`Py_TPFLAGS_MANAGED_WEAKREF`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_WEAKREF) in its place)

- [`tp_dictoffset`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dictoffset) (where feasible, reach for [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT) in its place)

- [`tp_vectorcall_offset`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_vectorcall_offset) (supply `"__vectorcalloffset__"` within [PyMemberDef](https://docs.python.org/3.14/c-api/structures.html#pymemberdef-offsets))

Should moving to a `MANAGED` flag be impossible (say, for vectorcall or to keep Python versions before 3.12 working), state the offset within [`Py_tp_members`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_tp_members). The [PyMemberDef documentation](https://docs.python.org/3.14/c-api/structures.html#pymemberdef-offsets) spells out the specifics.

When you build a heap type, none of these internal fields can be assigned whatsoever:

- [`tp_dict`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dict), [`tp_mro`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_mro), [`tp_cache`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_cache), [`tp_subclasses`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_subclasses), and [`tp_weaklist`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_weaklist).

Assigning [`Py_tp_bases`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_tp_bases) or [`Py_tp_base`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_tp_base) can cause trouble on certain platforms. Steer clear of that by going through the *bases* argument of `PyType_FromSpecWithBases()` instead.

Changed in version 3.9: Within the unlimited API, slots from [`PyBufferProcs`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyBufferProcs) are now assignable.

Changed in version 3.11: Both [`bf_getbuffer`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyBufferProcs.bf_getbuffer) and [`bf_releasebuffer`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyBufferProcs.bf_releasebuffer) can now be reached through the [limited API](https://docs.python.org/3.14/c-api/stable.html#limited-c-api).

Changed in version 3.14: You may now assign the [`tp_vectorcall`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_vectorcall) field by way of [`Py_tp_vectorcall`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_tp_vectorcall). The field’s own documentation explains further.

 void *pfunc

Whatever value you want the slot to carry. Usually that amounts to a function pointer.

A *pfunc* value cannot be `NULL`, with these slots as the exceptions:

- [`Py_tp_doc`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_tp_doc)

- `Py_tp_token` (to read more clearly, favor `Py_TP_USE_SPEC` over `NULL`)

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytype-frommetaclass-to-pytype-fromspec.md) · [Previous source contract](name-to-itemsize.md) · [Following source contract](py-tp-token-to-py-tp-use-spec.md)

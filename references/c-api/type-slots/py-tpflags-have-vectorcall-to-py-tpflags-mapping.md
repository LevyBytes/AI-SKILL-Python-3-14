# type slots C API: `Py_TPFLAGS_HAVE_VECTORCALL`, `Py_TPFLAGS_IMMUTABLETYPE`, `Py_TPFLAGS_DISALLOW_INSTANTIATION`, `Py_TPFLAGS_MAPPING`

Py_TPFLAGS_HAVE_VECTORCALL

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

This bit gets enabled when the class supports the [vectorcall protocol](https://docs.python.org/3.14/c-api/call.html#vectorcall). Consult `tp_vectorcall_offset` for the specifics.

**Inheritance:**

A subtype picks up this bit whenever `tp_call` is itself inherited.

Added in version 3.8: as `_Py_TPFLAGS_HAVE_VECTORCALL`

Changed in version 3.9.

Given its present name, with the leading underscore dropped. Its former provisional name is now [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated).

Changed in version 3.12: The interpreter now strips this flag from a class once that class’s [`__call__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__call__) method gets reassigned.

Mutable classes are now permitted to inherit this flag.

 Py_TPFLAGS_IMMUTABLETYPE

This bit applies to type objects that cannot change: you can neither assign nor remove type attributes.

[`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) sets this flag on static types for you.

**Inheritance:**

Subtypes do not pick up this flag.

Added in version 3.10.

 Py_TPFLAGS_DISALLOW_INSTANTIATION

Prevent the type from producing instances: assign NULL to `tp_new` and leave the `__new__` key out of the type dictionary.

You must enable this flag before the type is created rather than afterward. As an illustration, it has to be in place prior to [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) being invoked on the type.

For static types, the flag is enabled for you when `tp_base` is either NULL or `&PyBaseObject_Type` while `tp_new` is NULL.

**Inheritance:**

Subtypes do not pick up this flag. That said, a subclass remains non-instantiable until it supplies a non-NULL `tp_new` (achievable only through the C API).

Note

If you want to block direct instantiation of a class while still permitting its subclasses to be instantiated (say, for an [abstract base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class)), avoid this flag. Rather, arrange for `tp_new` to succeed only when called on subclasses.

Added in version 3.10.

 Py_TPFLAGS_MAPPING

This bit signals that instances of the class are eligible to match mapping patterns when serving as the subject of a [`match`](https://docs.python.org/3.14/reference/compound_stmts.html#match) block. The interpreter sets it automatically upon registering or subclassing [`collections.abc.Mapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Mapping), and clears it upon registering [`collections.abc.Sequence`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Sequence).

Note

`Py_TPFLAGS_MAPPING` and `Py_TPFLAGS_SEQUENCE` cannot coexist; turning both flags on at once is an error.

**Inheritance:**

Any type that has not already enabled `Py_TPFLAGS_SEQUENCE` inherits this flag.

See also

[**PEP 634**](https://peps.python.org/pep-0634/) – Structural Pattern Matching: Specification

Added in version 3.10.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Previous source contract](py-tpflags-have-finalize.md) · [Following source contract](py-tpflags-sequence-to-pytypeobject-tp-doc.md)

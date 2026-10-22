# type slots C API: `Py_TPFLAGS_SEQUENCE`, `Py_TPFLAGS_VALID_VERSION_TAG`, `Py_TPFLAGS_HAVE_VERSION_TAG`, `Py_TPFLAGS_INLINE_VALUES`, `Py_TPFLAGS_IS_ABSTRACT`, `Py_TPFLAGS_HAVE_STACKLESS_EXTENSION`, `PyTypeObject.tp_doc`

Py_TPFLAGS_SEQUENCE

This bit signals that instances of the class are eligible to match sequence patterns when serving as the subject of a [`match`](https://docs.python.org/3.14/reference/compound_stmts.html#match) block. The interpreter sets it automatically upon registering or subclassing [`collections.abc.Sequence`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Sequence), and clears it upon registering [`collections.abc.Mapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Mapping).

Note

`Py_TPFLAGS_MAPPING` and `Py_TPFLAGS_SEQUENCE` cannot coexist; turning both flags on at once is an error.

**Inheritance:**

Any type that has not already enabled `Py_TPFLAGS_MAPPING` inherits this flag.

See also

[**PEP 634**](https://peps.python.org/pep-0634/) – Structural Pattern Matching: Specification

Added in version 3.10.

 Py_TPFLAGS_VALID_VERSION_TAG

Internal. Refrain from setting or clearing this flag. When a class has been modified, call [`PyType_Modified()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Modified) instead

Warning

Although this flag appears in header files, it is not in use. A future release of CPython will drop it

 Py_TPFLAGS_HAVE_VERSION_TAG

This [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) macro is a no-op. In the past, it served to signal that the `tp_version_tag` field existed and had been initialized.

 Py_TPFLAGS_INLINE_VALUES

This bit signals that instances of this type carry an “inline values” array (holding the object’s attributes) located immediately past the end of the object.

For this, `Py_TPFLAGS_HAVE_GC` must be enabled.

**Inheritance:**

Subtypes do not pick up this flag.

Added in version 3.13.

 Py_TPFLAGS_IS_ABSTRACT

This bit signals that the type is abstract and consequently cannot be instantiated.

**Inheritance:**

Subtypes do not pick up this flag.

See also

[`abc`](https://docs.python.org/3.14/library/abc.html#module-abc)

 Py_TPFLAGS_HAVE_STACKLESS_EXTENSION

Internal. Refrain from setting or clearing this flag. In the past, this was a flag held in reserve for Stackless Python.

Warning

Although this flag appears in header files, it is not in use. A future release of CPython may drop it.

 const char *[PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_doc

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_doc` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

An optional pointer to a NUL-terminated C string holding the docstring for this type object. It surfaces as the [`__doc__`](https://docs.python.org/3.14/reference/datamodel.html#type.__doc__) attribute on both the type and its instances.

**Inheritance:**

Subtypes do *not* inherit this field.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Previous source contract](py-tpflags-have-vectorcall-to-py-tpflags-mapping.md) · [Following source contract](pytypeobject-tp-traverse.md)

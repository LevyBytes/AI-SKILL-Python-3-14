# Py_TPFLAGS_LONG_SUBCLASS / Py_TPFLAGS_LIST_SUBCLASS / Py_TPFLAGS_TUPLE_SUBCLASS / Py_TPFLAGS_BYTES_SUBCLASS / Py_TPFLAGS_UNICODE_SUBCLASS / Py_TPFLAGS_DICT_SUBCLASS / Py_TPFLAGS_BASE_EXC_SUBCLASS / Py_TPFLAGS_TYPE_SUBCLASS

Py_TPFLAGS_LONG_SUBCLASS

 Py_TPFLAGS_LIST_SUBCLASS

 Py_TPFLAGS_TUPLE_SUBCLASS

 Py_TPFLAGS_BYTES_SUBCLASS

 Py_TPFLAGS_UNICODE_SUBCLASS

 Py_TPFLAGS_DICT_SUBCLASS

 Py_TPFLAGS_BASE_EXC_SUBCLASS

 Py_TPFLAGS_TYPE_SUBCLASS
Routines like [`PyLong_Check()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_Check) invoke [`PyType_FastSubclass()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FastSubclass) with one of these flags as a fast way to decide whether a type descends from a built-in type; these targeted tests run faster than a broad check such as [`PyObject_IsInstance()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_IsInstance). When you define custom types deriving from built-ins, make sure their `tp_flags` are configured correctly; otherwise the code handling those types will act inconsistently depending on which kind of check gets used.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Previous source contract](py-tpflags-method-descriptor-to-py-tpflags-items-at-end.md) · [Previous source contract](py-tpflags-have-finalize.md)

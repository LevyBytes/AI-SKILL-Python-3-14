# ctypes: `ctypes.py_object`

*class *ctypes.py_object

Stands for the C [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)* datatype. Invoking this with no argument produces a `NULL` PyObject* pointer.

Changed in version 3.14: `py_object` is now a [generic type](https://docs.python.org/3.14/glossary.html#term-generic-type).

The `ctypes.wintypes` module supplies a fair number of further Windows-specific data types, such as `HWND`, `WPARAM`, `VARIANT_BOOL` or `DWORD`. A handful of handy structures like `MSG` or `RECT` are defined there as well.

[Subject index](INDEX.md) · [Previous](ctypes-hresult-class.md) · [Continue](ctypes-union-class.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: Fundamental data types](ctypes-simplecdata-class.md)

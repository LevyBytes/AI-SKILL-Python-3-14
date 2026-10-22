# array: `array.typecodes`

# Array

### `array` — Efficient arrays of numeric values

---

An object type supplied by this module gives you a compact way to hold an array of elementary values — characters, integers, and floating-point numbers. Such arrays are mutable [sequence](https://docs.python.org/3.14/glossary.html#term-sequence) types that act a great deal like lists, the difference being that they restrict what type of object may live inside them. You fix that type when you build the object by passing a *type code*, a single character. These are the type codes that exist:

| Type code | C Type | Python Type | Minimum size in bytes | Notes |
| --- | --- | --- | --- | --- |
| `'b'` | signed char | int | 1 |  |
| `'B'` | unsigned char | int | 1 |  |
| `'u'` | wchar_t | Unicode character | 2 | (1) |
| `'w'` | Py_UCS4 | Unicode character | 4 | (2) |
| `'h'` | signed short | int | 2 |  |
| `'H'` | unsigned short | int | 2 |  |
| `'i'` | signed int | int | 2 |  |
| `'I'` | unsigned int | int | 2 |  |
| `'l'` | signed long | int | 4 |  |
| `'L'` | unsigned long | int | 4 |  |
| `'q'` | signed long long | int | 8 |  |
| `'Q'` | unsigned long long | int | 8 |  |
| `'f'` | float | float | 4 |  |
| `'d'` | double | float | 8 |  |

Notes:

1.

Whether it spans 16 bits or 32 bits hinges on the platform.

Changed in version 3.9: For its C type, `array('u')` now relies on `wchar_t` in place of the deprecated `Py_UNICODE`. Behaviour stays the same here, since `Py_UNICODE` has been an alias for `wchar_t` ever since Python 3.3.

Deprecated since version 3.3, will be removed in version 3.16: Switch over to the `'w'` typecode instead.

2.

Added in version 3.13.

See also

Comparable type codes — though not identical ones — turn up in the [ctypes](https://docs.python.org/3.14/library/ctypes.html#ctypes-fundamental-data-types) and [struct](https://docs.python.org/3.14/library/struct.html#format-characters) modules, and in outside packages such as [numpy](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_interface__).

How values are actually laid out comes down to the machine architecture — more precisely, the C implementation. You can read the real size off the `array.itemsize` attribute.

This module provides the item below:

 array.typecodes

A string holding every type code on offer.

This module provides the type below:

[Subject index](INDEX.md) · [Continue](array-array-class-to-array-array-remove.md)

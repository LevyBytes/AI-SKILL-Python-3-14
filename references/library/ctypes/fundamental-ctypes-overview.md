# ctypes — Fundamental data types — Section introduction and initial examples

### Fundamental data types

`ctypes` defines a number of primitive C compatible data types:

| ctypes type | C type | Python type | `_type_` |
| --- | --- | --- | --- |
| `c_bool` | _Bool | `bool` | `'?'` |
| `c_char` | char | 1-character `bytes` | `'c'` |
| `c_wchar` | `wchar_t` | 1-character `str` | `'u'` |
| `c_byte` | char | `int` | `'b'` |
| `c_ubyte` | unsigned char | `int` | `'B'` |
| `c_short` | short | `int` | `'h'` |
| `c_ushort` | unsigned short | `int` | `'H'` |
| `c_int` | int | `int` | `'i'` * |
| `c_int8` | `int8_t` | `int` | * |
| `c_int16` | `int16_t` | `int` | * |
| `c_int32` | `int32_t` | `int` | * |
| `c_int64` | `int64_t` | `int` | * |
| `c_uint` | unsigned int | `int` | `'I'` * |
| `c_uint8` | `uint8_t` | `int` | * |
| `c_uint16` | `uint16_t` | `int` | * |
| `c_uint32` | `uint32_t` | `int` | * |
| `c_uint64` | `uint64_t` | `int` | * |
| `c_long` | long | `int` | `'l'` |
| `c_ulong` | unsigned long | `int` | `'L'` |
| `c_longlong` | long long | `int` | `'q'` * |
| `c_ulonglong` | unsigned long long | `int` | `'Q'` * |
| `c_size_t` | `size_t` | `int` | * |
| `c_ssize_t` | `Py_ssize_t` | `int` | * |
| `c_time_t` | `time_t` | `int` | * |
| `c_float` | float | `float` | `'f'` |
| `c_double` | double | `float` | `'d'` |
| `c_longdouble` | long double | `float` | `'g'` * |
| `c_char_p` | char* (NUL terminated) | `bytes` or `None` | `'z'` |
| `c_wchar_p` | wchar_t* (NUL terminated) | `str` or `None` | `'Z'` |
| `c_void_p` | void* | `int` or `None` | `'P'` |
| `py_object` | PyObject* | `object` | `'O'` |
| VARIANT_BOOL | short int | `bool` | `'v'` |

On top of these, when IEC 60559 compatible complex arithmetic (Annex G) is supported by both C and `libffi`, the complex types listed below become available:

| ctypes type | C type | Python type | `_type_` |
| --- | --- | --- | --- |
| `c_float_complex` | float complex | `complex` | `'F'` |
| `c_double_complex` | double complex | `complex` | `'D'` |
| `c_longdouble_complex` | long double complex | `complex` | `'G'` |

Every one of these types is constructed by calling it, optionally supplying an initializer whose type and value are correct:

```python
>>> c_int()
c_long(0)
>>> c_wchar_p("Hello, World")
c_wchar_p(140018365411392)
>>> c_ushort(-3)
c_ushort(65533)
>>>

```

For the numeric types, the constructors coerce their input using [`__bool__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__bool__), [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) (for `int`), [`__float__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__float__) or [`__complex__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__complex__). As a result, `c_bool` will accept any object that carries a truth value:

```python
>>> empty_list = []
>>> c_bool(empty_list)
c_bool(False)

```

Because these types are mutable, you can also alter their value at a later point:

```python
>>> i = c_int(42)
>>> print(i)
c_long(42)
>>> print(i.value)
42
>>> i.value = -99
>>> print(i.value)
-99
>>>

```

[Subject index](INDEX.md) · [Previous](calling-functions.md) · [Continue](ctypes-and-given-that-python-string-objects-cannot-be-mutated.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)

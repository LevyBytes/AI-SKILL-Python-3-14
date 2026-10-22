# ctypes: `ctypes.addressof()`, `ctypes.alignment()`, `ctypes.byref()`, `ctypes.CopyComPointer()`, `ctypes.cast()`, `ctypes.create_string_buffer()`

### Utility functions

 ctypes.addressof(*obj*)

Hands back the memory buffer's address as an integer. *obj* has to be an instance of a ctypes type.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `ctypes.addressof` with argument `obj`.

 ctypes.alignment(*obj_or_type*)

Hands back a ctypes type's alignment requirements. *obj_or_type* has to be a ctypes type or instance.

 ctypes.byref(*obj*[, *offset*])

Hands back a light-weight pointer aimed at *obj*, where *obj* has to be a ctypes type instance. *offset*, defaulting to zero, must be an integer added onto the internal pointer value.

`byref(obj, offset)` corresponds to this C code:

```python
(((char *)&obj) + offset)

```

The object returned is usable solely as a foreign function call parameter. It works much like `pointer(obj)`, except that constructing it is far quicker.

 ctypes.CopyComPointer(*src*, *dst*)

Duplicates a COM pointer from *src* into *dst* and hands back the Windows specific `HRESULT` value.

Provided *src* is not `NULL`, its `AddRef` method is invoked, which bumps the reference count.

By contrast, the reference count of *dst* is not lowered before the new value is assigned. Except when *dst* is `NULL`, it falls to the caller to lower the reference count by invoking its `Release` method whenever that is needed.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

Added in version 3.14.

 ctypes.cast(*obj*, *type*)

This function works like the cast operator in C. It returns a fresh instance of *type* pointing at the same memory block as *obj*. *type* has to be a pointer type, and *obj* has to be an object that can be read as a pointer.

 ctypes.create_string_buffer(*init*, *size=None*)

 ctypes.create_string_buffer(*size*)

This function builds a mutable character buffer. What it returns is a ctypes array of `c_char`.

When *size* is supplied (and not `None`), it must be an [`int`](https://docs.python.org/3.14/library/functions.html#int). It fixes the length of the array that is returned.

When the *init* argument is supplied, it must be [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes). It serves to initialize the array items. Any bytes left uninitialized this way are set to zero (NUL).

When *size* is omitted (or is `None`), the buffer is made one element bigger than *init*, which in effect appends a NUL terminator.

When both arguments are supplied, *size* must be at least `len(init)`.

Warning

Should *size* match `len(init)` exactly, no NUL terminator gets appended, so refrain from using such a buffer as a C string.

For example:

```python
>>> bytes(create_string_buffer(2))
b'\x00\x00'
>>> bytes(create_string_buffer(b'ab'))
b'ab\x00'
>>> bytes(create_string_buffer(b'ab', 2))
b'ab'
>>> bytes(create_string_buffer(b'ab', 4))
b'ab\x00\x00'
>>> bytes(create_string_buffer(b'abcdef', 2))
Traceback (most recent call last):
   ...
ValueError: byte string too long

```

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `ctypes.create_string_buffer` with arguments `init`, `size`.

[Subject index](INDEX.md) · [Previous](windows-function-prototype-example.md) · [Continue](ctypes-create-unicode-buffer-to-ctypes-memset.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)

# ctypes - Fundamental data types - Contract: When you assign a fresh value to instances of the pointer types `c_char_p`, `c_wchar_p`, and `c_void_p`, you alter the *memory location* they reference, *not the contents* of the memory block (and naturally so, given that Python string objects cannot be mutated):

When you assign a fresh value to instances of the pointer types `c_char_p`, `c_wchar_p`, and `c_void_p`, you alter the *memory location* they reference, *not the contents* of the memory block (and naturally so, given that Python string objects cannot be mutated):

```python
>>> s = "Hello, World"
>>> c_s = c_wchar_p(s)
>>> print(c_s)
c_wchar_p(139966785747344)
>>> print(c_s.value)
Hello World
>>> c_s.value = "Hi, there"
>>> print(c_s)              # the memory location has changed
c_wchar_p(139966783348904)
>>> print(c_s.value)
Hi, there
>>> print(s)                # first object is unchanged
Hello, World
>>>

```

Take care, though, never to hand these to functions that expect pointers into mutable memory. When you do need mutable memory blocks, ctypes provides a `create_string_buffer()` function that produces them in a number of ways. You can read (or overwrite) the present contents of the memory block through the `raw` property; to treat it as a NUL terminated string instead, reach for the `value` property:

```python
>>> from ctypes import *
>>> p = create_string_buffer(3)            # create a 3 byte buffer, initialized to NUL bytes
>>> print(sizeof(p), repr(p.raw))
3 b'\x00\x00\x00'
>>> p = create_string_buffer(b"Hello")     # create a buffer containing a NUL terminated string
>>> print(sizeof(p), repr(p.raw))
6 b'Hello\x00'
>>> print(repr(p.value))
b'Hello'
>>> p = create_string_buffer(b"Hello", 10) # create a 10 byte buffer
>>> print(sizeof(p), repr(p.raw))
10 b'Hello\x00\x00\x00\x00\x00'
>>> p.value = b"Hi"
>>> print(sizeof(p), repr(p.raw))
10 b'Hi\x00lo\x00\x00\x00\x00\x00'
>>>

```

The `create_string_buffer()` function stands in for the former `c_buffer()` function (which remains accessible as an alias). When you want a mutable memory block holding unicode characters of the C type `wchar_t`, turn to the `create_unicode_buffer()` function.

[Subject index](INDEX.md) · [Previous](fundamental-ctypes-overview.md) · [Continue](calling-functions-continued.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: Fundamental data types](fundamental-ctypes-overview.md)

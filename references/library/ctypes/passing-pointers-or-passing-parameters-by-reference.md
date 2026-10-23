# ctypes - Passing pointers (or: passing parameters by reference)

### Passing pointers (or: passing parameters by reference)

Now and then a C api function wants a *pointer* to a data type as a parameter, perhaps so it can write into that location, or because the data is too bulky to pass by value. This goes by the name *passing parameters by reference* as well.

`ctypes` exposes the `byref()` function, used for passing parameters by reference. The very same outcome is reachable with the `pointer()` function, but `pointer()` performs considerably more work since it builds an actual pointer object — so `byref()` is the faster choice when you have no need for the pointer object within Python itself:

```python
>>> i = c_int()
>>> f = c_float()
>>> s = create_string_buffer(b'\000' * 32)
>>> print(i.value, f.value, repr(s.value))
0 0.0 b''
>>> libc.sscanf(b"1 3.14 Hello", b"%d %f %s",
...             byref(i), byref(f), s)
3
>>> print(i.value, f.value, repr(s.value))
1 3.1400001049 b'Hello'
>>>

```

[Subject index](INDEX.md) · [Previous](return-types.md) · [Continue](structures-and-unions.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)

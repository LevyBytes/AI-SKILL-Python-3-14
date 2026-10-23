# ctypes - Calling functions

### Calling functions

These functions may be called exactly as you would call any other Python callable. The example below relies on the `rand()` function, which accepts no arguments and hands back a pseudo-random integer:

```python
>>> print(libc.rand())
1804289383

```

On Windows, you can invoke the `GetModuleHandleA()` function, which yields a win32 module handle (supply `None` as the lone argument to call it with a `NULL` pointer):

```python
>>> print(hex(windll.kernel32.GetModuleHandleA(None)))
0x1d000000
>>>

```

A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised should you invoke an `stdcall` function using the `cdecl` calling convention, or the reverse:

```python
>>> cdll.kernel32.GetModuleHandleA(None)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Procedure probably called with not enough arguments (4 bytes missing)
>>>

>>> windll.msvcrt.printf(b"spam")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Procedure probably called with too many arguments (4 bytes in excess)
>>>

```

Determining the proper calling convention means examining the C header file or the documentation belonging to the function you intend to call.

On Windows, `ctypes` leans on win32 structured exception handling to guard against crashes from general protection faults when functions receive invalid argument values:

```python
>>> windll.kernel32.GetModuleHandleA(32)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: exception: access violation reading 0x00000020
>>>

```

When erroneous C library calls produce segmentation faults or similar crashes, the [`faulthandler`](https://docs.python.org/3.14/library/faulthandler.html#module-faulthandler) module is a useful aid for debugging them.

The only native Python objects you can hand directly to these function calls as parameters are `None`, integers, bytes objects, and (unicode) strings. `None` becomes a C `NULL` pointer; bytes objects and strings are handed over as a pointer to the memory block holding their data (char* or wchar_t*). Python integers go through as the platform's default C int type, with their value masked down to fit that C type.

Before turning to functions that take other parameter types, we first need a deeper grasp of the `ctypes` data types.

[Subject index](INDEX.md) · [Previous](accessing-functions-from-loaded-dlls.md) · [Continue](fundamental-ctypes-overview.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)

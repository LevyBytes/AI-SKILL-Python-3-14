# ctypes - Return types

### Return types

Functions are presumed by default to return the C int type. You can declare other return types by assigning the `restype` attribute of the function object.

The C prototype of `time()` is `time_t time(time_t *)`. Since `time_t` may differ from the default int return type, you ought to assign the `restype` attribute:

```python
>>> libc.time.restype = c_time_t

```

You can declare the argument types via `argtypes`:

```python
>>> libc.time.argtypes = (POINTER(c_time_t),)

```

To invoke the function passing a `NULL` pointer as the first argument, supply `None`:

```python
>>> print(libc.time(None))
1150640792

```

The next example is more elaborate; it employs the `strchr()` function, which takes a string pointer along with a char and returns a pointer to a string:

```python
>>> strchr = libc.strchr
>>> strchr(b"abcdef", ord("d"))
8059983
>>> strchr.restype = c_char_p    # c_char_p is a pointer to a string
>>> strchr(b"abcdef", ord("d"))
b'def'
>>> print(strchr(b"abcdef", ord("x")))
None
>>>

```

To sidestep the [`ord("x")`](https://docs.python.org/3.14/library/functions.html#ord) calls shown above, you can assign the `argtypes` attribute, and then the second argument will be coerced from a single-character Python bytes object into a C char:

```pycon
>>> strchr.restype = c_char_p
>>> strchr.argtypes = [c_char_p, c_char]
>>> strchr(b"abcdef", b"d")
b'def'
>>> strchr(b"abcdef", b"def")
Traceback (most recent call last):
ctypes.ArgumentError: argument 2: TypeError: one character bytes, bytearray or integer expected
>>> print(strchr(b"abcdef", b"x"))
None
>>> strchr(b"abcdef", b"d")
b'def'
>>>

```

You may likewise use a callable Python object (a function or a class, say) as the `restype` attribute, provided the foreign function returns an integer. That callable receives the *integer* the C function returns, and whatever it produces becomes the result of your own function call. This proves handy for spotting error return values and raising an exception automatically:

```python
>>> GetModuleHandle = windll.kernel32.GetModuleHandleA
>>> def ValidHandle(value):
...     if value == 0:
...         raise WinError()
...     return value
...
>>>
>>> GetModuleHandle.restype = ValidHandle
>>> GetModuleHandle(None)
486539264
>>> GetModuleHandle("something silly")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in ValidHandle
OSError: [Errno 126] The specified module could not be found.
>>>

```

`WinError` is a function that calls the Windows `FormatMessage()` api to obtain the textual representation of an error code, and *returns* an exception. `WinError` accepts an optional error code parameter; when none is supplied, it falls back to `GetLastError()` to retrieve it.

Do note that a considerably more capable error-checking facility is offered through the `errcheck` attribute; consult the reference manual for the particulars.

[Subject index](INDEX.md) · [Previous](specifying-the-required-argument-types-function-prototypes.md) · [Continue](passing-pointers-or-passing-parameters-by-reference.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)

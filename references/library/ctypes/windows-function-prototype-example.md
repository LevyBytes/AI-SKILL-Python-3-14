# ctypes - Function prototypes - Code example: >>> from ctypes import POINTER, WINFUNCTYPE, windll, WinError

```python
>>> from ctypes import POINTER, WINFUNCTYPE, windll, WinError
>>> from ctypes.wintypes import BOOL, HWND, RECT
>>> prototype = WINFUNCTYPE(BOOL, HWND, POINTER(RECT))
>>> paramflags = (1, "hwnd"), (2, "lprect")
>>> GetWindowRect = prototype(("GetWindowRect", windll.user32), paramflags)
>>>

```

Functions that have output parameters automatically return the output parameter value when there is just one, or a tuple of the output parameter values when there is more than one, so the GetWindowRect function, once called, now returns a RECT instance.

Output parameters can be paired with the `errcheck` protocol to carry out additional output processing and error checking. Since the win32 `GetWindowRect` api function returns a `BOOL` indicating success or failure, this function could perform the error checking and raise an exception whenever the api call failed:

```python
>>> def errcheck(result, func, args):
...     if not result:
...         raise WinError()
...     return args
...
>>> GetWindowRect.errcheck = errcheck
>>>

```

When the `errcheck` function passes back unchanged the argument tuple it was given, `ctypes` proceeds with the normal handling it applies to the output parameters. Should you prefer to return a tuple of window coordinates rather than a `RECT` instance, you can pull out the fields inside the function and return those instead, at which point the normal handling will no longer occur:

```python
>>> def errcheck(result, func, args):
...     if not result:
...         raise WinError()
...     rc = args[1]
...     return rc.left, rc.top, rc.bottom, rc.right
...
>>> GetWindowRect.errcheck = errcheck
>>>

```

[Subject index](INDEX.md) · [Previous](prototype.md) · [Continue](ctypes-addressof-to-ctypes-create-string-buffer.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: Function prototypes](ctypes-cfunctype-to-prototype.md) · [Owning module, declaration or section: prototype](prototype.md)

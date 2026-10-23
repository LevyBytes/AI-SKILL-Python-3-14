# ctypes - Function prototypes - Signature and initial contract

prototype(*vtbl_index*, *name*[, *paramflags*[, *iid*]])

Hands back a foreign function that invokes a COM method. *vtbl_index*, a small non-negative integer, gives the position inside the virtual function table. *name* is name of the COM method. *iid*, optional, is a pointer to the interface identifier, employed for extended error reporting.

When *iid* is left out, a failing COM method call raises an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError). When *iid* is supplied, a `COMError` is raised in its place.

COM methods follow a special calling convention: beyond the parameters listed in the `argtypes` tuple, they need a pointer to the COM interface as the first argument.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

The optional *paramflags* parameter yields foreign function wrappers with considerably richer functionality than what was outlined above.

*paramflags* must be a tuple of the same length as `argtypes`.

Every item in this tuple holds more detail about one parameter; it must be a tuple of one, two, or three items.

The first item is an integer holding a combination of direction flags for the parameter:

>

1

Marks a parameter as input to the function.

2

Output parameter. A value is filled in by the foreign function.

4

An input parameter whose default is the integer zero.

The second item, optional, gives the parameter name as a string. Once that is provided, the foreign function accepts named parameters.

The third item, optional, supplies this parameter's default value.

The example below shows how to wrap the Windows `MessageBoxW` function so it allows default parameters and named arguments. From the windows header file, the C declaration reads:

```python
WINUSERAPI int WINAPI
MessageBoxW(
    HWND hWnd,
    LPCWSTR lpText,
    LPCWSTR lpCaption,
    UINT uType);

```

Here is the wrapping with `ctypes`:

```python
>>> from ctypes import c_int, WINFUNCTYPE, windll
>>> from ctypes.wintypes import HWND, LPCWSTR, UINT
>>> prototype = WINFUNCTYPE(c_int, HWND, LPCWSTR, LPCWSTR, UINT)
>>> paramflags = (1, "hwnd", 0), (1, "text", "Hi"), (1, "caption", "Hello from ctypes"), (1, "flags", 0)
>>> MessageBox = prototype(("MessageBoxW", windll.user32), paramflags)

```

The `MessageBox` foreign function can now be called in these ways:

```python
>>> MessageBox()
>>> MessageBox(text="Spam, spam, spam")
>>> MessageBox(flags=2, text="foo bar")

```

A further example illustrates output parameters. The win32 `GetWindowRect` function obtains the dimensions of a given window by writing them into a `RECT` structure the caller must provide. The C declaration is:

```python
WINUSERAPI BOOL WINAPI
GetWindowRect(
     HWND hWnd,
     LPRECT lpRect);

```

Here is the wrapping with `ctypes`:

[Subject index](INDEX.md) · [Previous](ctypes-cfunctype-to-prototype.md) · [Continue](windows-function-prototype-example.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: Function prototypes](ctypes-cfunctype-to-prototype.md)

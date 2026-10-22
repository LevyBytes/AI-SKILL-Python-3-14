# ctypes — Accessing functions from loaded dlls

### Accessing functions from loaded dlls

Functions surface as attributes on the dll objects:

```python
>>> libc.printf
<_FuncPtr object at 0x...>
>>> print(windll.kernel32.GetModuleHandleA)
<_FuncPtr object at 0x...>
>>> print(windll.kernel32.MyOwnFunction)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "ctypes.py", line 239, in __getattr__
    func = _StdcallFuncPtr(name, self)
AttributeError: function 'MyOwnFunction' not found
>>>

```

Be aware that win32 system dlls such as `kernel32` and `user32` frequently export both ANSI and UNICODE flavors of a given function. The UNICODE flavor carries a `W` suffix on its name, while the ANSI flavor carries an `A` suffix. The win32 `GetModuleHandle` function — which yields a *module handle* for a supplied module name — has the C prototype below, and a macro decides which of the two is surfaced as `GetModuleHandle`, depending on whether UNICODE has been defined:

```python
/* ANSI version */
HMODULE GetModuleHandleA(LPCSTR lpModuleName);
/* UNICODE version */
HMODULE GetModuleHandleW(LPCWSTR lpModuleName);

```

*windll* makes no magical attempt to pick between them; you must reach for the variant you require by naming `GetModuleHandleA` or `GetModuleHandleW` explicitly, then calling it with bytes or string objects as appropriate.

Occasionally, dlls export functions whose names are not legal Python identifiers, such as `"??2@YAPAXI@Z"`. When that happens you must turn to [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr) to fetch the function:

```python
>>> getattr(cdll.msvcrt, "??2@YAPAXI@Z")
<_FuncPtr object at 0x...>
>>>

```

On Windows, certain dlls export functions by ordinal rather than by name. You reach such functions by indexing the dll object with the ordinal number:

```python
>>> cdll.kernel32[1]
<_FuncPtr object at 0x...>
>>> cdll.kernel32[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "ctypes.py", line 310, in __getitem__
    func = _StdcallFuncPtr(name, self)
AttributeError: function ordinal 0 not found
>>>

```

[Subject index](INDEX.md) · [Previous](loading-dynamic-link-libraries.md) · [Continue](calling-functions.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)

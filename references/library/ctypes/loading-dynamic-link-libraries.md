# ctypes - Loading dynamic link libraries

### Loading dynamic link libraries

`ctypes` exposes the `cdll` object, plus `windll` and `oledll` on Windows, which serve to load dynamic link libraries.

Libraries are loaded by referencing them as attributes on these objects. `cdll` handles libraries whose functions are exported using the standard `cdecl` calling convention, whereas `windll` libraries invoke their functions through the `stdcall` calling convention. `oledll` likewise relies on the `stdcall` calling convention but additionally treats the functions as returning a Windows `HRESULT` error code. That error code drives the automatic raising of an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception whenever the function call fails.

Changed in version 3.3: Windows errors formerly raised [`WindowsError`](https://docs.python.org/3.14/library/exceptions.html#WindowsError), which has since become an alias of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

What follows are a few Windows examples. Keep in mind that `msvcrt` is the MS standard C library that holds the bulk of the standard C functions, and it adopts the `cdecl` calling convention:

```python
>>> from ctypes import *
>>> print(windll.kernel32)
<WinDLL 'kernel32', handle ... at ...>
>>> print(cdll.msvcrt)
<CDLL 'msvcrt', handle ... at ...>
>>> libc = cdll.msvcrt
>>>

```

The customary `.dll` file suffix is tacked on automatically by Windows.

Note

Reaching the standard C library by way of `cdll.msvcrt` pulls in a stale version of the library, one that may clash with the version Python itself relies on. Wherever you can, prefer native Python functionality; failing that, import and rely on the `msvcrt` module.

On other systems, loading a library demands the filename *including* the extension, so attribute access is not a viable way to load them. Instead, either invoke the `LoadLibrary()` method of the dll loaders, or load the library by constructing an instance of `CDLL` through its constructor.

As an illustration, on Linux:

```python
>>> cdll.LoadLibrary("libc.so.6")
<CDLL 'libc.so.6', handle ... at ...>
>>> libc = CDLL("libc.so.6")
>>> libc
<CDLL 'libc.so.6', handle ... at ...>
>>>

```

On macOS:

```python
>>> cdll.LoadLibrary("libc.dylib")
<CDLL 'libc.dylib', handle ... at ...>
>>> libc = CDLL("libc.dylib")
>>> libc
<CDLL 'libc.dylib', handle ... at ...>

```

[Subject index](INDEX.md) · [Previous](ctypes-tutorial.md) · [Continue](accessing-functions-from-loaded-dlls.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)

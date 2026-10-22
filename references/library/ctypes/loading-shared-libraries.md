# ctypes: Shared-library loading flags and Windows error state

Setting the *use_last_error* parameter to true turns on the equivalent behavior for the Windows error code, which the `GetLastError()` and `SetLastError()` Windows API functions handle; you read and update the ctypes private copy of that windows error code through `ctypes.get_last_error()` and `ctypes.set_last_error()`.

On Windows, the *winmode* parameter controls the way the library gets loaded (because *mode* has no effect there). Any value accepted by the Win32 API `LoadLibraryEx` flags parameter is allowed. If you leave it out, the default chooses flags that produce the most secure DLL load, sidestepping problems like DLL hijacking. The surest way to load the intended library along with its dependencies is to supply the DLL's full path.

Building a `CDLL` instance on Windows can still fail even when a DLL of that name is present. Should a DLL that the loaded DLL depends on be missing, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) error is raised carrying the text *“[WinError 126] The specified module could not be found”.* The message leaves out the name of the absent DLL because the Windows API never surfaces that detail, which makes the failure tricky to track down. Clearing it up requires identifying the dependent DLLs and pinpointing the missing one with Windows debugging and tracing tools.

See also

[Microsoft DUMPBIN tool](https://learn.microsoft.com/en-us/cpp/build/reference/dumpbin-reference?view=msvc-170) – A tool to find DLL dependents.

Changed in version 3.8: Added *winmode* parameter.

Changed in version 3.12: The *name* parameter can now be a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

This class exposes no public methods to instances. You reach functions provided by the shared library either as attributes or via indexing. Be aware that fetching a function as an attribute caches it, so each subsequent attribute access yields the very same object. Indexing, by contrast, hands back a fresh object on every access:

```python
>>> from ctypes import CDLL
>>> libc = CDLL("libc.so.6")  # On Linux
>>> libc.time == libc.time
True
>>> libc['time'] == libc['time']
False

```

These public attributes exist. They are prefixed with an underscore so they do not collide with the names of exported functions:

 _handle

The system handle through which the library is reached.

 _name

The library name that was handed to the constructor.

[Subject index](INDEX.md) · [Continue](ctypes-oledll-class.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: ctypes.CDLL](ctypes-cdll-class.md) · [Owning module, declaration or section: Loading shared libraries](ctypes-cdll-class.md) · [Preceding source contract and version conditions](ctypes-cdll-class.md)

# ctypes: `ctypes.OleDLL`

*class *ctypes.OleDLL

Refer to the superclass `CDLL` for shared details.

The functions in this library follow the `stdcall` calling convention and are expected to hand back the windows specific `HRESULT` code. An `HRESULT` value carries data about whether the call succeeded or failed plus a supplementary error code. Whenever the return value indicates failure, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised on your behalf.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

Changed in version 3.3: the exception raised was formerly [`WindowsError`](https://docs.python.org/3.14/library/exceptions.html#WindowsError), nowadays just an alias for [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

[Subject index](INDEX.md) · [Previous](loading-shared-libraries.md) · [Continue](ctypes-windll-class.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: Loading shared libraries](ctypes-cdll-class.md)

# ctypes — Exceptions

### Exceptions

`*exception *ctypes.ArgumentError`

Thrown whenever a call into a foreign function is unable to convert one of the arguments handed to it.

`*exception *ctypes.COMError(*hresult*, *text*, *details*)`

Thrown whenever a COM method call has failed.

`hresult`

The integer that stands for the error code.

`text`

The error message itself.

`details`

The 5-tuple `(descr, source, helpfile, helpcontext, progid)`.

In this tuple, *descr* holds the description in text form. *source* gives the language-dependent `ProgID` tied to whichever class or application set off the error. *helpfile* points to where the help file lives. *helpcontext* names the help-context identifier. Finally, *progid* supplies the `ProgID` for whatever interface defined this error.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](ctypes-pointer-class.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)

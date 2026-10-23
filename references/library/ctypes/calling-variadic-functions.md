# ctypes - Calling variadic functions

### Calling variadic functions

Across many platforms, calling variadic functions via ctypes is indistinguishable from calling functions that take a fixed parameter count. On certain platforms, however — ARM64 for Apple Platforms being the notable case — the calling convention used for variadic functions diverges from the one used for ordinary functions.

On those platforms you must supply the `argtypes` attribute for the regular, non-variadic, function arguments:

```python
libc.printf.argtypes = [ctypes.c_char_p]

```

Since declaring the attribute does not hurt portability, the recommended practice is to always supply `argtypes` for every variadic function.

[Subject index](INDEX.md) · [Previous](calling-functions-continued.md) · [Continue](calling-functions-with-your-own-custom-data-types.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)

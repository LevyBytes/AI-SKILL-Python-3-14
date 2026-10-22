# Python 3.11.0 alpha 6 / library / ctypes

[bpo-46323](https://bugs.python.org/issue?@action=redirect&bpo=46323): [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) now reserves memory on the stack rather than the heap when passing arguments during a call into a Python callback function. Donghee Na wrote the patch.

[bpo-45898](https://bugs.python.org/issue?@action=redirect&bpo=45898): [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) stops defining `ffi_type_*` symbols inside `cfield.c`. libffi has shipped those symbols for more than ten years.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

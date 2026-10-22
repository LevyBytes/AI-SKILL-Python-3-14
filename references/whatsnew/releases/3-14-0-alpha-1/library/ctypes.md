# Python 3.14.0 alpha 1 / library / ctypes

[gh-100980](https://github.com/python/cpython/issues/100980): The [`_fields_`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure._fields_) attribute on [`ctypes.Structure`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure) and [`Union`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Union) no longer gets assigned whenever the setattr operation throws an error.

[gh-61103](https://github.com/python/cpython/issues/61103): Where the compiler offers C11 complex arithmetic, [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) now accepts the C types float complex, double complex and long double complex, exposing them respectively as [`c_float_complex`](https://docs.python.org/3.14/library/ctypes.html#ctypes.c_float_complex), [`c_double_complex`](https://docs.python.org/3.14/library/ctypes.html#ctypes.c_double_complex) and [`c_longdouble_complex`](https://docs.python.org/3.14/library/ctypes.html#ctypes.c_longdouble_complex). Patch by Sergey B Kirpichev.

[gh-105733](https://github.com/python/cpython/issues/105733): [`ctypes.ARRAY()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.ARRAY) is now [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated): no deprecation warnings come from it any longer and nothing is slated to remove it.

[gh-117142](https://github.com/python/cpython/issues/117142): The [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) module is now importable within every subinterpreter, even ones owning their own GIL.

[gh-110190](https://github.com/python/cpython/issues/110190): ctypes structs carrying an array on SPARC are fixed by giving `MAX_STRUCT_SIZE` a value of 32 in stgdict. Jakub Kulik contributed this

[gh-125206](https://github.com/python/cpython/issues/125206): A workaround covering old libffi versions has been added. The ctypes module handles double complex only when libffi >= 3.3.0. Patch by Mikhail Efimov.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

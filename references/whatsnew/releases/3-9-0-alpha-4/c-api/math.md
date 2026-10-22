# Python 3.9.0 alpha 4 / c api / math

[bpo-35081](https://bugs.python.org/issue?@action=redirect&bpo=35081): Relocate the `dtoa.h` header file into the internal C API as `pycore_dtoa.h`: it carries only private functions (prefixed by `_Py`). The [`math`](https://docs.python.org/3.14/library/math.html#module-math) and [`cmath`](https://docs.python.org/3.14/library/cmath.html#module-cmath) modules from now on require compilation with the `Py_BUILD_CORE` macro defined.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

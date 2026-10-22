# Python 3.14.4 final / library / struct

[gh-145750](https://github.com/python/cpython/issues/145750): Steers clear of undefined behaviour from signed integer overflow while parsing format strings inside the [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) module. OSS Fuzz reported it in [#488466741](https://issues.oss-fuzz.com/issues/488466741).

[gh-145623](https://github.com/python/cpython/issues/145623): Corrects a crash inside [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) that fires when calling [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) or `__sizeof__()` upon an uninitialized [`struct.Struct`](https://docs.python.org/3.14/library/struct.html#struct.Struct) object built through `Struct.__new__()` without any `__init__()` call.

[gh-145158](https://github.com/python/cpython/issues/145158): Steers clear of undefined behaviour from signed integer overflow while parsing format strings inside the [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) module.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

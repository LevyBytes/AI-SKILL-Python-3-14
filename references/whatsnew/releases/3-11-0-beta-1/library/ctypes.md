# Python 3.11.0 beta 1 / library / ctypes

[gh-92356](https://github.com/python/cpython/issues/92356): Resolve a performance regression affecting ctypes function calls.

[bpo-47197](https://bugs.python.org/issue?@action=redirect&bpo=47197): ctypes previously mishandled `void` return types; for example a function declared as `ctypes.CFUNCTYPE(None, ctypes.c_int)` ended up called with the signature `int f(int)` rather than `void f(int)`. Because Wasm targets demand that function pointers be invoked with correct signatures, this produced crashes. That problem is now resolved.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# What's new in Python 3.14 / Free-threaded mode improvements — contextvars, decimal, sys, sysconfig, threading, warnings

> (Contributed by Ken Jin in [gh-128563](https://github.com/python/cpython/issues/128563), with ideas on how to implement this in CPython by Mark Shannon, Garrett Gu, Haoran Xu, and Josh Haberman.)

### Free-threaded mode improvements

Originally introduced in 3.13, CPython's free-threaded mode ([**PEP 703**](https://peps.python.org/pep-0703/)) has seen substantial refinement in Python 3.14. What PEP 703 laid out is now complete, C API changes included, and stopgap measures inside the interpreter have given way to lasting fixes. With the specializing adaptive interpreter ([**PEP 659**](https://peps.python.org/pep-0659/)) now active under free-threaded mode, performance climbs sharply thanks to that plus a host of further optimizations. Single-threaded code under free-threaded mode now pays a penalty of around 5-10%, varying by platform and the C compiler in use.

Starting with Python 3.14, building extension modules against the free-threaded CPython on Windows means the build backend must explicitly set the `Py_GIL_DISABLED` preprocessor variable, since the C compiler will no longer infer it on its own. To read which value applied when a live interpreter was compiled, call [`sysconfig.get_config_var()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_config_var).

Whether concurrent safe warnings control is on gets governed by the new [`-X context_aware_warnings`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) flag. Its default is true on the free-threaded build and false on the GIL-enabled build.

There is also a fresh [`thread_inherit_context`](https://docs.python.org/3.14/library/sys.html#sys.flags.thread_inherit_context) flag; when turned on, any thread spun up via [`threading.Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread) begins holding a copy of the [`Context()`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) belonging to whoever invoked [`start()`](https://docs.python.org/3.14/library/threading.html#threading.Thread.start). Crucially, this lets the warning-filtering context set up by [`catch_warnings`](https://docs.python.org/3.14/library/warnings.html#warnings.catch_warnings) be "inherited" by threads (or asyncio tasks) launched inside that context. Other modules leaning on context variables feel the effect too, the [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) context manager among them. On the free-threaded build this flag is true by default, whereas on the GIL-enabled build it is false.

[Subject index](INDEX.md) · [Previous source section](a-new-type-of-interpreter.md) · [Next source section](syntax-error-hints.md) · [Release/subject declaration](summary-release-highlights.md)

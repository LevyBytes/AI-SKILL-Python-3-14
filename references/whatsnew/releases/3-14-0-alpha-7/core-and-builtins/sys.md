# Python 3.14.0 alpha 7 / core and builtins / sys

[gh-131591](https://github.com/python/cpython/issues/131591): Implemented [**PEP 768**](https://peps.python.org/pep-0768/) (Safe external debugger interface for CPython). A new [`sys.remote_exec()`](https://docs.python.org/3.14/library/sys.html#sys.remote_exec) function joins the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) module. It arranges for a Python file to run inside a separate process. Pablo Galindo, Matt Wozniski and Ivona Stojanovic wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.5.1 release candidate 1 / core and builtins / compiler and parser

[bpo-25630](https://bugs.python.org/issue?@action=redirect&bpo=25630): Corrected a potential segfault while parsing arguments inside functions that take filesystem paths.

[bpo-25555](https://bugs.python.org/issue?@action=redirect&bpo=25555): Corrected the parser and AST so that the lineno and col_offset of the "arg" node get filled when AST is compiled from Python objects.

[bpo-25150](https://bugs.python.org/issue?@action=redirect&bpo=25150): Concealed the private `_Py_atomic_*xxx*` symbols away from the public Python.h header to resolve a compilation error under OpenMP. PyThreadState_GET() turns into an alias for PyThreadState_Get() so as to dodge ABI incompatibilities.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

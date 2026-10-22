# Python 3.9.0 alpha 2 / core and builtins / numbers

[bpo-38858](https://bugs.python.org/issue?@action=redirect&bpo=38858): Every Python subinterpreter now keeps its own “small integer singletons” covering numbers in the [-5; 257] range. Changing how many small integers exist at build time is no longer possible by overriding the `NSMALLNEGINTS` and `NSMALLPOSINTS` macros: those macros must instead be edited by hand inside the `pycore_pystate.h` header file.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

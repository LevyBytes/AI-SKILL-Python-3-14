# Python 3.7.0 alpha 2 / core and builtins / pdb

[bpo-31353](https://bugs.python.org/issue?@action=redirect&bpo=31353): [**PEP 553**](https://peps.python.org/pep-0553/) - Introduce a new built-in named `breakpoint()` that invokes `sys.breakpointhook()`. Out of the box this imports `pdb` and runs `pdb.set_trace()`, though users can replace `sys.breakpointhook()` to launch whichever debugger they prefer. The hook's original value is kept in `sys.__breakpointhook__`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

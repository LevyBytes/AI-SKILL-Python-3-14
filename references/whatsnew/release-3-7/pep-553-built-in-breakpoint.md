# What's New In Python 3.7 / PEP 553: Built-in `breakpoint()` — pdb, sys

### PEP 553: Built-in `breakpoint()`

Python 3.7 ships the new built-in [`breakpoint()`](https://docs.python.org/3.14/library/functions.html#breakpoint) function, offering a simple and uniform route into the Python debugger.

Calling the built-in `breakpoint()` invokes [`sys.breakpointhook()`](https://docs.python.org/3.14/library/sys.html#sys.breakpointhook). That hook, by default, imports [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) and afterward runs `pdb.set_trace()`; however, reassign `sys.breakpointhook()` to whatever function you prefer and `breakpoint()` will launch any debugger. On top of that, you can point the [`PYTHONBREAKPOINT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONBREAKPOINT) environment variable at the callable for whichever debugger you favor. Use `PYTHONBREAKPOINT=0` to switch off the built-in `breakpoint()` entirely.

See also

[**PEP 553**](https://peps.python.org/pep-0553/) — Built-in breakpoint()

PEP written and implemented by Barry Warsaw

[Subject index](INDEX.md) · [Previous source section](pep-540-forced-utf-8-runtime-mode.md) · [Next source section](pep-539-new-c-api-for-thread-local-storage.md) · [Release/subject declaration](summary-release-highlights.md)

# Is there a source code-level debugger with breakpoints and single-stepping?

### Programming FAQ

### General questions

### Is there a source code-level debugger with breakpoints and single-stepping?

Yes.

The sections that follow cover several Python debuggers, and the built-in [`breakpoint()`](https://docs.python.org/3.14/library/functions.html#breakpoint) function lets you enter any of them.

For Python, the pdb module offers a basic yet capable console-mode debugger. It ships with the standard Python library and is [`documented in the Library Reference Manual`](https://docs.python.org/3.14/library/pdb.html#module-pdb). Using the pdb source as a model, you can even build a debugger of your own.

IDLE, the interactive development environment bundled with the standard Python distribution (typically reachable as [`idlelib`](https://docs.python.org/3.14/library/idle.html#module-idlelib)), comes with a graphical debugger.

PythonWin is a Python IDE shipping with a pdb-based GUI debugger. The PythonWin debugger highlights breakpoints in color and offers several neat capabilities, including the debugging of non-PythonWin programs. You can obtain PythonWin through the [pywin32](https://github.com/mhammond/pywin32) project and within the [ActivePython](https://www.activestate.com/products/python/) distribution.

[Eric](https://eric-ide.python-projects.org/) is an IDE constructed on top of PyQt and the Scintilla editing widget.

[trepan3k](https://github.com/rocky/python3-trepan/) is a gdb-like debugger.

[Visual Studio Code](https://code.visualstudio.com/) is an IDE whose debugging features tie into version-control software.

A range of commercial Python IDEs ship with graphical debuggers. Among them are:

- [Wing IDE](https://wingware.com/)

- [PyCharm](https://www.jetbrains.com/pycharm/)

[Subject index](INDEX.md)

# PYTHONINSPECT

PYTHONINSPECT

When this holds a non-empty string it amounts to giving the `-i` option.

Python code can likewise alter this variable through [`os.environ`](https://docs.python.org/3.14/library/os.html#os.environ) to compel inspect mode once the program ends.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `cpython.run_stdin` with no arguments.

Changed in version 3.12.5: (also 3.11.10, 3.10.15, 3.9.20, and 3.8.20) Emits audit events.

Changed in version 3.13: Relies on PyREPL where feasible; when that happens, `PYTHONSTARTUP` runs as well. Emits audit events.

[Subject index](INDEX.md) · [Previous source section](pythondebug.md) · [Following source section](pythonunbuffered.md)

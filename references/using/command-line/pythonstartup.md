# PYTHONSTARTUP

PYTHONSTARTUP

When this names a readable file, the Python commands inside that file run before the very first prompt appears in interactive mode. The file runs within the same namespace where interactive commands run, so that objects defined or imported there can be referenced without qualification during the interactive session. You may likewise alter the prompts [`sys.ps1`](https://docs.python.org/3.14/library/sys.html#sys.ps1) and [`sys.ps2`](https://docs.python.org/3.14/library/sys.html#sys.ps2) plus the hook [`sys.__interactivehook__`](https://docs.python.org/3.14/library/sys.html#sys.__interactivehook__) inside this file.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `cpython.run_startup` with the filename as the argument when called on startup.

[Subject index](INDEX.md) · [Previous source section](pythonplatlibdir.md) · [Following source section](pythonoptimize.md)

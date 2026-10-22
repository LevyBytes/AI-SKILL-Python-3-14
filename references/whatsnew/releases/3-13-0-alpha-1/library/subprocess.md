# Python 3.13.0 alpha 1 / library / subprocess

[gh-104372](https://github.com/python/cpython/issues/104372): On Linux, where [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) may lean on the `vfork()` syscall to spawn faster, the parent process no longer stalls other threads: it releases the GIL while awaiting the vfork'ed child process `exec()` result. That keeps launching a binary off a slow filesystem from holding up the rest of the program.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

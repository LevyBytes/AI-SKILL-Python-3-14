# Using the Debug build and Development mode

### Using the Debug build and Development mode

To make debugging smoother, consider doing the following:

- Run a [debug build](https://docs.python.org/3.14/using/configure.html#debug-build) of Python. (Building from source, pass `configure --with-pydebug`. On Linux distros, install and run a package such as `python-debug` or `python-dbg` where one exists.)

- Turn on the runtime [development mode](https://docs.python.org/3.14/library/devmode.html#devmode) (`-X dev`).

Each one switches on additional assertions and switches off certain optimizations. Now and then that conceals the very bug you are chasing, yet for the most part it smooths the way.

[Subject index](INDEX.md) · [Previous source context](setup-for-python-from-a-linux-distro.md) · [Following source context](using-the-python-gdb-extension.md)

# The global interpreter lock in free-threaded Python

### The global interpreter lock in free-threaded Python

Even on free-threaded CPython, you have the choice to turn the GIL back on at runtime, either through the [`PYTHON_GIL`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_GIL) environment variable or via the [`-X gil`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command-line option.

There is also an automatic path to re-enabling the GIL: importing a C-API extension module that has not declared free-threading support flips it on, and the interpreter emits a warning when that happens.

Beyond each project's own docs, these sites keep tabs on how well widely used packages handle free threading:

- [https://py-free-threading.github.io/tracking/](https://py-free-threading.github.io/tracking/)

- [https://hugovk.github.io/free-threaded-wheels/](https://hugovk.github.io/free-threaded-wheels/)

[Subject index](INDEX.md) · [Previous source context](identifying-free-threaded-python.md) · [Following source context](thread-safety.md)

# --disable-gil

--disable-gil

Turns on the ability to run Python free of the [global interpreter lock](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock) (GIL): a [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build).

Defines the `Py_GIL_DISABLED` macro and appends `"t"` onto [`sys.abiflags`](https://docs.python.org/3.14/library/sys.html#sys.abiflags).

For further detail consult [Free-threaded CPython](https://docs.python.org/3.14/whatsnew/3.13.html#whatsnew313-free-threaded-cpython).

Added in version 3.13.

[Subject index](INDEX.md) · [Previous source section](enable-pystats-object-and-garbage-collector-statistics.md) · [Following source section](enable-experimental-jit-no-yes-yes-off-interpreter.md)

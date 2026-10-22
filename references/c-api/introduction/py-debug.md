# Debugging Builds

### Debugging Builds

Several macros can be compiled into Python to switch on additional checks of the interpreter and of extension modules. Because these checks generally impose a hefty runtime cost, they stay off by default.

The file `Misc/SpecialBuilds.txt` in the Python source distribution contains a complete catalog of the assorted debugging-build varieties. There are builds offering reference-count tracing, memory-allocator debugging, or low-level profiling of the interpreter's main loop. Only the builds used most often will get coverage through the rest of this section.

 Py_DEBUG

Building the interpreter with the `Py_DEBUG` macro set yields what people usually mean by [a debug build of Python](https://docs.python.org/3.14/using/configure.html#debug-build). In the Unix build, `Py_DEBUG` is turned on by passing [`--with-pydebug`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-pydebug) to the `./configure` command. It's likewise implied whenever the non-Python-specific `_DEBUG` macro is present. With `Py_DEBUG` turned on in the Unix build, compiler optimization gets switched off.

Beyond the reference-count debugging covered below, further checks run; see [Python Debug Build](https://docs.python.org/3.14/using/configure.html#debug-build).

Setting `Py_TRACE_REFS` switches on reference tracing (consult the [`configure --with-trace-refs option`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-trace-refs)). Once defined, a circular doubly linked list of live objects is kept by appending two more fields to every [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject). Total allocations get counted too. At exit, all references that remain are printed. (Under interactive mode this occurs following every statement the interpreter runs.)

For fuller detail, please see `Misc/SpecialBuilds.txt` within the Python source distribution.

[Subject index](INDEX.md) · [Previous source contract](embedding-python.md) · [Following source contract](pyo3.md)

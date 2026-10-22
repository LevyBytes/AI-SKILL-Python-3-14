# --with-trace-refs

--with-trace-refs

Turn on reference tracing for debugging needs (off by default).

Effects:

- Define the `Py_TRACE_REFS` macro.

- Add [`sys.getobjects()`](https://docs.python.org/3.14/library/sys.html#sys.getobjects) function.

- Add [`PYTHONDUMPREFS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONDUMPREFS) environment variable.

Setting the [`PYTHONDUMPREFS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONDUMPREFS) environment variable lets you print out the objects and reference counts that remain alive when Python shuts down.

[Statically allocated objects](https://docs.python.org/3.14/c-api/typeobj.html#static-types) go untraced.

Added in version 3.8.

Changed in version 3.13: This build now keeps ABI compatibility with both the release and the debug build.

[Subject index](INDEX.md) · [Previous source section](with-pydebug.md) · [Following source section](with-assertions.md)

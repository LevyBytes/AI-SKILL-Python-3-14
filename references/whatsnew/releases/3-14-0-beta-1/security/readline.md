# Python 3.14.0 beta 1 / security / readline

[gh-115322](https://github.com/python/cpython/issues/115322): The C extension modules sitting beneath [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline):, [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess), and [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) will now emit audit events from code paths not previously instrumented that may touch the file system through C function invocation and spawning of external binaries. Additionally, the `ctypes.call_function` audit hook was corrected so that its `function pointer` is reported as an unsigned value.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

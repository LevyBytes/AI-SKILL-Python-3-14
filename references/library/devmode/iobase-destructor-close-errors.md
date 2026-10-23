# Effects of the Python Development Mode - Contract: Any `close()` exceptions raised by the `io.IOBase` destructor get written to the log.

Any `close()` exceptions raised by the [`io.IOBase`](https://docs.python.org/3.14/library/io.html#io.IOBase) destructor get written to the log.

- Flips the [`dev_mode`](https://docs.python.org/3.14/library/sys.html#sys.flags.dev_mode) attribute on [`sys.flags`](https://docs.python.org/3.14/library/sys.html#sys.flags) to `True`.

By default the Python Development Mode leaves the [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) module switched off, since the toll it takes on performance and memory would be too steep. Turning the `tracemalloc` module on yields extra detail about where certain errors come from. To illustrate, [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) records the traceback at the point the resource was allocated, while a buffer overflow error records the traceback at the point the memory block was allocated.

The Python Development Mode does nothing to stop the [`-O`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-O) command line option from stripping [`assert`](https://docs.python.org/3.14/reference/simple_stmts.html#assert) statements or from forcing [`__debug__`](https://docs.python.org/3.14/library/constants.html#debug__) to `False`.

Turning on the Python Development Mode is possible solely at Python startup. You can read its value out of [`sys.flags.dev_mode`](https://docs.python.org/3.14/library/sys.html#sys.flags).

Changed in version 3.8: The [`io.IOBase`](https://docs.python.org/3.14/library/io.html#io.IOBase) destructor now records `close()` exceptions in the log.

Changed in version 3.9: The *encoding* and *errors* arguments now get validated across string encode and decode operations.

[Subject index](INDEX.md) · [Previous](development-mode-effects-overview.md) · [Continue](resourcewarning-example.md) · [Owning module, declaration or section: Effects of the Python Development Mode](development-mode-effects-overview.md)

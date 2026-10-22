# Python 3.14.0 beta 1 / core and builtins / sys

[gh-128555](https://github.com/python/cpython/issues/128555): The [`sys.flags.thread_inherit_context`](https://docs.python.org/3.14/library/sys.html#sys.flags.thread_inherit_context) flag is added.

  - By default, this flag is true on the free-threaded build and false otherwise. When the flag is true, a new thread launched with [`threading.Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread) will, by default, take a copy of the [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) belonging to whoever called [`threading.Thread.start()`](https://docs.python.org/3.14/library/threading.html#threading.Thread.start), rather than running with an empty context.

  - The [`-X thread_inherit_context`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command-line option and the [`PYTHON_THREAD_INHERIT_CONTEXT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_THREAD_INHERIT_CONTEXT) environment variable are added, both of which set the [`thread_inherit_context`](https://docs.python.org/3.14/library/sys.html#sys.flags.thread_inherit_context) flag.

  - A `context` keyword parameter is added to [`Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread). Use it to hand a specific context value to a freshly created thread.

  - The `_contextvars` module is made built-in.

[gh-133231](https://github.com/python/cpython/issues/133231): New helpers for watching JIT compilation are added: [`sys._jit.is_available()`](https://docs.python.org/3.14/library/sys.html#sys._jit.is_available), [`sys._jit.is_enabled()`](https://docs.python.org/3.14/library/sys.html#sys._jit.is_enabled), and [`sys._jit.is_active()`](https://docs.python.org/3.14/library/sys.html#sys._jit.is_active).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

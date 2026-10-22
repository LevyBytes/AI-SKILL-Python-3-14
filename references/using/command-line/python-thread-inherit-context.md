# PYTHON_THREAD_INHERIT_CONTEXT

PYTHON_THREAD_INHERIT_CONTEXT

When this variable holds `1`, a launching [`Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread) will, as its default, take a copy of the context belonging to whoever invoked `Thread.start()`. If it does not, freshly spawned threads begin with no context at all. Left unset, the variable falls back to `1` for free-threaded builds and `0` everywhere else. Refer also to `-X thread_inherit_context`.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous source section](python-gil.md) · [Following source section](python-context-aware-warnings.md)

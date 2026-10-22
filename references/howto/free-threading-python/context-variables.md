# Context variables

### Context variables

On the free-threaded build, the [`thread_inherit_context`](https://docs.python.org/3.14/library/sys.html#sys.flags.thread_inherit_context) flag defaults to true, so any thread spun up with [`threading.Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread) begins life holding a copy of the [`Context()`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) belonging to whoever invoked [`start()`](https://docs.python.org/3.14/library/threading.html#threading.Thread.start). With the standard GIL-enabled build the flag is false by default, leaving new threads with an empty `Context()`.

[Subject index](INDEX.md) · [Previous source context](behavioral-changes.md) · [Following source context](warning-filters.md)

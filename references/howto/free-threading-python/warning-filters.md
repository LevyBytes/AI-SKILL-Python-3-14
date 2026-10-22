# Warning filters

### Warning filters

On the free-threaded build, [`context_aware_warnings`](https://docs.python.org/3.14/library/sys.html#sys.flags.context_aware_warnings) defaults to true, whereas the standard GIL-enabled build leaves it false by default. When the flag is on, the [`warnings.catch_warnings`](https://docs.python.org/3.14/library/warnings.html#warnings.catch_warnings) context manager backs its warning filters with a context variable. When it is off, `catch_warnings` instead edits the shared global filters list, an operation that isn't thread-safe. The [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) module covers this further.

[Subject index](INDEX.md) · [Previous source context](context-variables.md) · [Following source context](increased-memory-usage.md)

# -X context_aware_warnings=*0,1*

- `-X context_aware_warnings=*0,1*` makes the [`warnings.catch_warnings`](https://docs.python.org/3.14/library/warnings.html#warnings.catch_warnings) context manager rely on a [`ContextVar`](https://docs.python.org/3.14/library/contextvars.html#contextvars.ContextVar) for keeping the warnings filter state. When left unset, this option's value falls back to `1` on free-threaded builds and `0` everywhere else. Refer also to `PYTHON_CONTEXT_AWARE_WARNINGS`.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous source section](x-thread-inherit-context-0-1.md) · [Following source section](x-tlbc-0-1.md)

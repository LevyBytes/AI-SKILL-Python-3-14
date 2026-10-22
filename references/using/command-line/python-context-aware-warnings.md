# PYTHON_CONTEXT_AWARE_WARNINGS

PYTHON_CONTEXT_AWARE_WARNINGS

With a value of `1`, the [`warnings.catch_warnings`](https://docs.python.org/3.14/library/warnings.html#warnings.catch_warnings) context manager keeps the warnings filter state inside a [`ContextVar`](https://docs.python.org/3.14/library/contextvars.html#contextvars.ContextVar). When the variable is absent, it falls back to `1` for free-threaded builds and `0` otherwise. Consult `-X context_aware_warnings`.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous source section](python-thread-inherit-context.md) · [Following source section](python-jit.md)

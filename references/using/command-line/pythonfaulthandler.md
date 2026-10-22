# PYTHONFAULTHANDLER

PYTHONFAULTHANDLER

When this environment variable holds a non-empty string, [`faulthandler.enable()`](https://docs.python.org/3.14/library/faulthandler.html#faulthandler.enable) runs at startup: it sets up a handler for the [`SIGSEGV`](https://docs.python.org/3.14/library/signal.html#signal.SIGSEGV), [`SIGFPE`](https://docs.python.org/3.14/library/signal.html#signal.SIGFPE), [`SIGABRT`](https://docs.python.org/3.14/library/signal.html#signal.SIGABRT), [`SIGBUS`](https://docs.python.org/3.14/library/signal.html#signal.SIGBUS) and [`SIGILL`](https://docs.python.org/3.14/library/signal.html#signal.SIGILL) signals to dump the Python traceback. This amounts to the `-X` `faulthandler` option.

Added in version 3.3.

[Subject index](INDEX.md) · [Previous source section](pythonwarnings.md) · [Following source section](pythontracemalloc.md)

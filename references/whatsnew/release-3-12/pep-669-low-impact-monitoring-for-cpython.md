# What’s New In Python 3.12 / PEP 669: Low impact monitoring for CPython — sys.monitoring

### PEP 669: Low impact monitoring for CPython

A new [`API`](https://docs.python.org/3.14/library/sys.monitoring.html#module-sys.monitoring) for profilers, debuggers, and similar tooling to watch events inside CPython is laid out by [**PEP 669**](https://peps.python.org/pep-0669/). A broad set of events is covered, among them calls, returns, lines, exceptions, jumps, and others. The upshot is that the cost tracks usage, enabling debuggers and coverage tools with overhead close to zero. Refer to `sys.monitoring` for the specifics.

(Contributed by Mark Shannon in [gh-103082](https://github.com/python/cpython/issues/103082).)

[Subject index](INDEX.md) · [Previous source section](pep-684-a-per-interpreter-gil.md) · [Next source section](pep-688-making-the-buffer-protocol-accessible-in-python.md) · [Release/subject declaration](summary-release-highlights.md)

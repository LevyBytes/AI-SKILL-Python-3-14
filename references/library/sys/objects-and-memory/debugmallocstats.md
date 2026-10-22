# sys._debugmallocstats

sys._debugmallocstats()

Write low-level details to stderr describing the state of CPython's memory allocator.

When Python is [built in debug mode](https://docs.python.org/3.14/using/configure.html#debug-build) ([`configure --with-pydebug option`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-pydebug)), it additionally runs some costly internal consistency checks.

Added in version 3.3.

**CPython implementation detail:** This function belongs to CPython specifically. The precise output format is left undefined here and is subject to change.

[API family](INDEX.md) · [sys context index](../INDEX.md).

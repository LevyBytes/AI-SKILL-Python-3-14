# What's new in Python 3.14 / asyncio — asyncio-task

### asyncio

- Standard benchmark numbers climbed by 10-20% after a new per-thread doubly linked list for [`native tasks`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) was put in place, which also trims memory usage. That lets outside introspection tooling such as python -m asyncio pstree examine the call graph of asyncio tasks executing across every thread. (Contributed by Kumar Aditya in [gh-107803](https://github.com/python/cpython/issues/107803).)

- The module gains first class support for [free-threading builds](https://docs.python.org/3.14/glossary.html#term-free-threading). That permits running many event loops in parallel over separate threads, scaling linearly alongside the thread count. (Contributed by Kumar Aditya in [gh-128002](https://github.com/python/cpython/issues/128002).)

[Subject index](INDEX.md) · [Previous source section](optimizations.md) · [Next source section](base64.md) · [Release/subject declaration](summary-release-highlights.md)

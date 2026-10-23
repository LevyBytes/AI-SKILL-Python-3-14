# What's New In Python 3.7 / tracemalloc - tracemalloc

### tracemalloc

[`tracemalloc.Traceback`](https://docs.python.org/3.14/library/tracemalloc.html#tracemalloc.Traceback) now resembles ordinary tracebacks more closely, ordering its frames from oldest through most recent. A negative *limit* is now accepted by [`Traceback.format()`](https://docs.python.org/3.14/library/tracemalloc.html#tracemalloc.Traceback.format), which trims the output down to the `abs(limit)` oldest frames. The freshly added *most_recent_first* argument to `Traceback.format()` restores the former behaviour. (Contributed by Jesse Bakker in [bpo-32121](https://bugs.python.org/issue?@action=redirect&bpo=32121).)

[Subject index](INDEX.md) · [Previous source section](tkinter.md) · [Next source section](types.md) · [Release/subject declaration](summary-release-highlights.md)

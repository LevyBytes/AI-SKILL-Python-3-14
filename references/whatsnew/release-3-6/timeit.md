# What's New In Python 3.6 / timeit - timeit

### timeit

So that the cumulative run time reaches at least 200 milliseconds, the fresh [`Timer.autorange()`](https://docs.python.org/3.14/library/timeit.html#timeit.Timer.autorange) convenience method repeatedly invokes [`Timer.timeit()`](https://docs.python.org/3.14/library/timeit.html#timeit.Timer.timeit). (Contributed by Steven D — Aprano in [bpo-6422](https://bugs.python.org/issue?@action=redirect&bpo=6422).)

Should the spread between the best and worst times be sizable (4x), [`timeit`](https://docs.python.org/3.14/library/timeit.html#module-timeit) now issues a warning. (Contributed by Serhiy Storchaka in [bpo-23552](https://bugs.python.org/issue?@action=redirect&bpo=23552).)

[Subject index](INDEX.md) · [Previous source section](time.md) · [Next source section](tkinter.md) · [Release/subject declaration](summary-release-highlights.md)

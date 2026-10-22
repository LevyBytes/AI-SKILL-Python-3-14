# What’s New In Python 3.5 / timeit — timeit

### timeit

To choose the time unit shown in the timer's output, you can now pass the `-u` or `--unit=*U*` command line option. The values it allows are `usec`, `msec`, or `sec`. Julian Gindi landed this (see [bpo-18983](https://bugs.python.org/issue?@action=redirect&bpo=18983)).

There is a new *globals* parameter on the [`timeit()`](https://docs.python.org/3.14/library/timeit.html#timeit.timeit) function for naming the namespace where the code is to execute. Ben Roberts contributed this (see [bpo-2527](https://bugs.python.org/issue?@action=redirect&bpo=2527)).

[Subject index](INDEX.md) · [Previous source section](time.md) · [Next source section](tkinter.md) · [Release/subject declaration](summary-release-highlights.md)

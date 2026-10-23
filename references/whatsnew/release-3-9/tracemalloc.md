# What's New In Python 3.9 / tracemalloc - tracemalloc

### tracemalloc

A new [`tracemalloc.reset_peak()`](https://docs.python.org/3.14/library/tracemalloc.html#tracemalloc.reset_peak) was added; it lowers the recorded peak of traced memory blocks down to the present size, which lets you gauge the peak reached by particular sections of code. (Contributed by Huon Wilson in [bpo-40630](https://bugs.python.org/issue?@action=redirect&bpo=40630).)

[Subject index](INDEX.md) · [Previous source section](sys.md) · [Next source section](typing.md) · [Release/subject declaration](summary-release-highlights.md)

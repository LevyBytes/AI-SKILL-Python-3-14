# What’s New In Python 3.8 / sys - gc, sys

### sys

A new [`sys.unraisablehook()`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook) function arrived that you can override to govern the treatment of "unraisable exceptions." Python invokes it once an exception has surfaced yet no avenue exists for Python to deal with it. As an illustration, that happens when a destructor throws an exception or while garbage collection runs ([`gc.collect()`](https://docs.python.org/3.14/library/gc.html#gc.collect)). (Contributed by Victor Stinner in [bpo-36829](https://bugs.python.org/issue?@action=redirect&bpo=36829).)

[Subject index](INDEX.md) · [Previous source section](statistics.md) · [Next source section](tarfile.md) · [Release/subject declaration](assignment-expressions.md)

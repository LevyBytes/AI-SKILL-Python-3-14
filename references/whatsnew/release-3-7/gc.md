# What's New In Python 3.7 / gc - gc

### gc

A fresh [`gc.freeze()`](https://docs.python.org/3.14/library/gc.html#gc.freeze) function lets you freeze every object the garbage collector is tracking and keep them out of later collections. Doing this ahead of a POSIX `fork()` call helps make the GC copy-on-write friendly or accelerates collection. The fresh [`gc.unfreeze()`](https://docs.python.org/3.14/library/gc.html#gc.unfreeze) functions reverses that. On top of that, you can call [`gc.get_freeze_count()`](https://docs.python.org/3.14/library/gc.html#gc.get_freeze_count) to learn how many objects are frozen. (Contributed by Li Zekun in [bpo-31558](https://bugs.python.org/issue?@action=redirect&bpo=31558).)

[Subject index](INDEX.md) · [Previous source section](functools.md) · [Next source section](hmac.md) · [Release/subject declaration](summary-release-highlights.md)

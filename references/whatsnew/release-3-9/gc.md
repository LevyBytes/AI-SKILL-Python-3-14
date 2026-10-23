# What's New In Python 3.9 / gc - gc

### gc

Whenever the garbage collector runs a pass during which certain objects resurrect (meaning they stay reachable from beyond the isolated cycles once the finalizers have run), it refrains from holding back the collection of every object that is yet unreachable. (Contributed by Pablo Galindo and Tim Peters in [bpo-38379](https://bugs.python.org/issue?@action=redirect&bpo=38379).)

A fresh function [`gc.is_finalized()`](https://docs.python.org/3.14/library/gc.html#gc.is_finalized) was added to test whether the garbage collector has already finalized an object. (Contributed by Pablo Galindo in [bpo-39322](https://bugs.python.org/issue?@action=redirect&bpo=39322).)

[Subject index](INDEX.md) · [Previous source section](ftplib.md) · [Next source section](hashlib.md) · [Release/subject declaration](summary-release-highlights.md)

# What's New In Python 3.7 / concurrent.futures — concurrent.futures

### concurrent.futures

Fresh *initializer* and *initargs* constructor arguments are now accepted by both [`ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) and [`ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor). (Contributed by Antoine Pitrou in [bpo-21423](https://bugs.python.org/issue?@action=redirect&bpo=21423).)

By way of the fresh *mp_context* argument, the [`ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) can be handed a multiprocessing context. (Contributed by Thomas Moreau in [bpo-31540](https://bugs.python.org/issue?@action=redirect&bpo=31540).)

[Subject index](INDEX.md) · [Previous source section](compileall.md) · [Next source section](contextlib.md) · [Release/subject declaration](summary-release-highlights.md)

# What’s New In Python 3.5 / concurrent.futures - concurrent.futures

### concurrent.futures

The [`Executor.map()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Executor.map) method henceforth takes a *chunksize* argument so tasks can be batched for better throughput whenever [`ProcessPoolExecutor()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) is in use. (Contributed by Dan O’Reilly in [bpo-11271](https://bugs.python.org/issue?@action=redirect&bpo=11271).)

Supplying the worker count to the [`ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) constructor is optional these days. Its default works out to 5 times the CPU count. (Contributed by Claudiu Popa in [bpo-21527](https://bugs.python.org/issue?@action=redirect&bpo=21527).)

[Subject index](INDEX.md) · [Previous source section](compileall.md) · [Next source section](configparser.md) · [Release/subject declaration](summary-release-highlights.md)

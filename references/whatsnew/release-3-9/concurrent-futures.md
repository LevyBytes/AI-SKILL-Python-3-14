# What's New In Python 3.9 / concurrent.futures — concurrent.futures

### concurrent.futures

A fresh *cancel_futures* parameter was added to [`concurrent.futures.Executor.shutdown()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Executor.shutdown); it cancels every pending future yet to begin running instead of awaiting their completion ahead of closing the executor. (Contributed by Kyle Stanley in [bpo-39349](https://bugs.python.org/issue?@action=redirect&bpo=39349).)

Daemon threads were taken out of [`ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) and [`ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor). The result is smoother interoperation with subinterpreters and steadier shutdown behavior. (Contributed by Kyle Stanley in [bpo-39812](https://bugs.python.org/issue?@action=redirect&bpo=39812).)

Within [`ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor), workers now appear lazily, spawning solely when no idle worker remains to be reused. That trims launch cost and cuts down the CPU time squandered on idle workers. (Contributed by Kyle Stanley in [bpo-39207](https://bugs.python.org/issue?@action=redirect&bpo=39207).)

[Subject index](INDEX.md) · [Previous source section](compileall.md) · [Next source section](curses.md) · [Release/subject declaration](summary-release-highlights.md)

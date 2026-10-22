# What's New In Python 3.7 / contextlib — contextlib

### contextlib

The fresh [`nullcontext()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.nullcontext) gives you a leaner, quicker do-nothing context manager versus [`ExitStack`](https://docs.python.org/3.14/library/contextlib.html#contextlib.ExitStack). (Contributed by Jesse-Bakker in [bpo-10049](https://bugs.python.org/issue?@action=redirect&bpo=10049).)

To round out their synchronous equivalents, the fresh [`asynccontextmanager()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.asynccontextmanager), [`AbstractAsyncContextManager`](https://docs.python.org/3.14/library/contextlib.html#contextlib.AbstractAsyncContextManager), and [`AsyncExitStack`](https://docs.python.org/3.14/library/contextlib.html#contextlib.AsyncExitStack) were introduced. (Contributed by Jelle Zijlstra in [bpo-29679](https://bugs.python.org/issue?@action=redirect&bpo=29679) and [bpo-30241](https://bugs.python.org/issue?@action=redirect&bpo=30241), and by Alexander Mohr and Ilya Kulakov in [bpo-29302](https://bugs.python.org/issue?@action=redirect&bpo=29302).)

[Subject index](INDEX.md) · [Previous source section](concurrent-futures.md) · [Next source section](cprofile.md) · [Release/subject declaration](summary-release-highlights.md)

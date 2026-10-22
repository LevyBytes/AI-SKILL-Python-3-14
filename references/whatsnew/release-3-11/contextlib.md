# What's New In Python 3.11 / contextlib — contextlib, os

### contextlib

- A non parallel-safe [`chdir()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.chdir) context manager was added; it switches the working directory and puts the prior one back when it exits. The implementation simply wraps [`chdir()`](https://docs.python.org/3.14/library/os.html#os.chdir). (Contributed by Filipe Laíns in [bpo-25625](https://bugs.python.org/issue?@action=redirect&bpo=25625))

[Subject index](INDEX.md) · [Previous source section](asyncio.md) · [Next source section](dataclasses.md) · [Release/subject declaration](summary-release-highlights.md)

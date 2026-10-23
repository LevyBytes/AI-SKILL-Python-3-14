# What's New In Python 3.10 / contextlib - contextlib

### contextlib

Add a [`contextlib.aclosing()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.aclosing) context manager that safely shuts down async generators along with objects standing for asynchronously released resources. (Contributed by Joongi Kim and John Belmonte in [bpo-41229](https://bugs.python.org/issue?@action=redirect&bpo=41229).)

Add support for the asynchronous context manager protocol to [`contextlib.nullcontext()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.nullcontext). (Contributed by Tom Gringauz in [bpo-41543](https://bugs.python.org/issue?@action=redirect&bpo=41543).)

Add [`AsyncContextDecorator`](https://docs.python.org/3.14/library/contextlib.html#contextlib.AsyncContextDecorator) so that async context managers can serve as decorators.

[Subject index](INDEX.md) · [Previous source section](collections-abc.md) · [Next source section](curses.md) · [Release/subject declaration](summary-release-highlights.md)

# What’s New In Python 3.5 / collections.abc — collections.abc

### collections.abc

The `Sequence.index()` method henceforth takes *start* and *stop* arguments so it matches the equivalent methods on [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple), [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), and similar. (Contributed by Devin Jeanpierre in [bpo-23086](https://bugs.python.org/issue?@action=redirect&bpo=23086).)

A fresh [`Generator`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Generator) abstract base class. (Contributed by Stefan Behnel in [bpo-24018](https://bugs.python.org/issue?@action=redirect&bpo=24018).)

Fresh [`Awaitable`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Awaitable), [`Coroutine`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Coroutine), [`AsyncIterator`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.AsyncIterator), and [`AsyncIterable`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.AsyncIterable) abstract base classes. (Contributed by Yury Selivanov in [bpo-24184](https://bugs.python.org/issue?@action=redirect&bpo=24184).)

On older Python releases, you can grab a backport of these new ABCs from an external [PyPI package](https://pypi.org/project/backports_abc/).

[Subject index](INDEX.md) · [Previous source section](collections.md) · [Next source section](compileall.md) · [Release/subject declaration](summary-release-highlights.md)

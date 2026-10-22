# What’s New In Python 3.8 / io — io

> (Contributed by Raymond Hettinger in [bpo-36326](https://bugs.python.org/issue?@action=redirect&bpo=36326).)

### io

Within development mode ([`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `env`) and under a [debug build](https://docs.python.org/3.14/using/configure.html#debug-build), the [`io.IOBase`](https://docs.python.org/3.14/library/io.html#io.IOBase) finalizer now records the exception should its `close()` method fail. Within a release build that exception is, by default, dropped quietly.

[Subject index](INDEX.md) · [Previous source section](inspect.md) · [Next source section](itertools.md) · [Release/subject declaration](assignment-expressions.md)

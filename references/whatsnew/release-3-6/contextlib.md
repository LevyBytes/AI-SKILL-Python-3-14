# What's New In Python 3.6 / contextlib - contextlib, typing

### contextlib

A [`contextlib.AbstractContextManager`](https://docs.python.org/3.14/library/contextlib.html#contextlib.AbstractContextManager) class now exists to serve as an abstract base class for context managers. It supplies a reasonable stock implementation of `__enter__()` returning `self` while keeping `__exit__()` as an abstract method. A counterpart class arrived in the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module under the name [`typing.ContextManager`](https://docs.python.org/3.14/library/typing.html#typing.ContextManager). (Contributed by Brett Cannon in [bpo-25609](https://bugs.python.org/issue?@action=redirect&bpo=25609).)

[Subject index](INDEX.md) · [Previous source section](concurrent-futures.md) · [Next source section](datetime.md) · [Release/subject declaration](summary-release-highlights.md)

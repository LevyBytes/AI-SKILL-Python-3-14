# What’s New In Python 3.5 / io - io

### io

There is a new [`BufferedIOBase.readinto1()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.readinto1) method; at most once does it invoke the underlying raw stream's [`RawIOBase.read()`](https://docs.python.org/3.14/library/io.html#io.RawIOBase.read) or [`RawIOBase.readinto()`](https://docs.python.org/3.14/library/io.html#io.RawIOBase.readinto) methods. (Contributed by Nikolaus Rath in [bpo-20578](https://bugs.python.org/issue?@action=redirect&bpo=20578).)

[Subject index](INDEX.md) · [Previous source section](inspect.md) · [Next source section](ipaddress.md) · [Release/subject declaration](summary-release-highlights.md)

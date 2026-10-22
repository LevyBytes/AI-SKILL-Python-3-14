# What's New In Python 3.9 / nntplib

### nntplib

When the constructor of `NNTP` or `NNTP_SSL` receives a timeout of zero, it now raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), avoiding the accidental creation of a non-blocking socket. (Contributed by Donghee Na in [bpo-39259](https://bugs.python.org/issue?@action=redirect&bpo=39259).)

[Subject index](INDEX.md) · [Previous source section](multiprocessing.md) · [Next source section](os.md) · [Release/subject declaration](summary-release-highlights.md)

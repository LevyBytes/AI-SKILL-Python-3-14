# What's New In Python 3.9 / ftplib - ftplib

### ftplib

[`FTP`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP) plus [`FTP_TLS`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP_TLS) now throw a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) should the constructor receive a zero timeout, heading off creation of a non-blocking socket. (Contributed by Donghee Na in [bpo-39259](https://bugs.python.org/issue?@action=redirect&bpo=39259).)

[Subject index](INDEX.md) · [Previous source section](fcntl.md) · [Next source section](gc.md) · [Release/subject declaration](summary-release-highlights.md)

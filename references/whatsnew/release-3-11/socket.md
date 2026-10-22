# What's New In Python 3.11 / socket — socket

### socket

- CAN Socket support for NetBSD was added. (Contributed by Thomas Klausner in [bpo-30512](https://bugs.python.org/issue?@action=redirect&bpo=30512).)

- [`create_connection()`](https://docs.python.org/3.14/library/socket.html#socket.create_connection) offers a setting that, on connection failure, raises an [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup) bundling every error rather than just the final one. (Contributed by Irit Katriel in [bpo-29980](https://bugs.python.org/issue?@action=redirect&bpo=29980).)

[Subject index](INDEX.md) · [Previous source section](shutil.md) · [Next source section](sqlite3.md) · [Release/subject declaration](summary-release-highlights.md)

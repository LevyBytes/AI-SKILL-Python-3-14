# What's New In Python 3.4 / select - select

### select

[`epoll`](https://docs.python.org/3.14/library/select.html#select.epoll) objects have gained support for the context management protocol. Inside a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement, the [`close()`](https://docs.python.org/3.14/library/select.html#select.epoll.close) method fires by itself once the block finishes. (Contributed by Serhiy Storchaka in [bpo-16488](https://bugs.python.org/issue?@action=redirect&bpo=16488).)

[`devpoll`](https://docs.python.org/3.14/library/select.html#select.devpoll) objects have picked up [`fileno()`](https://docs.python.org/3.14/library/select.html#select.devpoll.fileno) and [`close()`](https://docs.python.org/3.14/library/select.html#select.devpoll.close) methods, plus a brand-new attribute [`closed`](https://docs.python.org/3.14/library/select.html#select.devpoll.closed). (Contributed by Victor Stinner in [bpo-18794](https://bugs.python.org/issue?@action=redirect&bpo=18794).)

[Subject index](INDEX.md) · [Previous source section](resource.md) · [Next source section](shelve.md) · [Release/subject declaration](release-highlights.md)

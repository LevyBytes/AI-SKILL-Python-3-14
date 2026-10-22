# What's New In Python 3.2 / asyncore

### asyncore

A new `handle_accepted()` method on `asyncore.dispatcher` hands back a `(sock, addr)` pair and fires once a connection to a fresh remote endpoint has genuinely been set up. It is meant to take the place of the older `handle_accept()` and spares the user from invoking `accept()` themselves.

(Contributed by Giampaolo Rodolà; [bpo-6706](https://bugs.python.org/issue?@action=redirect&bpo=6706).)

[Subject index](INDEX.md) · [Previous source section](poplib.md) · [Next source section](tempfile.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)

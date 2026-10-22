# What's New In Python 3.2 / socket — socket

### socket

Two enhancements land in the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module.

- A [`detach()`](https://docs.python.org/3.14/library/socket.html#socket.socket.detach) method now exists on socket objects; it moves the socket to a closed state yet leaves the underlying file descriptor open. That descriptor stays available for other work afterward. (Added by Antoine Pitrou; [bpo-8524](https://bugs.python.org/issue?@action=redirect&bpo=8524).)

- The [`socket.create_connection()`](https://docs.python.org/3.14/library/socket.html#socket.create_connection) helper now honors the context management protocol, so it always swallows [`socket.error`](https://docs.python.org/3.14/library/socket.html#socket.error) exceptions and closes the socket once finished. (Contributed by Giampaolo Rodolà; [bpo-9794](https://bugs.python.org/issue?@action=redirect&bpo=9794).)

[Subject index](INDEX.md) · [Previous source section](html.md) · [Next source section](ssl.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)

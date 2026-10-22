# Python 3.5.0 alpha 4 / library / socket

[bpo-23881](https://bugs.python.org/issue?@action=redirect&bpo=23881): Should the FTP connection fail, the urllib.request.ftpwrapper constructor now shuts the socket to clear a ResourceWarning.

[bpo-23853](https://bugs.python.org/issue?@action=redirect&bpo=23853): [`socket.socket.sendall()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendall) no longer resets the socket timeout on every successful send of data. That socket timeout now represents the overall maximum time allowed to transmit all data.

[bpo-23618](https://bugs.python.org/issue?@action=redirect&bpo=23618): [`socket.socket.connect()`](https://docs.python.org/3.14/library/socket.html#socket.socket.connect) now holds on until the connection finishes rather than raising [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) should signals interrupt the connection, provided signal handlers raise no exception and the socket is blocking or carries a timeout. For non-blocking sockets, `socket.socket.connect()` still raise `InterruptedError`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

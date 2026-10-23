# What’s New In Python 3.5 / ssl / Other Changes - ssl

#### Other Changes

To find out the protocol version actually being used, there is now a [`SSLSocket.version()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.version) method. Antoine Pitrou contributed this (see [bpo-20421](https://bugs.python.org/issue?@action=redirect&bpo=20421)).

A `SSLSocket.sendfile()` method is now part of the [`SSLSocket`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket) class. Giampaolo Rodola’ added this (see [bpo-17552](https://bugs.python.org/issue?@action=redirect&bpo=17552)).

On a non-blocking socket, whenever the operation would block, the `SSLSocket.send()` method now throws either the [`ssl.SSLWantReadError`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLWantReadError) or the [`ssl.SSLWantWriteError`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLWantWriteError) exception. Formerly it simply gave back `0`. Nikolaus Rath contributed this (see [bpo-20951](https://bugs.python.org/issue?@action=redirect&bpo=20951)).

Following [**RFC 5280**](https://datatracker.ietf.org/doc/html/rfc5280.html), the [`cert_time_to_seconds()`](https://docs.python.org/3.14/library/ssl.html#ssl.cert_time_to_seconds) function now treats its input time as UTC rather than as local time. On top of that, what it returns is always an [`int`](https://docs.python.org/3.14/library/functions.html#int). Akira Li landed this (see [bpo-19940](https://bugs.python.org/issue?@action=redirect&bpo=19940)).

The ciphers a client offered while handshaking are returned by the new `SSLObject.shared_ciphers()` and [`SSLSocket.shared_ciphers()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.shared_ciphers) methods. Benjamin Peterson contributed this (see [bpo-23186](https://bugs.python.org/issue?@action=redirect&bpo=23186)).

Belonging to the [`SSLSocket`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket) class, the [`SSLSocket.do_handshake()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.do_handshake), [`SSLSocket.read()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.read), `SSLSocket.shutdown()`, and [`SSLSocket.write()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.write) methods no longer restart the socket timeout on every send or receive of bytes. That timeout now stands for the longest total duration of the method as a whole. Victor Stinner added this (see [bpo-23853](https://bugs.python.org/issue?@action=redirect&bpo=23853)).

Matching against IP addresses is now possible through the `match_hostname()` function. Antoine Pitrou landed this (see [bpo-23239](https://bugs.python.org/issue?@action=redirect&bpo=23239)).

[Subject index](INDEX.md) · [Previous source section](ssl-application-layer-protocol-negotiation-support.md) · [Next source section](sqlite3.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](ssl-memory-bio-support.md)

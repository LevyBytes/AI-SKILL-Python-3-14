# What's New In Python 3.10 / socket - socket

### socket

The exception [`socket.timeout`](https://docs.python.org/3.14/library/socket.html#socket.timeout) now serves as an alias of [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError). (Contributed by Christian Heimes in [bpo-42413](https://bugs.python.org/issue?@action=redirect&bpo=42413).)

Add option to create MPTCP sockets with `IPPROTO_MPTCP` (Contributed by Rui Cunha in [bpo-43571](https://bugs.python.org/issue?@action=redirect&bpo=43571).)

Add `IP_RECVTOS` option so the type of service (ToS), or the DSCP/ECN fields, can be received (Contributed by Georg Sauthoff in [bpo-44077](https://bugs.python.org/issue?@action=redirect&bpo=44077).)

[Subject index](INDEX.md) · [Previous source section](site.md) · [Next source section](ssl.md) · [Release/subject declaration](summary-release-highlights.md)

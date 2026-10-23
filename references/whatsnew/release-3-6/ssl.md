# What's New In Python 3.6 / ssl - enum, ssl

### ssl

OpenSSL 1.1.0 is supported by [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl). 1.0.2 is the lowest recommended version. (Contributed by Christian Heimes in [bpo-26470](https://bugs.python.org/issue?@action=redirect&bpo=26470).)

From the default cipher suites, 3DES is gone, while ChaCha20 Poly1305 cipher suites are now included. (Contributed by Christian Heimes in [bpo-27850](https://bugs.python.org/issue?@action=redirect&bpo=27850) and [bpo-27766](https://bugs.python.org/issue?@action=redirect&bpo=27766).)

For options and ciphers, [`SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) ships with stronger default configuration. (Contributed by Christian Heimes in [bpo-28043](https://bugs.python.org/issue?@action=redirect&bpo=28043).)

Via the fresh [`SSLSession`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSession) class, an SSL session may be carried from one client-side connection over to another. By resuming a TLS session you can quicken the opening handshake, cut latency, and boost throughput (Contributed by Christian Heimes in [bpo-19500](https://bugs.python.org/issue?@action=redirect&bpo=19500) based on a draft by Alex Warhawk.)

To fetch the enabled ciphers ranked by cipher priority, you can use the fresh [`get_ciphers()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.get_ciphers) method.

Every flag and constant has been turned into [`IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum) and [`IntFlag`](https://docs.python.org/3.14/library/enum.html#enum.IntFlag). (Contributed by Christian Heimes in [bpo-28025](https://bugs.python.org/issue?@action=redirect&bpo=28025).)

TLS protocols specific to the server side and the client side were added for [`SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext). (Contributed by Christian Heimes in [bpo-28085](https://bugs.python.org/issue?@action=redirect&bpo=28085).)

To switch it on, [`ssl.SSLContext.post_handshake_auth`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.post_handshake_auth) was added, plus [`ssl.SSLSocket.verify_client_post_handshake()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.verify_client_post_handshake) for kicking off TLS 1.3 post-handshake authentication. (Contributed by Christian Heimes in [gh-78851](https://github.com/python/cpython/issues/78851).)

[Subject index](INDEX.md) · [Previous source section](socketserver.md) · [Next source section](statistics.md) · [Release/subject declaration](summary-release-highlights.md)

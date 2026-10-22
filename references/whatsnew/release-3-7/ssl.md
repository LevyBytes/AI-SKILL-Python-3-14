# What's New In Python 3.7 / ssl — ssl

### ssl

For verifying a host name or an IP address, the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module now relies on OpenSSL's builtin API in place of `match_hostname()`. The values get validated as the TLS handshake proceeds. Should any certificate validation error occur, including a failed host name check, an [`SSLCertVerificationError`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLCertVerificationError) is now raised, and the handshake is aborted with a proper TLS Alert message. That new exception carries extra information. You can tailor host name validation through [`SSLContext.hostname_checks_common_name`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.hostname_checks_common_name). (Contributed by Christian Heimes in [bpo-31399](https://bugs.python.org/issue?@action=redirect&bpo=31399).)

Note

This better host name check needs a *libssl* build that works with OpenSSL 1.0.2 or 1.1. Because of that, OpenSSL 0.9.8 along with 1.0.1 are dropped from support (consult Platform Support Removals for further detail). For the most part the ssl module works with LibreSSL 2.7.2 and later.

The `ssl` module will no longer place IP addresses into the SNI TLS extension. (Contributed by Christian Heimes in [bpo-32185](https://bugs.python.org/issue?@action=redirect&bpo=32185).)

`match_hostname()` has dropped support for partial wildcards along the lines of `www*.example.org`. (Contributed by Mandeep Singh in [bpo-23033](https://bugs.python.org/issue?@action=redirect&bpo=23033) and Christian Heimes in [bpo-31399](https://bugs.python.org/issue?@action=redirect&bpo=31399).)

When the `ssl` module picks its default cipher suite, it now follows a blacklist approach rather than relying on a hard-coded whitelist. Ciphers that OpenSSL security updates have blocked are no longer re-enabled by Python. You may configure the default cipher suite selection while compiling. (Contributed by Christian Heimes in [bpo-31429](https://bugs.python.org/issue?@action=redirect&bpo=31429).)

Server certificates that carry internationalized domain names (IDNs) can now be validated. Alongside this change, the [`SSLSocket.server_hostname`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.server_hostname) attribute now keeps the expected hostname in A-label form (`"xn--pythn-mua.org"`) instead of U-label form (`"pythön.org"`). (Contributed by Nathaniel J. Smith and Christian Heimes in [bpo-28414](https://bugs.python.org/issue?@action=redirect&bpo=28414).)

The `ssl` module carries preliminary, experimental support for TLS 1.3 plus OpenSSL 1.1.1. When Python 3.7.0 shipped, OpenSSL 1.1.1 remained in development and TLS 1.3 had yet to be finalized. How the TLS 1.3 handshake and protocol behave differs a bit from TLS 1.2 and earlier; see [TLS 1.3](https://docs.python.org/3.14/library/ssl.html#ssl-tlsv1-3). (Contributed by Christian Heimes in [bpo-32947](https://bugs.python.org/issue?@action=redirect&bpo=32947), [bpo-20995](https://bugs.python.org/issue?@action=redirect&bpo=20995), [bpo-29136](https://bugs.python.org/issue?@action=redirect&bpo=29136), [bpo-30622](https://bugs.python.org/issue?@action=redirect&bpo=30622) and [bpo-33618](https://bugs.python.org/issue?@action=redirect&bpo=33618))

Neither [`SSLSocket`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket) nor [`SSLObject`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLObject) carries a public constructor any longer. Constructing them directly was never a documented or supported capability. To make instances, use the [`SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) methods [`wrap_socket()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.wrap_socket) and [`wrap_bio()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.wrap_bio). (Contributed by Christian Heimes in [bpo-32951](https://bugs.python.org/issue?@action=redirect&bpo=32951))

The OpenSSL 1.1 APIs that set the lowest and highest TLS protocol version are reachable through [`SSLContext.minimum_version`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.minimum_version) and [`SSLContext.maximum_version`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.maximum_version). Which protocols are supported shows up through several new flags, for example [`HAS_TLSv1_1`](https://docs.python.org/3.14/library/ssl.html#ssl.HAS_TLSv1_1). (Contributed by Christian Heimes in [bpo-32609](https://bugs.python.org/issue?@action=redirect&bpo=32609).)

Added [`ssl.SSLContext.post_handshake_auth`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.post_handshake_auth) to turn on, plus [`ssl.SSLSocket.verify_client_post_handshake()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.verify_client_post_handshake) to kick off, TLS 1.3 post-handshake authentication. (Contributed by Christian Heimes in [gh-78851](https://github.com/python/cpython/issues/78851).)

### ssl

The `ssl.wrap_socket()` function is now deprecated. Use [`ssl.SSLContext.wrap_socket()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.wrap_socket) instead. (Contributed by Christian Heimes in [bpo-28124](https://bugs.python.org/issue?@action=redirect&bpo=28124).)

[Subject index](INDEX.md) · [Previous source section](sqlite3.md) · [Next source section](string.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](socket.md) · [Next source section](sunau.md)

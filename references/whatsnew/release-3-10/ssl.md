# What's New In Python 3.10 / ssl - ssl

### ssl

OpenSSL 1.1.1 or newer is now a requirement of the ssl module. (Contributed by Christian Heimes in [**PEP 644**](https://peps.python.org/pep-0644/) and [bpo-43669](https://bugs.python.org/issue?@action=redirect&bpo=43669).)

The ssl module carries early support for OpenSSL 3.0.0 plus a fresh option [`OP_IGNORE_UNEXPECTED_EOF`](https://docs.python.org/3.14/library/ssl.html#ssl.OP_IGNORE_UNEXPECTED_EOF). (Contributed by Christian Heimes in [bpo-38820](https://bugs.python.org/issue?@action=redirect&bpo=38820), [bpo-43794](https://bugs.python.org/issue?@action=redirect&bpo=43794), [bpo-43788](https://bugs.python.org/issue?@action=redirect&bpo=43788), [bpo-43791](https://bugs.python.org/issue?@action=redirect&bpo=43791), [bpo-43799](https://bugs.python.org/issue?@action=redirect&bpo=43799), [bpo-43920](https://bugs.python.org/issue?@action=redirect&bpo=43920), [bpo-43789](https://bugs.python.org/issue?@action=redirect&bpo=43789), and [bpo-43811](https://bugs.python.org/issue?@action=redirect&bpo=43811).)

Calling a deprecated function or relying on deprecated constants now produces a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). [`ssl.SSLContext.options`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.options) ships with [`OP_NO_SSLv2`](https://docs.python.org/3.14/library/ssl.html#ssl.OP_NO_SSLv2) and [`OP_NO_SSLv3`](https://docs.python.org/3.14/library/ssl.html#ssl.OP_NO_SSLv3) already enabled, so it cannot warn when you set the same flag again. A roster of the deprecated features lives in the deprecation section. (Contributed by Christian Heimes in [bpo-43880](https://bugs.python.org/issue?@action=redirect&bpo=43880).)

Default settings in the ssl module are tighter now. Ciphers lacking forward secrecy, along with SHA-1 MAC ciphers, are switched off by default. Security level 2 bans weak RSA, DH, and ECC keys that fall under 112 bits of security. [`SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) now uses a minimum protocol version of TLS 1.2 by default. These choices draw on Hynek Schlawack's research. (Contributed by Christian Heimes in [bpo-43998](https://bugs.python.org/issue?@action=redirect&bpo=43998).)

Official support has been dropped for the deprecated SSL 3.0, TLS 1.0, and TLS 1.1 protocols. Python takes no active steps to block them. That said, the OpenSSL build options, distro configurations, vendor patches, and cipher suites in effect might keep a handshake from succeeding.

Add a *timeout* parameter to the [`ssl.get_server_certificate()`](https://docs.python.org/3.14/library/ssl.html#ssl.get_server_certificate) function. (Contributed by Zackery Spytz in [bpo-31870](https://bugs.python.org/issue?@action=redirect&bpo=31870).)

The ssl module relies on heap-types together with multi-phase initialization. (Contributed by Christian Heimes in [bpo-42333](https://bugs.python.org/issue?@action=redirect&bpo=42333).)

A new verify flag [`VERIFY_X509_PARTIAL_CHAIN`](https://docs.python.org/3.14/library/ssl.html#ssl.VERIFY_X509_PARTIAL_CHAIN) has been added. (Contributed by l0x in [bpo-40849](https://bugs.python.org/issue?@action=redirect&bpo=40849).)

[Subject index](INDEX.md) · [Previous source section](socket.md) · [Next source section](sqlite3.md) · [Release/subject declaration](summary-release-highlights.md)

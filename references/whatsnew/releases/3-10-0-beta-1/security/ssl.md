# Python 3.10.0 beta 1 / security / ssl

[bpo-43998](https://bugs.python.org/issue?@action=redirect&bpo=43998): The [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module now defaults to stronger cipher suites. By default, ciphers lacking forward secrecy or relying on SHA-1 MAC are switched off. Security level 2 rules out weak RSA, DH, and ECC keys that fall below 112 bits of security. [`SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) now picks a minimum protocol version of TLS 1.2. These choices derive from Hynek Schlawack's research.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# What's New In Python 3.2 / ssl — ssl

### ssl

To cover the usual needs of secure (encrypted, authenticated) internet links, the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module gained several capabilities:

- [`SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext), a brand-new class, acts as a holder for long-lived SSL data — protocol settings, certificates, private keys, and assorted other options. Bundled with it is a [`wrap_socket()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.wrap_socket) for turning an SSL context into an SSL socket.

- A new function, `ssl.match_hostname()`, gives higher-level protocols server identity verification by carrying out the HTTPS rules (per [**RFC 2818**](https://datatracker.ietf.org/doc/html/rfc2818.html)), which fit other protocols equally well.

- The [`ssl.wrap_socket()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.wrap_socket) constructor function now accepts a *ciphers* argument. That *ciphers* string enumerates the permitted encryption algorithms in the format spelled out by the [OpenSSL documentation](https://docs.openssl.org/1.0.2/man1/ciphers/#cipher-list-format).

- Built against newer OpenSSL releases, the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module now handles the TLS protocol’s Server Name Indication extension, so several “virtual hosts” can present distinct certificates behind one IP port. Only client mode supports this extension, which you switch on by handing the *server_hostname* argument to [`ssl.SSLContext.wrap_socket()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.wrap_socket).

- Assorted options joined the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module, among them [`OP_NO_SSLv2`](https://docs.python.org/3.14/library/ssl.html#ssl.OP_NO_SSLv2), which turns off the insecure and obsolete SSLv2 protocol.

- Every OpenSSL cipher and digest algorithm is now loaded by the extension. Whenever certain SSL certificates fail verification, they surface as an “unknown algorithm” error.

- You can now read the OpenSSL version in use through the module attributes [`ssl.OPENSSL_VERSION`](https://docs.python.org/3.14/library/ssl.html#ssl.OPENSSL_VERSION) (a string), [`ssl.OPENSSL_VERSION_INFO`](https://docs.python.org/3.14/library/ssl.html#ssl.OPENSSL_VERSION_INFO) (a 5-tuple), and [`ssl.OPENSSL_VERSION_NUMBER`](https://docs.python.org/3.14/library/ssl.html#ssl.OPENSSL_VERSION_NUMBER) (an integer).

(Contributed by Antoine Pitrou in [bpo-8850](https://bugs.python.org/issue?@action=redirect&bpo=8850), [bpo-1589](https://bugs.python.org/issue?@action=redirect&bpo=1589), [bpo-8322](https://bugs.python.org/issue?@action=redirect&bpo=8322), [bpo-5639](https://bugs.python.org/issue?@action=redirect&bpo=5639), [bpo-4870](https://bugs.python.org/issue?@action=redirect&bpo=4870), [bpo-8484](https://bugs.python.org/issue?@action=redirect&bpo=8484), and [bpo-8321](https://bugs.python.org/issue?@action=redirect&bpo=8321).)

[Subject index](INDEX.md) · [Previous source section](socket.md) · [Next source section](nntp.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)

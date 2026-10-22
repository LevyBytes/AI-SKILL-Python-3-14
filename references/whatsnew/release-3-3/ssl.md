# What's New In Python 3.3 / ssl — ssl

### ssl

- The [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module gained a pair of random-generation helpers:

  - [`RAND_bytes()`](https://docs.python.org/3.14/library/ssl.html#ssl.RAND_bytes): generate cryptographically strong pseudo-random bytes.

  - `RAND_pseudo_bytes()`: generate pseudo-random bytes.

Victor Stinner contributed these ? refer to [bpo-12049](https://bugs.python.org/issue?@action=redirect&bpo=12049).

- The [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module now publishes a more granular tree of exceptions, simplifying how you examine each error class. Antoine Pitrou added this; consult [bpo-11183](https://bugs.python.org/issue?@action=redirect&bpo=11183).

- [`load_cert_chain()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.load_cert_chain) henceforth takes a *password* argument, applied whenever the private key sits encrypted. Adam Simpkins delivered this ? refer to [bpo-12803](https://bugs.python.org/issue?@action=redirect&bpo=12803).

- Both ordinary and Elliptic Curve flavors of Diffie-Hellman key exchange now work, surfaced via the [`load_dh_params()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.load_dh_params) plus [`set_ecdh_curve()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.set_ecdh_curve) methods. Antoine Pitrou wrote this ? see [bpo-13626](https://bugs.python.org/issue?@action=redirect&bpo=13626) along with [bpo-13627](https://bugs.python.org/issue?@action=redirect&bpo=13627).

- A new [`get_channel_binding()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.get_channel_binding) method on SSL sockets lets you build authentication schemes like SCRAM-SHA-1-PLUS. Jacek Konieczny added it; refer to [bpo-12551](https://bugs.python.org/issue?@action=redirect&bpo=12551).

- Its fresh [`compression()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.compression) method lets you ask which SSL compression algorithm an SSL socket employs. To switch compression off, reach for the new [`OP_NO_COMPRESSION`](https://docs.python.org/3.14/library/ssl.html#ssl.OP_NO_COMPRESSION) attribute. Antoine Pitrou supplied this ? see [bpo-13634](https://bugs.python.org/issue?@action=redirect&bpo=13634).

- The Next Protocol Negotiation extension is now reachable through the [`ssl.SSLContext.set_npn_protocols()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.set_npn_protocols) method. Colin Marc contributed this; refer to [bpo-14204](https://bugs.python.org/issue?@action=redirect&bpo=14204).

- Examining SSL failures got simpler with the new [`library`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLError.library) plus [`reason`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLError.reason) attributes. Antoine Pitrou landed this ? see [bpo-14837](https://bugs.python.org/issue?@action=redirect&bpo=14837).

- IPv6 is now handled by the [`get_server_certificate()`](https://docs.python.org/3.14/library/ssl.html#ssl.get_server_certificate) function. Charles-François Natali contributed it; refer to [bpo-11811](https://bugs.python.org/issue?@action=redirect&bpo=11811).

- A new [`OP_CIPHER_SERVER_PREFERENCE`](https://docs.python.org/3.14/library/ssl.html#ssl.OP_CIPHER_SERVER_PREFERENCE) attribute tells SSLv3 server sockets to honor the server's preferred cipher order over what the client wants ([bpo-13635](https://bugs.python.org/issue?@action=redirect&bpo=13635)).

[Subject index](INDEX.md) · [Previous source section](sqlite3.md) · [Next source section](stat.md) · [Release/subject declaration](summary-release-highlights.md)

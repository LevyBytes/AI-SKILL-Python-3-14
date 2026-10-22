# ssl: `SSLContext.sni_callback`, `SSLContext.set_servername_callback()`, `SSLContext.load_dh_params()`, `SSLContext.set_ecdh_curve()`, `SSLContext.wrap_socket()`, `SSLContext.sslsocket_class`

SSLContext.sni_callback

Register a callback that fires after the SSL/TLS server has received the TLS Client Hello handshake message, in the case where the TLS client supplies a server name indication. The server name indication mechanism is laid out in [**RFC 6066**](https://datatracker.ietf.org/doc/html/rfc6066.html) section 3 - Server Name Indication.

Each `SSLContext` allows only a single callback. Setting *sni_callback* to `None` turns the callback off. Calling this function again later switches off whatever callback was registered previously.

Three arguments are passed to the callback function: first the `ssl.SSLSocket`, second a string giving the server name the client means to reach (or [`None`](https://docs.python.org/3.14/library/constants.html#None) when the TLS Client Hello carries no server name), and third the original `SSLContext`. The server name argument is text. With an internationalized domain name, the server name comes through as an IDN A-label (`"xn--pythn-mua.org"`).

One common application of this callback is to swap the `SSLSocket.context` attribute of the `ssl.SSLSocket` for a fresh `SSLContext` object holding a certificate chain that lines up with the server name.

Because the TLS connection is still in its early negotiation stage, only a handful of methods and attributes work, such as `SSLSocket.selected_alpn_protocol()` and `SSLSocket.context`. The `SSLSocket.getpeercert()`, `SSLSocket.get_verified_chain()`, `SSLSocket.get_unverified_chain()` `SSLSocket.cipher()` and `SSLSocket.compression()` methods need the TLS connection to have moved past the TLS Client Hello, so they neither yield meaningful values nor can they be invoked safely.

For TLS negotiation to keep going, the *sni_callback* function has to return `None`. Should a TLS failure be wanted, a constant `ALERT_DESCRIPTION_*` may be returned. Returning anything else triggers a TLS fatal error carrying `ALERT_DESCRIPTION_INTERNAL_ERROR`.

Should the *sni_callback* function raise an exception, the TLS connection ends with a fatal TLS alert message of `ALERT_DESCRIPTION_HANDSHAKE_FAILURE`.

When the OpenSSL library was built with OPENSSL_NO_TLSEXT defined, this method raises [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

Added in version 3.7.

 SSLContext.set_servername_callback(*server_name_callback*)

This legacy API is kept around for backwards compatibility. Where you can, favor `sni_callback` instead. The supplied *server_name_callback* works much like *sni_callback*, with the difference that when the server hostname is an IDN-encoded internationalized domain name, the *server_name_callback* gets a decoded U-label (`"pythön.org"`).

Should the server name fail to decode, the TLS connection ends, sending the client a fatal TLS alert message of `ALERT_DESCRIPTION_INTERNAL_ERROR`.

Added in version 3.4.

 SSLContext.load_dh_params(*dhfile*, */*)

Bring in the key generation parameters used for Diffie-Hellman (DH) key exchange. Employing DH key exchange strengthens forward secrecy while costing extra computation (both on the server and on the client). The *dhfile* parameter ought to be the path of a file that holds DH parameters in PEM format.

Client sockets are unaffected by this setting. To tighten security further, you can additionally enable the `OP_SINGLE_DH_USE` option.

Added in version 3.3.

 SSLContext.set_ecdh_curve(*curve_name*, */*)

Choose, by name, the curve to use for Elliptic Curve-based Diffie-Hellman (ECDH) key exchange. ECDH runs markedly faster than ordinary DH while being, by most accounts, equally secure. The *curve_name* parameter ought to be a string naming a well-known elliptic curve, for instance `prime256v1` for a broadly supported curve.

Client sockets are unaffected by this setting. To tighten security further, you can additionally enable the `OP_SINGLE_ECDH_USE` option.

When `HAS_ECDH` is `False`, this method is unavailable.

Added in version 3.3.

See also

[SSL/TLS & Perfect Forward Secrecy](https://vincent.bernat.ch/en/blog/2011-ssl-perfect-forward-secrecy)

Vincent Bernat.

 SSLContext.wrap_socket(*sock*, *server_side=False*, *do_handshake_on_connect=True*, *suppress_ragged_eofs=True*, *server_hostname=None*, *session=None*)

Take an existing Python socket *sock*, wrap it, and return an instance of `SSLContext.sslsocket_class` (default `SSLSocket`). The SSL socket that comes back is bound to the context along with its settings and certificates. *sock* has to be a [`SOCK_STREAM`](https://docs.python.org/3.14/library/socket.html#socket.SOCK_STREAM) socket; no other socket types are supported.

The `server_side` parameter is a boolean indicating whether this socket should behave in a server-side or a client-side fashion.

With client-side sockets, context construction is deferred; should the underlying socket not yet be connected, the context is built after `connect()` runs on the socket. With server-side sockets, when the socket has no remote peer it is taken to be a listening socket, and server-side SSL wrapping happens automatically for client connections that the `accept()` method takes in. This method may raise `SSLError`.

For client connections, the optional *server_hostname* parameter names the hostname of the service being connected to. That makes it possible for one server to serve several SSL-based services each with its own certificate, much the way HTTP virtual hosts work. Supplying *server_hostname* raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when *server_side* is true.

The `do_handshake_on_connect` parameter dictates whether the SSL handshake runs automatically right after a `socket.connect()`, or whether the application program triggers it explicitly by calling the `SSLSocket.do_handshake()` method. Performing `SSLSocket.do_handshake()` explicitly hands the program control over the blocking behavior of the socket I/O that the handshake entails.

The `suppress_ragged_eofs` parameter governs how the `SSLSocket.recv()` method should report an unexpected EOF arriving from the connection's far end. Set to [`True`](https://docs.python.org/3.14/library/constants.html#True) (the default), it answers unexpected EOF errors from the underlying socket with an ordinary EOF (an empty bytes object); set to [`False`](https://docs.python.org/3.14/library/constants.html#False), it propagates the exceptions back to the caller.

*session*, see `session`.

If you need to wrap one `SSLSocket` inside another `SSLSocket`, use `SSLContext.wrap_bio()`.

Changed in version 3.5: A server_hostname may now always be supplied, even where OpenSSL lacks SNI support.

Changed in version 3.6: *session* argument was added.

Changed in version 3.7: Rather than a hard-coded `SSLSocket`, the method now hands back an instance of `SSLContext.sslsocket_class`.

 SSLContext.sslsocket_class

The type returned by `SSLContext.wrap_socket()`, which defaults to `SSLSocket`. You can assign this attribute on `SSLContext` instances to make them return a custom subclass of `SSLSocket`.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](sslcontext-get-ciphers-to-sslcontext-set-npn-protocols.md) · [Continue](sslcontext-wrap-bio-to-sslcontext-num-tickets.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: ssl.SSLContext](ssl-sslcontext-class.md) · [Owning module, declaration or section: SSL contexts](ssl-sslcontext-class.md)

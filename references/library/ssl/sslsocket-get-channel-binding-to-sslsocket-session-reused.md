# ssl: TLS channel binding, negotiated protocols and session state

SSLSocket.get_channel_binding(*cb_type='tls-unique'*)

Fetch channel binding data for the current connection as a bytes object. Returns `None` when there is no connection or the handshake has not finished.

The *cb_type* parameter lets you pick the channel binding type you want. The valid channel binding types appear in the `CHANNEL_BINDING_TYPES` list. At present only the 'tls-unique' channel binding, defined in [**RFC 5929**](https://datatracker.ietf.org/doc/html/rfc5929.html), is supported. [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised when an unsupported channel binding type is asked for.

Added in version 3.3.

 SSLSocket.selected_alpn_protocol()

Hand back the protocol chosen during the TLS handshake. `None` is returned when `SSLContext.set_alpn_protocols()` was not called, when the other party offers no ALPN support, when this socket supports none of the protocols the client proposed, or when the handshake has not yet taken place.

Added in version 3.5.

 SSLSocket.selected_npn_protocol()

Hand back the higher-level protocol chosen during the TLS/SSL handshake. This returns `None` when `SSLContext.set_npn_protocols()` was not called, when the other party offers no NPN support, or when the handshake has not yet taken place.

Added in version 3.3.

Deprecated since version 3.10: NPN has been superseded by ALPN

 SSLSocket.unwrap()

Runs the SSL shutdown handshake, which strips the TLS layer off the underlying socket and gives back the underlying socket object. Use this to move from encrypted operation across a connection back to unencrypted. From then on, conduct any further communication with the other side over the returned socket rather than the original one.

 SSLSocket.verify_client_post_handshake()

Asks a TLS 1.3 client for post-handshake authentication (PHA). PHA can only be started for a TLS 1.3 connection from a server-side socket, once the initial TLS handshake is done and with PHA turned on for both sides; see `SSLContext.post_handshake_auth`.

The method does not carry out a cert exchange right away. The server-side sends a CertificateRequest at the next write event and waits for the client to answer with a certificate at the next read event.

When some precondition is unmet (for example, not TLS 1.3, or PHA not enabled), an `SSLError` is raised.

Note

Available solely when OpenSSL 1.1.1 is present with TLS 1.3 turned on. Absent TLS 1.3 support, [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) is raised by the method.

Added in version 3.8.

 SSLSocket.version()

Hand back the actual SSL protocol version that the connection negotiated as a string, or `None` when no secure connection has been set up. At the time of writing, the return values that may appear include `"SSLv2"`, `"SSLv3"`, `"TLSv1"`, `"TLSv1.1"` and `"TLSv1.2"`. Newer OpenSSL releases may add further return values.

Added in version 3.5.

 SSLSocket.pending()

Gives back how many already decrypted bytes are ready to be read, pending on the connection.

 SSLSocket.context

The `SSLContext` object that this SSL socket is bound to.

Added in version 3.2.

 SSLSocket.server_side

A boolean that is `True` for server-side sockets and `False` for client-side sockets.

Added in version 3.2.

 SSLSocket.server_hostname

Hostname of the server: [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) type, or `None` for a server-side socket or when the hostname went unspecified in the constructor.

Added in version 3.2.

Changed in version 3.7: This attribute now always holds ASCII text. Should `server_hostname` be an internationalized domain name (IDN), the attribute keeps the A-label form (`"xn--pythn-mua.org"`) in place of the U-label form (`"pythön.org"`).

 SSLSocket.session

The `SSLSession` for this SSL connection. The session becomes available on both client and server side sockets once the TLS handshake has finished. On client sockets the session may be set before `do_handshake()` is called so that a session can be reused.

Added in version 3.6.

 SSLSocket.session_reused

Added in version 3.6.

[Subject index](INDEX.md) · [Previous](sslsocket-getpeercert-to-sslsocket-compression.md) · [Continue](ssl-sslcontext-class.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: ssl.SSLSocket](ssl-sslsocket-class-to-shutdown.md) · [Owning module, declaration or section: SSL sockets](ssl-sslsocket-class-to-shutdown.md)

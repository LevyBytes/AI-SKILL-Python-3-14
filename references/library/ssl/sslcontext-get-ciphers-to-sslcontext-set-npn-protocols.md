# ssl: `SSLContext.get_ciphers()`, `SSLContext.set_default_verify_paths()`, `SSLContext.set_ciphers()`, `SSLContext.set_alpn_protocols()`, `SSLContext.set_npn_protocols()`

SSLContext.get_ciphers()

Return a list of the ciphers that are enabled, ordered by cipher priority. Refer to `SSLContext.set_ciphers()`.

Example:

```python
>>> ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
>>> ctx.set_ciphers('ECDHE+AESGCM:!ECDSA')
>>> ctx.get_ciphers()
[{'aead': True,
  'alg_bits': 256,
  'auth': 'auth-rsa',
  'description': 'ECDHE-RSA-AES256-GCM-SHA384 TLSv1.2 Kx=ECDH     Au=RSA  '
                 'Enc=AESGCM(256) Mac=AEAD',
  'digest': None,
  'id': 50380848,
  'kea': 'kx-ecdhe',
  'name': 'ECDHE-RSA-AES256-GCM-SHA384',
  'protocol': 'TLSv1.2',
  'strength_bits': 256,
  'symmetric': 'aes-256-gcm'},
 {'aead': True,
  'alg_bits': 128,
  'auth': 'auth-rsa',
  'description': 'ECDHE-RSA-AES128-GCM-SHA256 TLSv1.2 Kx=ECDH     Au=RSA  '
                 'Enc=AESGCM(128) Mac=AEAD',
  'digest': None,
  'id': 50380847,
  'kea': 'kx-ecdhe',
  'name': 'ECDHE-RSA-AES128-GCM-SHA256',
  'protocol': 'TLSv1.2',
  'strength_bits': 128,
  'symmetric': 'aes-128-gcm'}]

```

Added in version 3.6.

 SSLContext.set_default_verify_paths()

Bring in a collection of default "certification authority" (CA) certificates from a filesystem path that was set when the OpenSSL library was built. Regrettably, there's no simple way to tell whether this method worked: when no certificates turn up, no error comes back. That said, if the OpenSSL library ships as part of the operating system, it's probably set up correctly.

 SSLContext.set_ciphers(*ciphers*, */*)

Set which ciphers are available to sockets that this context creates. The value should be a string in the [OpenSSL cipher list format](https://docs.openssl.org/master/man1/ciphers/). When no cipher can be chosen (because compile-time options or some other configuration rules out every cipher you named), an `SSLError` is raised.

Note

once connected, an SSL socket's `SSLSocket.cipher()` method reports the cipher currently in use.

`set_ciphers()` cannot be used to switch off TLS 1.3 cipher suites.

 SSLContext.set_alpn_protocols(*alpn_protocols*)

Declare which protocols the socket should advertise throughout the SSL/TLS handshake. The value should be a list of ASCII strings, such as `['http/1.1', 'spdy/2']`, arranged by preference. A protocol is chosen during the handshake and follows the procedure of [**RFC 7301**](https://datatracker.ietf.org/doc/html/rfc7301.html). Once the handshake succeeds, the `SSLSocket.selected_alpn_protocol()` method reports the protocol that was agreed upon.

When `HAS_ALPN` is `False`, this method raises [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

Added in version 3.5.

 SSLContext.set_npn_protocols(*npn_protocols*)

Declare which protocols the socket should advertise throughout the SSL/TLS handshake. The value should be a list of strings, such as `['http/1.1', 'spdy/2']`, arranged by preference. A protocol is chosen during the handshake and follows the procedure of [Application Layer Protocol Negotiation](https://en.wikipedia.org/wiki/Application-Layer_Protocol_Negotiation). Once the handshake succeeds, the `SSLSocket.selected_npn_protocol()` method reports the protocol that was agreed upon.

When `HAS_NPN` is `False`, this method raises [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

Added in version 3.3.

Deprecated since version 3.10: NPN has been superseded by ALPN

[Subject index](INDEX.md) · [Previous](sslcontext-cert-store-stats-to-sslcontext-get-ca-certs.md) · [Continue](sslcontext-sni-callback-to-sslcontext-sslsocket-class.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: ssl.SSLContext](ssl-sslcontext-class.md) · [Owning module, declaration or section: SSL contexts](ssl-sslcontext-class.md)

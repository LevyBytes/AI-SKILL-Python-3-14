# ssl: `SSLContext.options`, `SSLContext.post_handshake_auth`, `SSLContext.protocol`, `SSLContext.hostname_checks_common_name`, `SSLContext.security_level`, `SSLContext.verify_flags`, `SSLContext.verify_mode`

SSLContext.options

An integer standing for the collection of SSL options turned on for this context. Its default value is `OP_ALL`, though you can turn on others such as `OP_NO_SSLv2` by ORing them together.

Changed in version 3.6: `SSLContext.options` returns `Options` flags:

```python
>>> ssl.create_default_context().options
<Options.OP_ALL|OP_NO_SSLv3|OP_NO_SSLv2|OP_NO_COMPRESSION: 2197947391>

```

Deprecated since version 3.7: Every `OP_NO_SSL*` along with every `OP_NO_TLS*` option carries deprecated status as of Python 3.7. Reach for `SSLContext.minimum_version` together with `SSLContext.maximum_version` in their place.

 SSLContext.post_handshake_auth

Turn on TLS 1.3 post-handshake client authentication. Post-handshake auth starts out disabled, and a server can only ask for a TLS client certificate while the initial handshake is underway. With it enabled, a server is free to ask for a TLS client certificate at any point following the handshake.

Enabled on client-side sockets, it has the client tell the server that post-handshake authentication is supported.

Enabled on server-side sockets, `SSLContext.verify_mode` likewise has to be set to `CERT_OPTIONAL` or `CERT_REQUIRED`. The real client cert exchange is held off until `SSLSocket.verify_client_post_handshake()` runs and some I/O takes place.

Added in version 3.8.

 SSLContext.protocol

The protocol version that was selected while the context was being constructed. This attribute cannot be written to.

 SSLContext.hostname_checks_common_name

Whether `check_hostname`, lacking a subject alternative name extension, falls back to checking the cert's subject common name (default: true).

Added in version 3.7.

Changed in version 3.10: With OpenSSL prior to version 1.1.1l the flag did nothing. Workarounds for earlier versions are bundled into Python 3.8.9, 3.9.3, and 3.10.

 SSLContext.security_level

An integer standing for the [security level](https://docs.openssl.org/master/man3/SSL_CTX_get_security_level/) of the context. This attribute cannot be written to.

Added in version 3.10.

 SSLContext.verify_flags

The flags governing certificate verification operations. You can turn on flags such as `VERIFY_CRL_CHECK_LEAF` by ORing them together. Out of the box OpenSSL neither requires nor checks certificate revocation lists (CRLs).

Added in version 3.4.

Changed in version 3.6: `SSLContext.verify_flags` returns `VerifyFlags` flags:

```python
>>> ssl.create_default_context().verify_flags
<VerifyFlags.VERIFY_X509_TRUSTED_FIRST: 32768>

```

 SSLContext.verify_mode

Whether the certificates of other peers should be verified, and what to do when verification doesn't succeed. This attribute has to be one of `CERT_NONE`, `CERT_OPTIONAL` or `CERT_REQUIRED`.

Changed in version 3.6: `SSLContext.verify_mode` returns `VerifyMode` enum:

```python
>>> ssl.create_default_context().verify_mode
<VerifyMode.CERT_REQUIRED: 2>

```

[Subject index](INDEX.md) · [Previous](sslcontext-wrap-bio-to-sslcontext-num-tickets.md) · [Continue](sslcontext-set-psk-client-callback.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: ssl.SSLContext](ssl-sslcontext-class.md) · [Owning module, declaration or section: SSL contexts](ssl-sslcontext-class.md)

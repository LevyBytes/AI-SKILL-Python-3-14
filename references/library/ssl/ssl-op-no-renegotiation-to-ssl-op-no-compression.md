# ssl: `ssl.OP_NO_RENEGOTIATION`, `ssl.OP_CIPHER_SERVER_PREFERENCE`, `ssl.OP_SINGLE_DH_USE`, `ssl.OP_SINGLE_ECDH_USE`, `ssl.OP_ENABLE_MIDDLEBOX_COMPAT`, `ssl.OP_NO_COMPRESSION`

Added in version 3.6.3.

Deprecated since version 3.7: As of OpenSSL 1.1.0 the option is deprecated. For backwards compatibility with OpenSSL 1.0.2, it was added to 2.7.15 and 3.6.3.

 ssl.OP_NO_RENEGOTIATION

Turn off every renegotiation in TLSv1.2 and earlier. HelloRequest messages are not sent, and renegotiation requests carried in a ClientHello are ignored.

This option is only available with OpenSSL 1.1.0h and later.

Added in version 3.7.

 ssl.OP_CIPHER_SERVER_PREFERENCE

Apply the cipher ordering preferred by the server instead of the one preferred by the client. On client sockets and SSLv2 server sockets this option does nothing.

Added in version 3.3.

 ssl.OP_SINGLE_DH_USE

Stops the same DH key from being reused across separate SSL sessions. Forward secrecy is improved, though at the cost of additional computation. Only server sockets are affected by this option.

Added in version 3.3.

 ssl.OP_SINGLE_ECDH_USE

Stops the same ECDH key from being reused across separate SSL sessions. Forward secrecy is improved, though at the cost of additional computation. Only server sockets are affected by this option.

Added in version 3.3.

 ssl.OP_ENABLE_MIDDLEBOX_COMPAT

Emit placeholder Change Cipher Spec (CCS) messages during the TLS 1.3 handshake so that a TLS 1.3 connection more closely resembles a TLS 1.2 connection.

This option is only available with OpenSSL 1.1.1 and later.

Added in version 3.8.

 ssl.OP_NO_COMPRESSION

Turn off compression for the SSL channel. This helps when the application protocol provides a compression scheme of its own.

Added in version 3.3.

[Subject index](INDEX.md) · [Continue](ssl-options-class.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: Constants](ssl-cert-none-to-ssl-cert-required.md) · [Owning module, declaration or section: ssl.OP_NO_TLSv1_3](ssl-op-no-tlsv1-to-ssl-op-no-tlsv1-3.md) · [Preceding source contract and version conditions](ssl-op-no-tlsv1-to-ssl-op-no-tlsv1-3.md)

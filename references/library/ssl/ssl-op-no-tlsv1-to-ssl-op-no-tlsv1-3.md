# ssl: `ssl.OP_NO_TLSv1`, `ssl.OP_NO_TLSv1_1`, `ssl.OP_NO_TLSv1_2`, `ssl.OP_NO_TLSv1_3`

ssl.OP_NO_TLSv1

Blocks any TLSv1 connection. This option carries weight only together with `PROTOCOL_TLS`. It stops the peers from settling on TLSv1 as the protocol version.

Added in version 3.2.

Deprecated since version 3.7: From OpenSSL 1.1.0 onward this option counts as deprecated; switch to the newer `SSLContext.minimum_version` and `SSLContext.maximum_version` instead.

 ssl.OP_NO_TLSv1_1

Blocks any TLSv1.1 connection. This option carries weight only together with `PROTOCOL_TLS`. It stops the peers from settling on TLSv1.1 as the protocol version. Only present with openssl version 1.0.1+.

Added in version 3.4.

Deprecated since version 3.7: From OpenSSL 1.1.0 onward this option counts as deprecated.

 ssl.OP_NO_TLSv1_2

Blocks any TLSv1.2 connection. This option carries weight only together with `PROTOCOL_TLS`. It stops the peers from settling on TLSv1.2 as the protocol version. Only present with openssl version 1.0.1+.

Added in version 3.4.

Deprecated since version 3.7: From OpenSSL 1.1.0 onward this option counts as deprecated.

 ssl.OP_NO_TLSv1_3

Blocks any TLSv1.3 connection. This option carries weight only together with `PROTOCOL_TLS`. It stops the peers from settling on TLSv1.3 as the protocol version. TLS 1.3 ships with OpenSSL 1.1.1 or newer. Where Python was built against an OpenSSL older than that, the flag defaults to *0*.

[Subject index](INDEX.md) · [Previous](ssl-protocol-tls-to-ssl-op-no-sslv3.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: Constants](ssl-cert-none-to-ssl-cert-required.md) · [Required continuation of the source contract](ssl-op-no-renegotiation-to-ssl-op-no-compression.md)

# ssl: TLS protocol selection and legacy-protocol disabling

ssl.PROTOCOL_TLS

Picks the highest protocol version supported by both the server and the client. The name notwithstanding, this option can land on either an “SSL” or a “TLS” protocol.

Added in version 3.6.

Deprecated since version 3.10: Secure communication calls for distinct defaults on the client side versus the server side. As a result, the generic TLS protocol constant is now deprecated, with `PROTOCOL_TLS_CLIENT` and `PROTOCOL_TLS_SERVER` taking its place.

 ssl.PROTOCOL_TLS_CLIENT

Settle automatically on the topmost protocol version shared by client and server, and set the context up for client-side connections. By default the protocol switches on `CERT_REQUIRED` and `check_hostname`.

Added in version 3.6.

 ssl.PROTOCOL_TLS_SERVER

Settle automatically on the topmost protocol version shared by client and server, and set the context up for server-side connections.

Added in version 3.6.

 ssl.PROTOCOL_SSLv23

Alias for `PROTOCOL_TLS`.

Deprecated since version 3.6: Use `PROTOCOL_TLS` instead.

 ssl.PROTOCOL_SSLv3

Picks SSL version 3 to serve as the channel encryption protocol.

When OpenSSL has been built with the `no-ssl3` option, this protocol won't be present.

Warning

SSL version 3 is insecure. Its use is highly discouraged.

Deprecated since version 3.6: Every version-specific protocol has been deprecated by OpenSSL. Instead, reach for the default protocol `PROTOCOL_TLS_SERVER` or `PROTOCOL_TLS_CLIENT` together with `SSLContext.minimum_version` and `SSLContext.maximum_version`.

 ssl.PROTOCOL_TLSv1

Picks TLS version 1.0 to serve as the channel encryption protocol.

Deprecated since version 3.6: OpenSSL has marked every version-specific protocol as deprecated.

 ssl.PROTOCOL_TLSv1_1

Picks TLS version 1.1 to serve as the channel encryption protocol. Only present with openssl version 1.0.1+.

Added in version 3.4.

Deprecated since version 3.6: OpenSSL has marked every version-specific protocol as deprecated.

 ssl.PROTOCOL_TLSv1_2

Picks TLS version 1.2 to serve as the channel encryption protocol. Only present with openssl version 1.0.1+.

Added in version 3.4.

Deprecated since version 3.6: OpenSSL has marked every version-specific protocol as deprecated.

 ssl.OP_ALL

Switches on workarounds for assorted bugs found in other SSL implementations. By default this option is enabled. It won't necessarily set the identical flags that OpenSSL's `SSL_OP_ALL` constant does.

Added in version 3.2.

 ssl.OP_NO_SSLv2

Blocks any SSLv2 connection. This option carries weight only together with `PROTOCOL_TLS`. It stops the peers from settling on SSLv2 as the protocol version.

Added in version 3.2.

Deprecated since version 3.6: SSLv2 is deprecated

 ssl.OP_NO_SSLv3

Blocks any SSLv3 connection. This option carries weight only together with `PROTOCOL_TLS`. It stops the peers from settling on SSLv3 as the protocol version.

Added in version 3.2.

Deprecated since version 3.6: SSLv3 is deprecated

[Subject index](INDEX.md) · [Previous](ssl-verifyflags-class.md) · [Continue](ssl-op-no-tlsv1-to-ssl-op-no-tlsv1-3.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: Constants](ssl-cert-none-to-ssl-cert-required.md)

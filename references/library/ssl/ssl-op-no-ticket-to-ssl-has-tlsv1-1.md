# ssl: TLS ticket, compatibility and protocol-support flags

ssl.OP_NO_TICKET

Stop the client side from asking for a session ticket.

Added in version 3.6.

 ssl.OP_IGNORE_UNEXPECTED_EOF

Disregard an unexpected shutdown of TLS connections.

This option is only available with OpenSSL 3.0.0 and later.

Added in version 3.10.

 ssl.OP_ENABLE_KTLS

Turn on use of the kernel TLS. For the feature to apply, OpenSSL must have been built with support for it, and the kernel must support the negotiated cipher suites and extensions (which supported ones exist may differ across platforms and kernel versions).

Be aware that when kernel TLS is enabled, certain cryptographic operations run inside the kernel directly rather than through any available OpenSSL Providers. That can be a problem when, for instance, an application demands that every cryptographic operation go through the FIPS provider.

This option is only available with OpenSSL 3.0.0 and later.

Added in version 3.12.

 ssl.OP_LEGACY_SERVER_CONNECT

Permit legacy insecure renegotiation strictly between OpenSSL and servers that have not been patched.

Added in version 3.12.

 ssl.HAS_ALPN

Indicates whether the OpenSSL library ships with native support for the *Application-Layer Protocol Negotiation* TLS extension described in [**RFC 7301**](https://datatracker.ietf.org/doc/html/rfc7301.html).

Added in version 3.5.

 ssl.HAS_NEVER_CHECK_COMMON_NAME

Indicates whether the OpenSSL library ships with native support for skipping the subject common name check and whether `SSLContext.hostname_checks_common_name` can be written to.

Added in version 3.7.

 ssl.HAS_ECDH

Indicates whether the OpenSSL library ships with native support for the Elliptic Curve-based Diffie-Hellman key exchange. Unless the distributor turned the feature off on purpose, this should be true.

Added in version 3.3.

 ssl.HAS_SNI

Indicates whether the OpenSSL library ships with native support for the *Server Name Indication* extension (as defined in [**RFC 6066**](https://datatracker.ietf.org/doc/html/rfc6066.html)).

Added in version 3.2.

 ssl.HAS_NPN

Indicates whether the OpenSSL library ships with native support for the *Next Protocol Negotiation* described in the [Application Layer Protocol Negotiation](https://en.wikipedia.org/wiki/Application-Layer_Protocol_Negotiation). When this is true, the `SSLContext.set_npn_protocols()` method lets you advertise the protocols you intend to support.

Added in version 3.3.

 ssl.HAS_SSLv2

Indicates whether the OpenSSL library ships with native support for the SSL 2.0 protocol.

Added in version 3.7.

 ssl.HAS_SSLv3

Indicates whether the OpenSSL library ships with native support for the SSL 3.0 protocol.

Added in version 3.7.

 ssl.HAS_TLSv1

Indicates whether the OpenSSL library ships with native support for the TLS 1.0 protocol.

Added in version 3.7.

 ssl.HAS_TLSv1_1

Indicates whether the OpenSSL library ships with native support for the TLS 1.1 protocol.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](ssl-options-class.md) · [Continue](ssl-has-tlsv1-2-to-ssl-alert-description-internal-error.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: Constants](ssl-cert-none-to-ssl-cert-required.md)

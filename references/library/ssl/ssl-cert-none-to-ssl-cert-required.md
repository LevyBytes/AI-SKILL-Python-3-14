# ssl: `ssl.CERT_NONE`, `ssl.CERT_OPTIONAL`, `ssl.CERT_REQUIRED`

### Constants

>

All constants are now [`enum.IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum) or [`enum.IntFlag`](https://docs.python.org/3.14/library/enum.html#enum.IntFlag) collections.

Added in version 3.6.

 ssl.CERT_NONE

A possible setting for `SSLContext.verify_mode`. Save for `PROTOCOL_TLS_CLIENT`, this is what's used by default. On client-side sockets, practically any cert passes. Problems found during validation — say an expired or untrusted cert — go ignored and won't halt the TLS/SSL handshake.

Under server mode, the client is never asked for a certificate, and therefore supplies none toward client cert authentication.

See the discussion of Security considerations below.

 ssl.CERT_OPTIONAL

A possible setting for `SSLContext.verify_mode`. When used in client mode, `CERT_OPTIONAL` works just the same as `CERT_REQUIRED`. For client-side sockets, reaching for `CERT_REQUIRED` instead is the advised choice.

When in server mode, the client receives a request for its certificate. The client is free to disregard that request, or to send a certificate so as to carry out TLS client cert authentication. Whenever the client does send a certificate, it gets verified. Any failure during verification immediately tears down the TLS handshake.

To use this setting, you must hand a valid collection of CA certificates over to `SSLContext.load_verify_locations()`.

 ssl.CERT_REQUIRED

A possible setting for `SSLContext.verify_mode`. Under this mode, the opposite end of the socket connection has to present a certificate; absent one, or with one that fails validation, a `SSLError` is thrown. On its own this mode does **not** suffice to verify a certificate in client mode, since it performs no hostname matching. You also have to switch on `check_hostname` to confirm a cert is genuine. `PROTOCOL_TLS_CLIENT` switches on `CERT_REQUIRED` along with `check_hostname` by default.

On a server socket, this mode makes TLS client cert authentication mandatory. The client is sent a certificate request and is obliged to supply a certificate that is both valid and trusted.

To use this setting, you must hand a valid collection of CA certificates over to `SSLContext.load_verify_locations()`.

[Subject index](INDEX.md) · [Previous](ssl-enum-certificates-to-ssl-enum-crls.md) · [Continue](ssl-verifymode-class.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md)

# ssl: `SSLContext.set_psk_client_callback()`

SSLContext.set_psk_client_callback(*callback*)

Turn on TLS-PSK (pre-shared key) authentication for a client-side connection.

As a rule, certificate based authentication ought to be favored over this method.

The `callback` parameter is a callable object whose signature is: `def callback(hint: str | None) -> tuple[str | None, bytes]`. The `hint` parameter is an optional identity hint the server has sent. The return value is a tuple of the form (client-identity, psk). Client-identity is an optional string the server may use to pick a matching PSK for the client. Once UTF-8 encoded, the string has to be no longer than `256` octets. PSK is a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) holding the pre-shared key. Hand back a zero length PSK to turn down the connection.

Any existing callback is removed by setting `callback` to [`None`](https://docs.python.org/3.14/library/constants.html#None).

Note

When using TLS 1.3:

- the `hint` parameter is always [`None`](https://docs.python.org/3.14/library/constants.html#None).

- client-identity must be a non-empty string.

Example usage:

[Subject index](INDEX.md) · [Previous](sslcontext-options-to-sslcontext-verify-mode.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: ssl.SSLContext](ssl-sslcontext-class.md) · [Owning module, declaration or section: SSL contexts](ssl-sslcontext-class.md) · [Required continuation of the source contract](sslcontext-set-psk-server-callback.md)

# ssl: `SSLContext.set_psk_server_callback()`

```python
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
context.maximum_version = ssl.TLSVersion.TLSv1_2
context.set_ciphers('PSK')

# A simple lambda:
psk = bytes.fromhex('c0ffee')
context.set_psk_client_callback(lambda hint: (None, psk))

# A table using the hint from the server:
psk_table = { 'ServerId_1': bytes.fromhex('c0ffee'),
              'ServerId_2': bytes.fromhex('facade')
}
def callback(hint):
    return 'ClientId_1', psk_table.get(hint, b'')
context.set_psk_client_callback(callback)

```

When `HAS_PSK` evaluates to `False`, this method raises [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

Added in version 3.13.

 SSLContext.set_psk_server_callback(*callback*, *identity_hint=None*)

Turns on TLS-PSK (pre-shared key) authentication for a connection operating in server mode.

As a rule, you should favor certificate based authentication ahead of this approach.

The `callback` argument is a callable carrying the signature `def callback(identity: str | None) -> bytes`. Here, the `identity` parameter is an optional identity supplied by the client, which you can use to pick the matching PSK. What gets returned is a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) standing for the pre-shared key. To turn down the connection, return a PSK of zero length.

Assigning [`None`](https://docs.python.org/3.14/library/constants.html#None) to `callback` clears whatever callback was set previously.

The `identity_hint` argument is an optional identity hint string dispatched to the client. Once UTF-8 encoded, that string has to be no longer than `256` octets.

Note

The `identity_hint` parameter is not delivered to the client whenever TLS 1.3 is in use.

Example usage:

```python
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.maximum_version = ssl.TLSVersion.TLSv1_2
context.set_ciphers('PSK')

# A simple lambda:
psk = bytes.fromhex('c0ffee')
context.set_psk_server_callback(lambda identity: psk)

# A table using the identity of the client:
psk_table = { 'ClientId_1': bytes.fromhex('c0ffee'),
              'ClientId_2': bytes.fromhex('facade')
}
def callback(identity):
    return psk_table.get(identity, b'')
context.set_psk_server_callback(callback, 'ServerId_1')

```

When `HAS_PSK` evaluates to `False`, this method raises [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

Added in version 3.13.

[Subject index](INDEX.md) · [Continue](certificates.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: ssl.SSLContext](ssl-sslcontext-class.md) · [Owning module, declaration or section: SSL contexts](ssl-sslcontext-class.md) · [Owning module, declaration or section: SSLContext.set_psk_client_callback](sslcontext-set-psk-client-callback.md) · [Preceding source contract and version conditions](sslcontext-set-psk-client-callback.md)

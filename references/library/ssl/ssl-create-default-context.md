# ssl - Context creation

### Context creation

To build `SSLContext` objects suited to typical scenarios, a convenience function is provided.

 ssl.create_default_context(*purpose=Purpose.SERVER_AUTH*, ***, *cafile=None*, *capath=None*, *cadata=None*)

Hand back a fresh `SSLContext` object carrying defaults appropriate to the supplied *purpose*. The `ssl` module picks these defaults, which typically aim higher on security than you'd get by invoking the `SSLContext` constructor on your own.

The trio *cafile*, *capath*, *cadata* stand for optional CA certificates trusted during certificate verification, mirroring `SSLContext.load_verify_locations()`. Should every one of the three be [`None`](https://docs.python.org/3.14/library/constants.html#None), the function is free to fall back on the system's default CA certificates instead.

Here is what gets configured: `PROTOCOL_TLS_CLIENT` or `PROTOCOL_TLS_SERVER`, alongside `OP_NO_SSLv2` and `OP_NO_SSLv3`, plus strong cipher suites that exclude both RC4 and any unauthenticated suites. Supplying `SERVER_AUTH` for *purpose* switches `verify_mode` to `CERT_REQUIRED` and then either pulls in CA certificates (whenever *cafile*, *capath* or *cadata* supplies at least one) or falls back on `SSLContext.load_default_certs()` to bring in the default CA certificates.

Where `keylog_filename` is available and the `SSLKEYLOGFILE` environment variable has been set, `create_default_context()` switches on key logging.

Among this context's defaults you'll find `VERIFY_X509_PARTIAL_CHAIN` together with `VERIFY_X509_STRICT`. Their effect is to push the underlying OpenSSL implementation closer to a standards-conforming implementation of [**RFC 5280**](https://datatracker.ietf.org/doc/html/rfc5280.html), at the price of slightly reduced tolerance for older X.509 certificates.

Note

Without any advance deprecation, the cipher, options, protocol, and remaining settings can tighten toward stricter values at any time. The chosen values strike a reasonable middle ground between security and compatibility.

Should your program demand particular settings, build a `SSLContext` and configure those settings on your own.

Note

If older clients or servers, on attempting to talk to a `SSLContext` produced by this function, report an error reading “Protocol or cipher suite mismatch”, the likely cause is that those peers handle nothing beyond SSL3.0 — which this function rules out by way of `OP_NO_SSLv3`. SSL3.0 is broadly regarded as [completely broken](https://en.wikipedia.org/wiki/POODLE). To keep relying on this function and yet permit SSL 3.0 connections again, you can switch them back on with:

```python
ctx = ssl.create_default_context(Purpose.CLIENT_AUTH)
ctx.options &= ~ssl.OP_NO_SSLv3

```

Note

By default this context turns on `VERIFY_X509_STRICT`, and that may turn away malformed or pre-[**RFC 5280**](https://datatracker.ietf.org/doc/html/rfc5280.html) certificates the underlying OpenSSL implementation would otherwise accept. Turning it off is discouraged, but it can be done with:

```python
ctx = ssl.create_default_context()
ctx.verify_flags &= ~ssl.VERIFY_X509_STRICT

```

Added in version 3.4.

Changed in version 3.4.4: The default cipher string no longer carries RC4.

Changed in version 3.6: ChaCha20/Poly1305 joined the default cipher string.

3DES left the default cipher string.

Changed in version 3.8: Logging keys to `SSLKEYLOGFILE` gained support.

Changed in version 3.10: Rather than the generic `PROTOCOL_TLS`, the context now relies on the `PROTOCOL_TLS_CLIENT` or `PROTOCOL_TLS_SERVER` protocol.

Changed in version 3.13: Among the context's default verify flags are now `VERIFY_X509_PARTIAL_CHAIN` and `VERIFY_X509_STRICT`.

[Subject index](INDEX.md) · [Previous](socket-creation.md) · [Continue](ssl-sslerror-to-ssl-certificateerror.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md)

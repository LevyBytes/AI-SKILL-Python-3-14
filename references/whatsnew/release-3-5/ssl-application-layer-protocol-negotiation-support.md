# What’s New In Python 3.5 / ssl / Application-Layer Protocol Negotiation Support - ssl

#### Application-Layer Protocol Negotiation Support

Benjamin Peterson contributed this (see [bpo-20188](https://bugs.python.org/issue?@action=redirect&bpo=20188)).

Wherever OpenSSL support exists, the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module now provides the *Application-Layer Protocol Negotiation* TLS extension laid out in [**RFC 7301**](https://datatracker.ietf.org/doc/html/rfc7301.html).

To declare which protocols a socket ought to offer over the course of the TLS handshake, you can use the new [`SSLContext.set_alpn_protocols()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.set_alpn_protocols).

Whatever protocol got picked during the TLS handshake is reported by the new [`SSLSocket.selected_alpn_protocol()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.selected_alpn_protocol). Whether ALPN support exists is signaled by the [`HAS_ALPN`](https://docs.python.org/3.14/library/ssl.html#ssl.HAS_ALPN) flag.

[Subject index](INDEX.md) · [Previous source section](ssl-memory-bio-support.md) · [Next source section](ssl-other-changes.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](ssl-memory-bio-support.md)

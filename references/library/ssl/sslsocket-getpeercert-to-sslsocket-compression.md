# ssl: `SSLSocket.getpeercert()`, `SSLSocket.get_verified_chain()`, `SSLSocket.get_unverified_chain()`, `SSLSocket.cipher()`, `SSLSocket.shared_ciphers()`, `SSLSocket.compression()`

SSLSocket.getpeercert(*binary_form=False*)

When the peer at the far end of the connection has no certificate, return `None`. When the SSL handshake has not run yet, raise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

When the `binary_form` parameter is [`False`](https://docs.python.org/3.14/library/constants.html#False) and a certificate came back from the peer, this method gives you a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) instance. The dict is empty when the certificate went unvalidated. When the certificate was validated, you get a dict carrying several keys, among them `subject` (the principal the certificate was issued to) and `issuer` (the principal that issued the certificate). When a certificate carries an instance of the *Subject Alternative Name* extension (see [**RFC 3280**](https://datatracker.ietf.org/doc/html/rfc3280.html)), a `subjectAltName` key shows up in the dictionary too.

The `subject` and `issuer` fields are tuples that hold the series of relative distinguished names (RDNs) listed in the certificate's data structure for each respective field, and every RDN is itself a series of name-value pairs. Below is a real-world example:

```python
{'issuer': ((('countryName', 'IL'),),
            (('organizationName', 'StartCom Ltd.'),),
            (('organizationalUnitName',
              'Secure Digital Certificate Signing'),),
            (('commonName',
              'StartCom Class 2 Primary Intermediate Server CA'),)),
 'notAfter': 'Nov 22 08:15:19 2013 GMT',
 'notBefore': 'Nov 21 03:09:52 2011 GMT',
 'serialNumber': '95F0',
 'subject': ((('description', '571208-SLe257oHY9fVQ07Z'),),
             (('countryName', 'US'),),
             (('stateOrProvinceName', 'California'),),
             (('localityName', 'San Francisco'),),
             (('organizationName', 'Electronic Frontier Foundation, Inc.'),),
             (('commonName', '*.eff.org'),),
             (('emailAddress', 'hostmaster@eff.org'),)),
 'subjectAltName': (('DNS', '*.eff.org'), ('DNS', 'eff.org')),
 'version': 3}

```

When the `binary_form` parameter is [`True`](https://docs.python.org/3.14/library/constants.html#True) and a certificate was supplied, this method hands back the DER-encoded form of the whole certificate as a byte sequence, or [`None`](https://docs.python.org/3.14/library/constants.html#None) when the peer supplied none. The SSL socket's role governs whether the peer supplies a certificate at all:

- with a client SSL socket, the server always supplies a certificate, no matter whether validation was demanded;

- with a server SSL socket, the client supplies a certificate only when the server asks for one; consequently `getpeercert()` hands back [`None`](https://docs.python.org/3.14/library/constants.html#None) when you relied on `CERT_NONE` (as opposed to `CERT_OPTIONAL` or `CERT_REQUIRED`).

See also `SSLContext.check_hostname`.

Changed in version 3.2: Extra items such as `issuer` and `notBefore` now appear in the returned dictionary.

Changed in version 3.4: When the handshake has not completed, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. Further X509v3 extension items such as `crlDistributionPoints`, `caIssuers` and `OCSP` URIs now appear in the returned dictionary.

Changed in version 3.9: A trailing new line no longer appears on IPv6 address strings.

 SSLSocket.get_verified_chain()

Gives back the verified certificate chain supplied by the far end of the SSL channel as a list of DER-encoded bytes. When certificate verification was turned off, the method behaves identically to `get_unverified_chain()`.

Added in version 3.13.

 SSLSocket.get_unverified_chain()

Gives back the raw certificate chain supplied by the far end of the SSL channel as a list of DER-encoded bytes.

Added in version 3.13.

 SSLSocket.cipher()

Gives back a three-value tuple holding the name of the cipher in use, the version of the SSL protocol that governs its use, and how many secret bits are in use. When no connection has been set up, returns `None`.

 SSLSocket.shared_ciphers()

Hand back the list of ciphers that both the client and server have available. Every item in the returned list is a three-value tuple holding the cipher's name, the version of the SSL protocol that governs its use, and how many secret bits the cipher uses. `shared_ciphers()` returns `None` when no connection has been set up or when the socket is a client socket.

Added in version 3.5.

 SSLSocket.compression()

Hand back the compression algorithm in use as a string, or `None` when the connection is not compressed.

When the higher-level protocol provides a compression mechanism of its own, you may turn off SSL-level compression with `OP_NO_COMPRESSION`.

Added in version 3.3.

[Subject index](INDEX.md) · [Previous](sslsocket-read-to-sslsocket-do-handshake.md) · [Continue](sslsocket-get-channel-binding-to-sslsocket-session-reused.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: ssl.SSLSocket](ssl-sslsocket-class-to-shutdown.md) · [Owning module, declaration or section: SSL sockets](ssl-sslsocket-class-to-shutdown.md)

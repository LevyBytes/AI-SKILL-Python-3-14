# ssl multiprocessing, TLS 1.3 and platform limitations

### Multi-processing

Should you employ this module inside a multi-processed application (by way of, say, the [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) or [`concurrent.futures`](https://docs.python.org/3.14/library/concurrent.futures.html#module-concurrent.futures) modules), keep in mind that the internal random number generator within OpenSSL copes poorly with forked processes. Any application invoking an SSL feature alongside [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork) is obliged to alter the parent process's PRNG state. A single successful `RAND_add()` or `RAND_bytes()` call does the trick.

### TLS 1.3

Added in version 3.7.

In its behavior, the TLS 1.3 protocol diverges a little from earlier TLS/SSL versions. A number of the fresh TLS 1.3 capabilities have yet to be made available.

- A separate, non-overlapping collection of cipher suites is what TLS 1.3 draws on. Every AES-GCM and ChaCha20 cipher suite is on by default. As yet, the `SSLContext.set_ciphers()` method has no power to switch any TLS 1.3 ciphers on or off, although `SSLContext.get_ciphers()` will still report them.

- The initial handshake no longer carries session tickets, and their treatment has changed. Neither `SSLSocket.session` nor `SSLSession` works with TLS 1.3.

- Verification of client-side certificates likewise no longer occurs within the initial handshake. At any moment a server may ask for a certificate, and clients deal with such requests in the midst of sending or receiving application data to or from the server.

- Several TLS 1.3 features — among them early data, the deferred TLS client cert request, signature algorithm configuration, and rekeying — remain unsupported for now.

See also

Class [`socket.socket`](https://docs.python.org/3.14/library/socket.html#socket.socket)

Reference for the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) class that underlies it

[SSL/TLS Strong Encryption: An Introduction](https://httpd.apache.org/docs/trunk/en/ssl/ssl_intro.html)

An introduction drawn from the Apache HTTP Server documentation

[**RFC 1422: Privacy Enhancement for Internet Electronic Mail: Part II: Certificate-Based Key Management**](https://datatracker.ietf.org/doc/html/rfc1422.html)

Steve Kent

[**RFC 4086: Randomness Requirements for Security**](https://datatracker.ietf.org/doc/html/rfc4086.html)

Donald E. Eastlake, Jeffrey I. Schiller, Steve Crocker

[**RFC 5280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile**](https://datatracker.ietf.org/doc/html/rfc5280.html)

David Cooper et al.

[**RFC 5246: The Transport Layer Security (TLS) Protocol Version 1.2**](https://datatracker.ietf.org/doc/html/rfc5246.html)

Tim Dierks and Eric Rescorla.

[**RFC 6066: Transport Layer Security (TLS) Extensions**](https://datatracker.ietf.org/doc/html/rfc6066.html)

Donald E. Eastlake

[IANA TLS: Transport Layer Security (TLS) Parameters](https://www.iana.org/assignments/tls-parameters/tls-parameters.xml)

IANA

[**RFC 7525: Recommendations for Secure Use of Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)**](https://datatracker.ietf.org/doc/html/rfc7525.html)

IETF

[Mozilla’s Server Side TLS recommendations](https://wiki.mozilla.org/Security/Server_Side_TLS)

Mozilla

[Subject index](INDEX.md) · [Previous](ssl-manual-certificate-protocol-and-cipher-settings.md) · [Owning section heading](ssl-manual-certificate-protocol-and-cipher-settings.md)

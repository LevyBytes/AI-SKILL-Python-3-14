# ssl — Certificates

### Certificates

Broadly, certificates belong to a public-key / private-key scheme. Within that scheme, every *principal* (be it a machine, a person, or an organization) receives a distinct key made of two parts. The first part is published and is termed the *public key*; the second is held in confidence and is termed the *private key*. These two parts are connected such that a message you encrypt with one part can be decrypted using the other part, and **only** with the other part.

A certificate carries details about two principals. It holds a *subject*'s name together with that subject's public key. Beyond that, it carries an assertion from a second principal, the *issuer*, attesting that the subject really is who they say they are and that this truly is the subject's public key. The issuer signs that assertion with the issuer's private key, a secret known to the issuer alone. Even so, anyone is able to check the issuer's assertion by locating the issuer's public key, using it to decrypt the assertion, and matching the result against the rest of the certificate's contents. Each certificate likewise records the span of time during which it stays valid. Two fields capture this span, named "notBefore" and "notAfter".

Within Python's handling of certificates, either a client or a server may present a certificate to attest to its identity. The opposite end of a network connection can likewise be obligated to supply a certificate, and that certificate may be checked to whatever degree satisfies the client or server demanding such a check. You can configure the connection attempt so it throws an exception whenever the check does not pass. The underlying OpenSSL framework performs validation on its own; the application has no need to worry about how that works internally. That said, the application typically still has to furnish collections of certificates so the procedure can run.

Python keeps certificates inside files. The expected layout is "PEM" (refer to [**RFC 1422**](https://datatracker.ietf.org/doc/html/rfc1422.html)), a base-64 encoded representation enclosed by a header line and a footer line:

```python
-----BEGIN CERTIFICATE-----
... (certificate in base64 PEM encoding) ...
-----END CERTIFICATE-----

```

[Subject index](INDEX.md) · [Previous](sslcontext-set-psk-server-callback.md) · [Continue](certificate-chains.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md)

# ssl — Certificate chains

### Certificate chains

A Python file holding certificates may hold a series of them, occasionally referred to as a *certificate chain*. Such a chain ought to begin with the particular certificate for the principal who "is" the client or server, followed by the certificate of that certificate's issuer, then the certificate of *that* issuer, continuing upward through the chain until you arrive at a certificate that is *self-signed* — one whose subject and issuer coincide, occasionally referred to as a *root certificate*. You simply concatenate the certificates one after another in the certificate file. As an illustration, imagine we possessed a chain of three certificates, beginning at our own server certificate, proceeding to the certificate belonging to the certification authority that put its signature on it, and reaching the root certificate of the agency that issued the certification authority's certificate:

```python
-----BEGIN CERTIFICATE-----
... (certificate for your server)...
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
... (the certificate for the CA)...
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
... (the root certificate for the CA's issuer)...
-----END CERTIFICATE-----

```

[Subject index](INDEX.md) · [Previous](certificates.md) · [Continue](ca-certificates.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md)

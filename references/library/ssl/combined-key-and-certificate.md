# ssl — Combined key and certificate

### Combined key and certificate

Frequently the private key resides in the very same file as the certificate; under those circumstances, you need only pass the `certfile` parameter to `SSLContext.load_cert_chain()`. Where the private key is kept alongside the certificate, it ought to appear ahead of the first certificate in the certificate chain:

```python
-----BEGIN RSA PRIVATE KEY-----
... (private key in base64 encoding) ...
-----END RSA PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
... (certificate in base64 PEM encoding) ...
-----END CERTIFICATE-----

```

[Subject index](INDEX.md) · [Previous](ca-certificates.md) · [Continue](self-signed-certificates.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md)

# ssl: `ssl.enum_certificates()`, `ssl.enum_crls()`

ssl.enum_certificates(*store_name*)

Pull certificates out of Windows' system cert store. The *store_name* argument may take one of `CA`, `ROOT` or `MY`. Windows can expose extra cert stores as well.

Back comes a list of (cert_bytes, encoding_type, trust) tuples. Here encoding_type reports the cert_bytes encoding — `x509_asn` when the payload is X.509 ASN.1, or `pkcs_7_asn` when it is PKCS#7 ASN.1. The trust field conveys what the certificate may be used for, given as a set of OIDS, or simply `True` if the certificate is trusted across all purposes.

Example:

```python
>>> ssl.enum_certificates("CA")
[(b'data...', 'x509_asn', {'1.3.6.1.5.5.7.3.1', '1.3.6.1.5.5.7.3.2'}),
 (b'data...', 'x509_asn', True)]

```

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Added in version 3.4.

 ssl.enum_crls(*store_name*)

Pull CRLs out of Windows' system cert store. The *store_name* argument may take one of `CA`, `ROOT` or `MY`. Windows can expose extra cert stores as well.

Back comes a list of (cert_bytes, encoding_type, trust) tuples. Here encoding_type reports the cert_bytes encoding — `x509_asn` when the payload is X.509 ASN.1, or `pkcs_7_asn` when it is PKCS#7 ASN.1.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](ssl-cert-time-to-seconds-to-ssl-get-default-verify-paths.md) · [Continue](ssl-cert-none-to-ssl-cert-required.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: Certificate handling](ssl-cert-time-to-seconds-to-ssl-get-default-verify-paths.md)

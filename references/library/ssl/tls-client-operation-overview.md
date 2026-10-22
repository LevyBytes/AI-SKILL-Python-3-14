# ssl — Client-side operation — Section introduction and initial examples

### Client-side operation

The following example builds an SSL context configured with the advised security defaults for client sockets, which includes verifying certificates automatically:

```python
>>> context = ssl.create_default_context()

```

Should you rather adjust the security settings on your own, you can construct a context from the ground up (though take care, since getting every setting correct is not guaranteed):

```python
>>> context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
>>> context.load_verify_locations("/etc/ssl/certs/ca-bundle.crt")

```

(this snippet takes for granted that your operating system keeps a bundle of every CA certificate at `/etc/ssl/certs/ca-bundle.crt`; otherwise you will receive an error and need to correct the path)

The `PROTOCOL_TLS_CLIENT` protocol sets up the context for certificate validation along with hostname verification. It puts `verify_mode` at `CERT_REQUIRED` and turns `check_hostname` to `True`. Every other protocol builds SSL contexts whose defaults are insecure.

As you use the context to reach a server, `CERT_REQUIRED` together with `check_hostname` validate the server certificate: this confirms that one of the CA certificates signed the server certificate, verifies that the signature is correct, and checks further properties such as the validity and the identity of the hostname:

```python
>>> conn = context.wrap_socket(socket.socket(socket.AF_INET),
...                            server_hostname="www.python.org")
>>> conn.connect(("www.python.org", 443))

```

At that point you can retrieve the certificate:

```python
>>> cert = conn.getpeercert()

```

Looking it over by eye confirms the certificate does point to the intended service (namely the HTTPS host `www.python.org`):

```python
>>> pprint.pprint(cert)
{'OCSP': ('http://ocsp.digicert.com',),
 'caIssuers': ('http://cacerts.digicert.com/DigiCertSHA2ExtendedValidationServerCA.crt',),
 'crlDistributionPoints': ('http://crl3.digicert.com/sha2-ev-server-g1.crl',
                           'http://crl4.digicert.com/sha2-ev-server-g1.crl'),
 'issuer': ((('countryName', 'US'),),
            (('organizationName', 'DigiCert Inc'),),
            (('organizationalUnitName', 'www.digicert.com'),),
            (('commonName', 'DigiCert SHA2 Extended Validation Server CA'),)),
 'notAfter': 'Sep  9 12:00:00 2016 GMT',
 'notBefore': 'Sep  5 00:00:00 2014 GMT',
 'serialNumber': '01BB6F00122B177F36CAB49CEA8B6B26',
 'subject': ((('businessCategory', 'Private Organization'),),
             (('1.3.6.1.4.1.311.60.2.1.3', 'US'),),
             (('1.3.6.1.4.1.311.60.2.1.2', 'Delaware'),),
             (('serialNumber', '3359300'),),
             (('streetAddress', '16 Allen Rd'),),
             (('postalCode', '03894-4801'),),
             (('countryName', 'US'),),
             (('stateOrProvinceName', 'NH'),),
             (('localityName', 'Wolfeboro'),),
             (('organizationName', 'Python Software Foundation'),),
             (('commonName', 'www.python.org'),)),
 'subjectAltName': (('DNS', 'www.python.org'),
                    ('DNS', 'python.org'),
                    ('DNS', 'pypi.org'),
                    ('DNS', 'docs.python.org'),
                    ('DNS', 'testpypi.org'),
                    ('DNS', 'bugs.python.org'),
                    ('DNS', 'wiki.python.org'),
                    ('DNS', 'hg.python.org'),
                    ('DNS', 'mail.python.org'),
                    ('DNS', 'packaging.python.org'),
                    ('DNS', 'pythonhosted.org'),
                    ('DNS', 'www.pythonhosted.org'),
                    ('DNS', 'test.pythonhosted.org'),
                    ('DNS', 'us.pycon.org'),
                    ('DNS', 'id.python.org')),
 'version': 3}

```

With the SSL channel now up and the certificate checked, you may go on to converse with the server:

[Subject index](INDEX.md) · [Previous](testing-for-ssl-support.md) · [Continue](tls-client-http-request.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md)

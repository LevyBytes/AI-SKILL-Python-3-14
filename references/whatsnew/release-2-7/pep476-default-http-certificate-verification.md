# What’s New in Python 2.7 / PEP 476: Enabling certificate verification by default for stdlib http clients - http, urllib.request, xmlrpc.client

### PEP 476: Enabling certificate verification by default for stdlib http clients

[**PEP 476**](https://peps.python.org/pep-0476/) revised [`httplib`](https://docs.python.org/3.14/library/http.html#module-http) along with the modules built on it, including [`urllib2`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request) and [`xmlrpclib`](https://docs.python.org/3.14/library/xmlrpc.client.html#module-xmlrpc.client), so that by default they now confirm the server is offering a certificate signed by a Certificate Authority present in the platform trust store whose hostname agrees with the one being requested — a meaningful security gain for many programs. The Python 2.7.9 release introduced this change.

Programs that depend on the former behavior can supply an alternate context:

```python
import urllib2
import ssl

# This disables all verification
context = ssl._create_unverified_context()

# This allows using a specific certificate for the host, which doesn't need
# to be in the trust store
context = ssl.create_default_context(cafile="/path/to/file.crt")

urllib2.urlopen("https://invalid-cert", context=context)

```

[Subject index](INDEX.md) · [Previous source section](pep477-ensurepip-documentation.md) · [Next source section](pep-493-https-verification-migration-tools-for-python-2-7.md) · [Release/subject declaration](the-future-for-python-2-x.md)

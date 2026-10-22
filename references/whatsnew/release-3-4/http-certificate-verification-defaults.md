# What's New In Python 3.4 / Porting to Python 3.4 / Changes in the C API / PEP 476: Enabling certificate verification by default for stdlib http clients

### Changed in 3.4.3

### PEP 476: Enabling certificate verification by default for stdlib http clients

By default, [`http.client`](https://docs.python.org/3.14/library/http.client.html#module-http.client) — and the modules built on it, [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request) and [`xmlrpc.client`](https://docs.python.org/3.14/library/xmlrpc.client.html#module-xmlrpc.client) among them — will now confirm that the certificate the server offers is signed by a CA living in the platform trust store and that its hostname lines up with the one being requested, a meaningful security gain for a great many applications.

Applications that still need the former behavior may instead supply an alternate context:

```python
import urllib.request
import ssl

# This disables all verification
context = ssl._create_unverified_context()

# This allows using a specific certificate for the host, which doesn't need
# to be in the trust store
context = ssl.create_default_context(cafile="/path/to/file.crt")

urllib.request.urlopen("https://invalid-cert", context=context)

```

[Subject index](INDEX.md) · [Previous source section](porting-to-python-3-4-changes-in-the-c-api.md) · [Release/subject declaration](release-highlights.md) · [Release/subject declaration](porting-to-python-3-4.md) · [Release/subject declaration](porting-to-python-3-4-changes-in-the-c-api.md)

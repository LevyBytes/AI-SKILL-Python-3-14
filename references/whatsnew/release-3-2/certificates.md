# What's New In Python 3.2 / certificates - http.client, urllib.request

### certificates

[`http.client.HTTPSConnection`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPSConnection), [`urllib.request.HTTPSHandler`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.HTTPSHandler) and [`urllib.request.urlopen()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.urlopen) now accept optional arguments, letting a server certificate be validated against a roster of Certificate Authorities — the recommended practice when HTTPS is used publicly.

(Added by Antoine Pitrou, [bpo-9003](https://bugs.python.org/issue?@action=redirect&bpo=9003).)

[Subject index](INDEX.md) · [Previous source section](nntp.md) · [Next source section](imaplib.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)

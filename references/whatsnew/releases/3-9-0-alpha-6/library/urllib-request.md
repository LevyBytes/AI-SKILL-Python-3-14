# Python 3.9.0 alpha 6 / library / urllib request

[bpo-39503](https://bugs.python.org/issue?@action=redirect&bpo=39503): The [`AbstractBasicAuthHandler`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.AbstractBasicAuthHandler) in [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request) now reads every WWW-Authenticate HTTP header and tolerates several challenges within one header, taking the realm from the very first Basic challenge.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

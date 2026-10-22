# Python 3.9.0 alpha 1 / library / http client

[bpo-37440](https://bugs.python.org/issue?@action=redirect&bpo=37440): For the default context, or whenever a cert_file reaches HTTPSConnection, http.client now switches on TLS 1.3 post-handshake authentication.

[bpo-38216](https://bugs.python.org/issue?@action=redirect&bpo=38216): The uncommon code that needs to issue invalid http requests via the `http.client` library is now given a route to do that. The remedies applied for [bpo-30458](https://bugs.python.org/issue?@action=redirect&bpo=30458) had broken certain projects that depended on this capability to exercise their own handling of malformed requests.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.11.0 alpha 1 / security / http client

[bpo-44022](https://bugs.python.org/issue?@action=redirect&bpo=44022): [`http.client`](https://docs.python.org/3.14/library/http.client.html#module-http.client) now refrains from endlessly reading possible HTTP headers once the server returns a `100 Continue` status response.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.8.0 alpha 4 / security / http

[bpo-30458](https://bugs.python.org/issue?@action=redirect&bpo=30458): Tackles [**CVE 2019-9740**](https://www.cve.org/CVERecord?id=CVE-2019-9740) by refusing URL paths that carry embedded whitespace or control characters into the underlying http client request. URLs of that potentially malicious header-injection kind now prompt an http.client.InvalidURL exception to be raised.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

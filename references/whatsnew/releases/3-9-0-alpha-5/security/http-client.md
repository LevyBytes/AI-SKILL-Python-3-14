# Python 3.9.0 alpha 5 / security / http client

[bpo-38576](https://bugs.python.org/issue?@action=redirect&bpo=38576): Forbid control characters within hostnames in http.client, which addresses [**CVE 2019-18348**](https://www.cve.org/CVERecord?id=CVE-2019-18348). URLs of this kind, capable of malicious header injection, now lead to an InvalidURL being raised.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

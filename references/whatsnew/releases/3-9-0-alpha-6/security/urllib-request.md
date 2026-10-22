# Python 3.9.0 alpha 6 / security / urllib request

[bpo-39503](https://bugs.python.org/issue?@action=redirect&bpo=39503): [**CVE 2020-8492**](https://www.cve.org/CVERecord?id=CVE-2020-8492): Within the [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request) module, the [`AbstractBasicAuthHandler`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.AbstractBasicAuthHandler) class relies on an inefficient regular expression that an attacker can abuse to trigger a denial of service. The regex was corrected so catastrophic backtracking no longer happens. Ben Caller and Matt Schwager reported this vulnerability.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

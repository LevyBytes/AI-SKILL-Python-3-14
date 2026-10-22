# Python 3.7.0 beta 3 / security / ssl

[bpo-33136](https://bugs.python.org/issue?@action=redirect&bpo=33136): Harden the ssl module against LibreSSL [**CVE 2018-8970**](https://www.cve.org/CVERecord?id=CVE-2018-8970). X509_VERIFY_PARAM_set1_host() now receives an explicit namelen. A new test confirms that NULL bytes stay disallowed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

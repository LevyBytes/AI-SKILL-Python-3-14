# Python 3.8.0 alpha 1 / security / ssl

[bpo-33136](https://bugs.python.org/issue?@action=redirect&bpo=33136): Harden the ssl module against LibreSSL [**CVE 2018-8970**](https://www.cve.org/CVERecord?id=CVE-2018-8970). X509_VERIFY_PARAM_set1_host() now gets called with an explicit namelen. A fresh test confirms that NULL bytes stay disallowed.

[bpo-28414](https://bugs.python.org/issue?@action=redirect&bpo=28414): The ssl module now lets users carry out their own IDN en/decoding while using SNI.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

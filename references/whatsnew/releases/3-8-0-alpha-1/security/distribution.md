# Python 3.8.0 alpha 1 / security / distribution

[bpo-35746](https://bugs.python.org/issue?@action=redirect&bpo=35746): [**CVE 2019-5010**](https://www.cve.org/CVERecord?id=CVE-2019-5010): Repair a NULL pointer deref inside the ssl module. The cert parser mishandled CRL distribution points carrying an empty DP or URI. A malicious or buggy certificate could trigger a segfault. The flaw, tracked as (TALOS-2018-0758), was reported by Cisco's Colin Read along with Nicolas Edet.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

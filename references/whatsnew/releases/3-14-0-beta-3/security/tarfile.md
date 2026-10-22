# Python 3.14.0 beta 3 / security / tarfile

[gh-135034](https://github.com/python/cpython/issues/135034): Several issues that let `tarfile` extraction filters (`filter="data"` and `filter="tar"`) be circumvented through crafted symlinks and hard links were fixed.

Addresses [**CVE 2024-12718**](https://www.cve.org/CVERecord?id=CVE-2024-12718), [**CVE 2025-4138**](https://www.cve.org/CVERecord?id=CVE-2025-4138), [**CVE 2025-4330**](https://www.cve.org/CVERecord?id=CVE-2025-4330), and [**CVE 2025-4517**](https://www.cve.org/CVERecord?id=CVE-2025-4517).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.10.0 alpha 1 / library / tarfile

[bpo-41316](https://bugs.python.org/issue?@action=redirect&bpo=41316): Adjusted the [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) module so it writes only the basename of the TAR file into the GZIP compression header.

[bpo-39017](https://bugs.python.org/issue?@action=redirect&bpo=39017): Steer clear of an infinite loop when the tarfile module reads specially crafted TAR files ([**CVE 2019-20907**](https://www.cve.org/CVERecord?id=CVE-2019-20907)).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

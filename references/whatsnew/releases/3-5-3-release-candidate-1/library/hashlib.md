# Python 3.5.3 release candidate 1 / library / hashlib

[bpo-26470](https://bugs.python.org/issue?@action=redirect&bpo=26470): Ported the ssl and hashlib modules onto OpenSSL 1.1.0.

- Dropped the option of handing a file descriptor to os.access. That had never functioned, yet earlier it stayed silent instead of raising.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.11.0 alpha 6 / build / import

[bpo-46608](https://bugs.python.org/issue?@action=redirect&bpo=46608): Leave marshalled-frozen data out when deep-freezing to recover 300 KB of disk space. Part of this is a fresh `is_package` field on [`_frozen`](https://docs.python.org/3.14/c-api/import.html#c._frozen). Kumar Aditya wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

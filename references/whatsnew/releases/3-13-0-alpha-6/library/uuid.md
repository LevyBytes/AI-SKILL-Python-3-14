# Python 3.13.0 alpha 6 / library / uuid

[gh-113308](https://github.com/python/cpython/issues/113308): Strip a few internal protected pieces out of [`uuid`](https://docs.python.org/3.14/library/uuid.html#module-uuid): `_has_uuid_generate_time_safe`, `_netbios_getnode`, `_ipconfig_getnode`, and `_load_system_functions`. None of them were in use.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

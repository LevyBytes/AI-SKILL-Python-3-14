# Python 3.5.0 alpha 1 / library / email headerregistry

[bpo-21991](https://bugs.python.org/issue?@action=redirect&bpo=21991): The "params" attributes on email.headerregistry's headers are now read-only (MappingProxyType). The dictionary used to be mutable, yet a brand-new one was built every time the attribute was accessed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

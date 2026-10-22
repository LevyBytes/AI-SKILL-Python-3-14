# Python 3.11.0 alpha 2 / c api / modules

[bpo-45395](https://bugs.python.org/issue?@action=redirect&bpo=45395): Frozen modules supplied by the user (the array assigned to `PyImport_FrozenModules`) now act as supplements instead of supplanting the whole default frozen-module set. You can still turn off a frozen stdlib module by assigning NULL to the “code” field of that custom array entry.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

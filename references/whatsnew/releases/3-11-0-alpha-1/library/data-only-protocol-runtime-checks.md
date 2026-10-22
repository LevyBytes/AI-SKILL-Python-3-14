# Python 3.11.0 alpha 1 / library / subclasses typing protocol declaring only data variables raise typeerror under

[bpo-38908](https://bugs.python.org/issue?@action=redirect&bpo=38908): Subclasses of `typing.Protocol` declaring only data variables now raise a `TypeError` under an `isinstance` check unless `runtime_checkable()` decorates them. Such checks formerly succeeded quietly. Yurii Karabas supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

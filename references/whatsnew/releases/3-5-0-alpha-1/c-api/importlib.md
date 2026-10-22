# Python 3.5.0 alpha 1 / c api / importlib

[bpo-20942](https://bugs.python.org/issue?@action=redirect&bpo=20942): PyImport_ImportFrozenModuleObject() stopped assigning __file__, mirroring importlib’s behaviour; this touches _frozen_importlib together with any module brought in through imp.init_frozen().

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

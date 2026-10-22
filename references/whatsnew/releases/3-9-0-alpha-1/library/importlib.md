# Python 3.9.0 alpha 1 / library / importlib

[bpo-35923](https://bugs.python.org/issue?@action=redirect&bpo=35923): Adjusted [`importlib.machinery.BuiltinImporter`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.BuiltinImporter) so that it relies on `loader._ORIGIN` rather than a hardcoded value. Donghee Na supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

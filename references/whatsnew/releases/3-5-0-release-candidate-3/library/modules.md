# Python 3.5.0 release candidate 3 / library / modules

[bpo-24748](https://bugs.python.org/issue?@action=redirect&bpo=24748): A compatibility issue surfaced with py2exe and pywin32, so imp.load_dynamic() again disregards modules loaded earlier, letting Python modules swap themselves out for extension modules. Petr Viktorin contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.9.0 alpha 5 / library / subprocess

[bpo-39763](https://bugs.python.org/issue?@action=redirect&bpo=39763): The `distutils.spawn.spawn` function was reimplemented on top of the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module.

[bpo-39936](https://bugs.python.org/issue?@action=redirect&bpo=39936): AIX: When subprocess is unavailable while building Python from scratch, the _aix_support module is now fixed. Rather than carrying two implementations keyed on whether subprocess exists, it relies on the new private _bootsubprocess module. Consequently, _aix_support.aix_platform() yields identical results regardless of whether subprocess is present.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

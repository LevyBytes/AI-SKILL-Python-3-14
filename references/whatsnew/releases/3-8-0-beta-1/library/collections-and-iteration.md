# Python 3.8.0 beta 1 / library / collections and iteration

[bpo-35900](https://bugs.python.org/issue?@action=redirect&bpo=35900): Permits reduction methods to hand back a 6-item tuple whose 6th element names a custom state-setting method invoked in place of the usual `__setstate__` method.

[bpo-37054](https://bugs.python.org/issue?@action=redirect&bpo=37054): Repairs the destructor for `_pyio.BytesIO` and `_pyio.TextIOWrapper`: their `_buffer` attribute is set up at the earliest opportunity (within the class body), given that `__del__()` — which then calls `close()` — depends on it.

[bpo-22102](https://bugs.python.org/issue?@action=redirect&bpo=22102): Brought support for ZIP files whose disks are set to 0. Such files are routinely produced by builtin tooling on Windows whenever the ZIP64 extension is used. Francisco Facioni supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

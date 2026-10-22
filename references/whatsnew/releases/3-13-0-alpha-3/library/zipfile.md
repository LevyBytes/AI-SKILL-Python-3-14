# Python 3.13.0 alpha 3 / library / zipfile

[gh-113971](https://github.com/python/cpython/issues/113971): The formerly protected `._compresslevel` attribute on [`zipfile.ZipInfo`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipInfo) is now exposed publicly as `.compress_level`, while the old `_compresslevel` name stays reachable through a property to keep compatibility.

[gh-112932](https://github.com/python/cpython/issues/112932): Bring back the ability for [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile) to `extractall` out of zip files containing a “/” directory entry, the sort commonly inserted into zips by certain wiki or bug tracker data exporters.

[gh-109858](https://github.com/python/cpython/issues/109858): Shield [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile) against the "quoted-overlap" zipbomb. Reading an entry that overlaps another entry or the central directory now raises BadZipFile.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

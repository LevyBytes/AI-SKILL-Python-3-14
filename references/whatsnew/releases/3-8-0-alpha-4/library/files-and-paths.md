# Python 3.8.0 alpha 4 / library / files and paths

[bpo-31292](https://bugs.python.org/issue?@action=redirect&bpo=31292): Corrected `setup.py check --restructuredtext` for files that carry `include` directives.

[bpo-30427](https://bugs.python.org/issue?@action=redirect&bpo=30427): `os.path.normcase()` now leans on `os.fspath()` to validate its argument's type. The duplicate checks in the `posixpath.normcase()` and `ntpath.normcase()` versions have therefore been dropped. Wolfgang Maier authored the patch.

[bpo-36434](https://bugs.python.org/issue?@action=redirect&bpo=36434): A write failure inside a ZIP file will no longer block it from closing cleanly.

[bpo-26978](https://bugs.python.org/issue?@action=redirect&bpo=26978): `pathlib.path.link_to()` now exists; it establishes a hard link that targets a given path.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

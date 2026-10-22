# Python 3.8.0 alpha 1 / library / sys

[bpo-33185](https://bugs.python.org/issue?@action=redirect&bpo=33185): Repaired a regression that appeared when running pydoc using the [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) switch. (That regression entered in 3.7.0b3 through the resolution of [bpo-33053](https://bugs.python.org/issue?@action=redirect&bpo=33053))

This fix additionally changed pydoc to append `os.getcwd()` onto [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) where required, in place of appending `"."`.

[bpo-33169](https://bugs.python.org/issue?@action=redirect&bpo=33169): Remove `None` entries from [`sys.path_importer_cache`](https://docs.python.org/3.14/library/sys.html#sys.path_importer_cache) whenever `importlib.machinery.invalidate_caches()` runs.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

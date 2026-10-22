# Python 3.7.0 beta 4 / library / sys

[bpo-33185](https://bugs.python.org/issue?@action=redirect&bpo=33185): Resolved a regression that appeared when running pydoc with the [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) switch. (That regression had entered in 3.7.0b3 via the fix for [bpo-33053](https://bugs.python.org/issue?@action=redirect&bpo=33053)) The same fix also made pydoc append `os.getcwd()` onto [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) where needed, in place of adding `"."`.

[bpo-33169](https://bugs.python.org/issue?@action=redirect&bpo=33169): Remove entries of `None` from [`sys.path_importer_cache`](https://docs.python.org/3.14/library/sys.html#sys.path_importer_cache) whenever `importlib.machinery.invalidate_caches()` runs.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

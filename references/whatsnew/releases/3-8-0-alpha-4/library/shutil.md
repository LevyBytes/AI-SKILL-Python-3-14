# Python 3.8.0 alpha 4 / library / shutil

[bpo-35755](https://bugs.python.org/issue?@action=redirect&bpo=35755): With `PATH` unset, [`shutil.which()`](https://docs.python.org/3.14/library/shutil.html#shutil.which) along with `distutils.spawn.find_executable` now reach for `os.confstr("CS_PATH")` where it exists rather than [`os.defpath`](https://docs.python.org/3.14/library/os.html#os.defpath). Furthermore, when `PATH` holds an empty string, neither `os.confstr("CS_PATH")` nor `os.defpath` is consulted.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

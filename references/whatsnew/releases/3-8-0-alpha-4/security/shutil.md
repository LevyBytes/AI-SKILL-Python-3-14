# Python 3.8.0 alpha 4 / security / shutil

[bpo-35755](https://bugs.python.org/issue?@action=redirect&bpo=35755): When the `PATH` environment variable is unset, [`shutil.which()`](https://docs.python.org/3.14/library/shutil.html#shutil.which) now falls back to `os.confstr("CS_PATH")` where that is supported. The working directory is also dropped from `posixpath.defpath`. As a result, on Unix neither `shutil.which()` nor the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module will look in the current directory for an executable once `PATH` is absent.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

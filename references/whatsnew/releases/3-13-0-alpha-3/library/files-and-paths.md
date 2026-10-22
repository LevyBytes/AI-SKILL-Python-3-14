# Python 3.13.0 alpha 3 / library / files and paths

[bpo-29779](https://bugs.python.org/issue?@action=redirect&bpo=29779): Introduce a fresh [`PYTHON_HISTORY`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_HISTORY) environment variable for choosing where a `.python_history` file lives.

[bpo-43153](https://bugs.python.org/issue?@action=redirect&bpo=43153): On Windows, directory cleanup in `tempfile.TemporaryDirectory` used to hide a `PermissionError` behind a `NotADirectoryError`. When errors are not ignored, it now properly raises `PermissionError`. Andrei Kulakov and Ken Jin wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

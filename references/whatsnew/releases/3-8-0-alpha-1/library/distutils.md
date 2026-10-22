# Python 3.8.0 alpha 1 / library / distutils

[bpo-35699](https://bugs.python.org/issue?@action=redirect&bpo=35699): Corrected the detection of Visual Studio Build Tools 2017 within distutils

[bpo-34421](https://bugs.python.org/issue?@action=redirect&bpo=34421): Corrected distutils logging for non-ASCII strings, which had been causing installation failures on Windows.

[bpo-34738](https://bugs.python.org/issue?@action=redirect&bpo=34738): Directory entries are now included in ZIP files that `distutils` produces.

[bpo-34251](https://bugs.python.org/issue?@action=redirect&bpo=34251): Brought back `msilib.Win64` to keep backwards compatibility, given that `distutils`' `bdist_msi` command already relies on it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

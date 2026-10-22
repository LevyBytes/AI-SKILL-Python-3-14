# Python 3.12.0 beta 1 / library / files and paths

[gh-103861](https://github.com/python/cpython/issues/103861): Stop `zipfile.Zipfile` from producing broken zip archives whenever `force_zip64` was applied while appending files. Carey Metcalfe wrote the patch.

[gh-104372](https://github.com/python/cpython/issues/104372): Reworked the `_posixsubprocess` internals so that no Python C API is touched between fork and exec while marking `pass_fds=` file descriptors inheritable.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.1 final / library / tarfile

[gh-75989](https://github.com/python/cpython/issues/75989): During hardlink extraction, [`tarfile.TarFile.extractall()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile.extractall) together with [`tarfile.TarFile.extract()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile.extract) will now replace any existing symlinks. Alexander Enrique Urieles Nieto authored this fix ([gh-75989](https://github.com/python/cpython/issues/75989)).

[gh-81325](https://github.com/python/cpython/issues/81325): When acting on a tar archive, [`tarfile.TarFile`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile) will now take a [path-like](https://docs.python.org/3.14/glossary.html#term-path-like-object) argument. Alexander Enrique Urieles Nieto authored this change ([gh-81325](https://github.com/python/cpython/issues/81325)).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

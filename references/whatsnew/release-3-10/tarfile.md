# What's New In Python 3.10 / tarfile - shutil, tarfile

### Notable changes in 3.10.12

### tarfile

- A fresh *filter* argument now lands on the extraction methods of [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) and on [`shutil.unpack_archive()`](https://docs.python.org/3.14/library/shutil.html#shutil.unpack_archive), letting you rein in tar behaviors that might prove unexpected or hazardous — writing files beyond the target directory being one example. Particulars appear under [Extraction filters](https://docs.python.org/3.14/library/tarfile.html#tarfile-extraction-filter). Under Python 3.12, calling these without the *filter* argument surfaces a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Come Python 3.14, the fallback flips to `'data'`. (Contributed by Petr Viktorin in [**PEP 706**](https://peps.python.org/pep-0706/).)

[Subject index](INDEX.md) · [Previous source section](notable-security-feature-in-3-10-8.md) · [Release/subject declaration](summary-release-highlights.md)

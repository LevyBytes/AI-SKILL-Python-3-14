# What's New In Python 3.11 / tarfile — shutil, tarfile

### Notable changes in 3.11.4

### tarfile

- A new *filter* argument has been added to the extraction methods on [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) and to [`shutil.unpack_archive()`](https://docs.python.org/3.14/library/shutil.html#shutil.unpack_archive), letting you rein in tar behaviours that might prove unexpected or hazardous — writing files beyond the destination directory, for one. The particulars live at [Extraction filters](https://docs.python.org/3.14/library/tarfile.html#tarfile-extraction-filter). On Python 3.12, calling these without the *filter* argument raises a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning), and on Python 3.14 the default flips to `'data'`. (Contributed by Petr Viktorin in [**PEP 706**](https://peps.python.org/pep-0706/).)

[Subject index](INDEX.md) · [Previous source section](c-api-changes-removed.md) · [Next source section](openssl.md) · [Release/subject declaration](summary-release-highlights.md)

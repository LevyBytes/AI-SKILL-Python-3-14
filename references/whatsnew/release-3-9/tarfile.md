# What's New In Python 3.9 / tarfile — shutil, tarfile

### Notable changes in 3.9.17

### tarfile

- The extraction methods on [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile), along with [`shutil.unpack_archive()`](https://docs.python.org/3.14/library/shutil.html#shutil.unpack_archive), gain a fresh *filter* argument that lets you rein in tar features liable to surprise or endanger you, like writing files beyond the destination directory. Consult [Extraction filters](https://docs.python.org/3.14/library/tarfile.html#tarfile-extraction-filter) for the details. Under Python 3.12, calling these without the *filter* argument surfaces a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Under Python 3.14, the default flips to `'data'`. (Contributed by Petr Viktorin in [**PEP 706**](https://peps.python.org/pep-0706/).)

[Subject index](INDEX.md) · [Previous source section](notable-security-feature-in-3-9-14.md) · [Release/subject declaration](summary-release-highlights.md)

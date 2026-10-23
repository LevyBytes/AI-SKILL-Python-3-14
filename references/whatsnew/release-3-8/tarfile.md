# What’s New In Python 3.8 / tarfile - tarfile

### tarfile

For new archives, the [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) module henceforth defaults to the current pax (POSIX.1-2001) format rather than the GNU-specific one used before. The result is stronger cross-platform portability thanks to one consistent encoding (UTF-8) within a standardized, extensible format, plus a number of further advantages. (Contributed by C.A.M. Gerlach in [bpo-36268](https://bugs.python.org/issue?@action=redirect&bpo=36268).)

### Notable changes in 3.8.17

### tarfile

- Both the extraction methods on [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) and [`shutil.unpack_archive()`](https://docs.python.org/3.14/library/shutil.html#shutil.unpack_archive) gained a *filter* argument, letting you rein in tar behaviors that could prove surprising or hazardous, like writing files beyond the destination directory. Turn to [Extraction filters](https://docs.python.org/3.14/library/tarfile.html#tarfile-extraction-filter) for the specifics. Under Python 3.12, calling these without the *filter* argument raises a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Come Python 3.14, the default flips to `'data'`. (The work here came from Petr Viktorin under [**PEP 706**](https://peps.python.org/pep-0706/).)

[Subject index](INDEX.md) · [Previous source section](sys.md) · [Next source section](threading.md) · [Release/subject declaration](assignment-expressions.md) · [Previous source section](notable-security-feature-in-3-8-14.md)

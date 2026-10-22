# Python 3.12.0 beta 1 / library / tarfile

[gh-102953](https://github.com/python/cpython/issues/102953): The extraction routines in [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) plus [`shutil.unpack_archive()`](https://docs.python.org/3.14/library/shutil.html#shutil.unpack_archive) gain a fresh *filter* argument for curbing tar features that may prove surprising or hazardous, such as writing files beyond the target directory. Refer to [Extraction filters](https://docs.python.org/3.14/library/tarfile.html#tarfile-extraction-filter) for the specifics.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

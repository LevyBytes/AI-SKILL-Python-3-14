# Python 3.5.3 release candidate 1 / library / files and paths

[bpo-29094](https://bugs.python.org/issue?@action=redirect&bpo=29094): Within a ZIP file built using an extern file object plus modes "w" and "x", offsets are now measured from the start of the file.

[bpo-28847](https://bugs.python.org/issue?@action=redirect&bpo=28847): dbm.dumb can now read read-only files and skips writing the index file whenever nothing has changed.

[bpo-26293](https://bugs.python.org/issue?@action=redirect&bpo=26293): Repair the writing of ZIP files that begin somewhere other than the start of the file. Offsets inside the ZIP file are now measured from the start of the archive, conforming to the specification.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

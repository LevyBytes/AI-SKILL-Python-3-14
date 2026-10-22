# Python 3.14.0 release candidate 1 / library / took out never released zipfile zipfile data offset property had introduced a7 because

[gh-136170](https://github.com/python/cpython/issues/136170): Took out the never-released `zipfile.ZipFile.data_offset` property that had been introduced in 3.14.0a7, because its intended behavior in certain situations stayed unclear and the outcome did not always match what a user would anticipate.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

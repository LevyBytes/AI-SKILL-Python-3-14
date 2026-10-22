# Python 3.12.0 alpha 5 / library / files and paths

[gh-96290](https://github.com/python/cpython/issues/96290): Correct how partial and invalid UNC drives are treated by `ntpath.splitdrive()`, and by `ntpath.normpath()` on systems that are not Windows. `splitdrive()` now reads paths such as ‘\server’ and ‘\’ as holding nothing but a drive, so on non-Windows systems `normpath()` leaves them alone. Because native OS APIs do the work, `normpath()` on Windows behaves the same as before. Eryk Sun wrote the patch, with help from Barney Gale.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

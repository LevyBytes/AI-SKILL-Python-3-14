# What's new in Python 3.14 / tarfile - tarfile

### tarfile

- [`data_filter()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.data_filter) now normalizes the targets of symbolic links so as to thwart path traversal attacks. (Contributed by Petr Viktorin in [gh-127987](https://github.com/python/cpython/issues/127987) and [**CVE 2025-4138**](https://www.cve.org/CVERecord?id=CVE-2025-4138).)

- [`extractall()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile.extractall) now bypasses the fix-up of directory attributes whenever a directory has been deleted or swapped out for some other kind of file. (Contributed by Petr Viktorin in [gh-127987](https://github.com/python/cpython/issues/127987) and [**CVE 2024-12718**](https://www.cve.org/CVERecord?id=CVE-2024-12718).)

- [`extract()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile.extract) and [`extractall()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile.extractall) now re-apply the extraction filter both when a link (hard or symbolic) is replaced by a copy of a different archive member and when directory attributes are being fixed up. The former case raises a new exception, [`LinkFallbackError`](https://docs.python.org/3.14/library/tarfile.html#tarfile.LinkFallbackError). (Contributed by Petr Viktorin for [**CVE 2025-4330**](https://www.cve.org/CVERecord?id=CVE-2025-4330) and [**CVE 2024-12718**](https://www.cve.org/CVERecord?id=CVE-2024-12718).)

- [`extract()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile.extract) and [`extractall()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile.extractall) no longer extract rejected members once [`errorlevel()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile.errorlevel) equals zero. (Contributed by Matt Prodani and Petr Viktorin in [gh-112887](https://github.com/python/cpython/issues/112887) and [**CVE 2025-4435**](https://www.cve.org/CVERecord?id=CVE-2025-4435).)

[Subject index](INDEX.md) · [Previous source section](sysconfig.md) · [Next source section](threading.md) · [Release/subject declaration](summary-release-highlights.md)

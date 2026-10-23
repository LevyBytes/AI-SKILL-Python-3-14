# What's New In Python 3.13 / tempfile - os, tempfile

### tempfile

- Owing to the [`os.mkdir()`](https://docs.python.org/3.14/library/os.html#os.mkdir) changes, the `0o700` default mode that [`tempfile.mkdtemp()`](https://docs.python.org/3.14/library/tempfile.html#tempfile.mkdtemp) uses now restricts access to the new directory on Windows. It acts as a mitigation for [**CVE 2024-4030**](https://www.cve.org/CVERecord?id=CVE-2024-4030). (Contributed by Steve Dower in [gh-118486](https://github.com/python/cpython/issues/118486).)

[Subject index](INDEX.md) · [Previous source section](sys.md) · [Next source section](time.md) · [Release/subject declaration](summary-release-highlights.md)

# What's new in Python 3.14 / os.path - os.path

### os.path

- A fresh value, [`ALLOW_MISSING`](https://docs.python.org/3.14/library/os.path.html#os.path.ALLOW_MISSING), is now accepted by the *strict* parameter of [`realpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.realpath). When chosen, any error besides [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) gets re-raised; the path that results may not exist yet, though it will carry no symlinks. (Contributed by Petr Viktorin for [**CVE 2025-4517**](https://www.cve.org/CVERecord?id=CVE-2025-4517).)

[Subject index](INDEX.md) · [Previous source section](os.md) · [Next source section](pathlib.md) · [Release/subject declaration](summary-release-highlights.md)

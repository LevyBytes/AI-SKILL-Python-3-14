# What's New In Python 3.7 / Notable changes in Python 3.7.2 — venv

### Notable changes in Python 3.7.2

Within 3.7.2, [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv) running on Windows stops copying the original binaries and instead produces redirector scripts called `python.exe` and `pythonw.exe`. This clears up a long-running problem whereby every virtual environment had to be upgraded or rebuilt with each Python update. Be aware, though, that this release still calls for rebuilding virtual environments so as to pick up the new scripts.

[Subject index](INDEX.md) · [Previous source section](notable-changes-in-python-3-7-1.md) · [Next source section](notable-changes-in-python-3-7-6.md) · [Release/subject declaration](summary-release-highlights.md)

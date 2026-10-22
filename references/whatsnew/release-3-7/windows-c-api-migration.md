# What's New In Python 3.7 / Porting to Python 3.7 / Changes in the C API / Windows-only Changes — sys

### Windows-only Changes

The file that overrides [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) now goes by `<python-executable>._pth` in place of `'sys.path'`. Consult [Finding modules](https://docs.python.org/3.14/using/windows.html#windows-finding-modules) for further detail. Steve Dower contributed this through [bpo-28137](https://bugs.python.org/issue?@action=redirect&bpo=28137).

[Subject index](INDEX.md) · [Previous source section](bytecode-migration-changes.md) · [Next source section](cpython-implementation-migration.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](porting-to-python-3-7.md) · [Release/subject declaration](porting-to-python-3-7-changes-in-the-c-api.md)

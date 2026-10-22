# Python 3.5.1 release candidate 1 / tests / numeric behavior

[bpo-23919](https://bugs.python.org/issue?@action=redirect&bpo=23919): Keep assert dialogs from popping up during the test suite.

- There used to be a ceiling of 9 forwarded arguments; now `PCbuild\rt.bat` will hand any number of them straight through to regrtest.py.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

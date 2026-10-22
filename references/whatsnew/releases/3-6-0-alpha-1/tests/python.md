# Python 3.6.0 alpha 1 / tests / python

[bpo-22806](https://bugs.python.org/issue?@action=redirect&bpo=22806): A new `python -m test --list-tests` command was added that lists the available tests.

[bpo-18174](https://bugs.python.org/issue?@action=redirect&bpo=18174): The `python -m test --huntrleaks ...` mode now additionally watches for file-descriptor leaks. Richard Oudkerk wrote the patch.

[bpo-25260](https://bugs.python.org/issue?@action=redirect&bpo=25260): Repair `python -m test --coverage` behavior on Windows. The roster of ignored directories was dropped.

- `PCbuild\rt.bat` will now take any number of arguments and forward them to regrtest.py. Earlier the cap sat at 9.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

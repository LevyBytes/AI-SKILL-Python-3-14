# Python 3.7.0 alpha 3 / idle / imports and modules

[bpo-31836](https://bugs.python.org/issue?@action=redirect&bpo=31836): When it runs after test_idle (which sets ps1), Test_code_module now passes. The code module relies on sys.ps1 when present, otherwise assigning it ?>>> ?. Both of those paths are now tested correctly by Test_code_module. The same applies to ps2.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.6.4 release candidate 1 / idle / imports and modules

[bpo-31836](https://bugs.python.org/issue?@action=redirect&bpo=31836): Test_code_module now succeeds when run after test_idle, which assigns ps1. Should sys.ps1 be present the code module uses it, otherwise it assigns ?>>> ?. Both of those behaviors are now tested properly by Test_code_module. The same applies to ps2.

[bpo-1612262](https://bugs.python.org/issue?@action=redirect&bpo=1612262): Nested classes plus functions are now displayed by IDLE's module browser. Guilherme Polo and Cheryl Sabella respectively wrote the original patches for the code and the tests.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

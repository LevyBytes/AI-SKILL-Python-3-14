# Python 3.9.0 alpha 5 / c api / descriptor

[bpo-39884](https://bugs.python.org/issue?@action=redirect&bpo=39884): To make debugging easier, [`PyDescr_NewMethod()`](https://docs.python.org/3.14/c-api/descriptor.html#c.PyDescr_NewMethod) and [`PyCFunction_NewEx()`](https://docs.python.org/3.14/c-api/structures.html#c.PyCFunction_NewEx) now embed the method name within the SystemError "bad call flags" error message.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

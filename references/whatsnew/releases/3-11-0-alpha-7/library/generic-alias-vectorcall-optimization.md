# Python 3.11.0 alpha 7 / library / make calls genericalias objects faster adopting pep vectorcall trading

[bpo-47067](https://bugs.python.org/issue?@action=redirect&bpo=47067): Make calls on `GenericAlias` objects faster by adopting [**PEP 590**](https://peps.python.org/pep-0590/) `vectorcall` and by trading `PyObject_SetAttrString` for `PyObject_SetAttr`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

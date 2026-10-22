# Python 3.10.0 beta 1 / c api / functions and types

[bpo-43962](https://bugs.python.org/issue?@action=redirect&bpo=43962): _PyInterpreterState_IDIncref() now invokes _PyInterpreterState_IDInitref() and always bumps id_refcount. Previously, a call to _xxsubinterpreters.get_current() could leave id_refcount inconsistent once a _xxsubinterpreters.InterpreterID object was freed. Victor Stinner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

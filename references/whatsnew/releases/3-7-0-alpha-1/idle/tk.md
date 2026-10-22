# Python 3.7.0 alpha 1 / idle / tk

[bpo-31414](https://bugs.python.org/issue?@action=redirect&bpo=31414): IDLE – repair the tk entry box tests by clearing them first. Appending to an int entry differs from deleting then inserting, since int(‘’) raises an error.

[bpo-30853](https://bugs.python.org/issue?@action=redirect&bpo=30853): IDLE – Split a VarTrace class out of ConfigDialog. Instance tracers handle pairs made up of a tk variable plus a callback function. Once tracing is enabled, assigning the variable invokes the function. The new class has 100% test coverage.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

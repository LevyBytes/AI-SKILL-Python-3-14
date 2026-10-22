# Python 3.6.3 release candidate 1 / idle / tk

[bpo-31414](https://bugs.python.org/issue?@action=redirect&bpo=31414): IDLE — repaired the tk entry-box tests by clearing them first. Appending to an int entry differs from a delete-then-insert because `int('')` will fail.

[bpo-30853](https://bugs.python.org/issue?@action=redirect&bpo=30853): IDLE — Extract a VarTrace class out of ConfigDialog. The instance tracers handle pairs, each made of a tk variable plus a callback function. With tracing active, assigning the variable invokes the function. The fresh class enjoys 100% test coverage.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

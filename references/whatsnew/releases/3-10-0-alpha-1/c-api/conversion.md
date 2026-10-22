# Python 3.10.0 alpha 1 / c api / conversion

[bpo-41524](https://bugs.python.org/issue?@action=redirect&bpo=41524): Repaired a defect in [`PyOS_mystrnicmp()`](https://docs.python.org/3.14/c-api/conversion.html#c.PyOS_mystrnicmp) and [`PyOS_mystricmp()`](https://docs.python.org/3.14/c-api/conversion.html#c.PyOS_mystricmp) whereby pointers advanced past where the string ended.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

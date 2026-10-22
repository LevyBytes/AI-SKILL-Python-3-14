# Python 3.11.0 alpha 4 / c api / function

[bpo-46236](https://bugs.python.org/issue?@action=redirect&bpo=46236): Repair a defect in [`PyFunction_GetAnnotations()`](https://docs.python.org/3.14/c-api/function.html#c.PyFunction_GetAnnotations) that made it hand back a `tuple` rather than a `dict`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

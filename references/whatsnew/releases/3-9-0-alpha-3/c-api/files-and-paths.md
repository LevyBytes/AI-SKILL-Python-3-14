# Python 3.9.0 alpha 3 / c api / files and paths

[bpo-39372](https://bugs.python.org/issue?@action=redirect&bpo=39372): Header files were cleaned of interfaces that were declared yet never implemented. The public API symbols dropped here are: `_PyBytes_InsertThousandsGroupingLocale`, `_PyBytes_InsertThousandsGrouping`, `_Py_InitializeFromArgs`, `_Py_InitializeFromWideArgs`, `_PyFloat_Repr`, `_PyFloat_Digits`, `_PyFloat_DigitsInit`, `PyFrame_ExtendStack`, `_PyAIterWrapper_Type`, `PyNullImporter_Type`, `PyCmpWrapper_Type`, `PySortWrapper_Type`, `PyNoArgsFunction`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

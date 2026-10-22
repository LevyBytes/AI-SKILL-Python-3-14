# Python 3.9.0 alpha 1 / build / veryhigh

[bpo-37189](https://bugs.python.org/issue?@action=redirect&bpo=37189): A range of `PyRun_*XXX*()` functions such as [`PyRun_String()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyRun_String) had stopped being exported from `libpython38.dll` by accident. They are exported once more so the ABI stays compatible.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

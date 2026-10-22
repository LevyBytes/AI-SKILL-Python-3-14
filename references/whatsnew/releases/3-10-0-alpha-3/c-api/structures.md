# Python 3.10.0 alpha 3 / c api / structures

[bpo-42171](https://bugs.python.org/issue?@action=redirect&bpo=42171): The [`METH_FASTCALL`](https://docs.python.org/3.14/c-api/structures.html#c.METH_FASTCALL) calling convention joins the limited API. On Windows, the limited API gains the [`PyModule_AddType()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_AddType), [`PyType_FromModuleAndSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromModuleAndSpec), [`PyType_GetModule()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetModule) and [`PyType_GetModuleState()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetModuleState) functions.

[bpo-39573](https://bugs.python.org/issue?@action=redirect&bpo=39573): Turn [`Py_TYPE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_TYPE) plus [`Py_SIZE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_SIZE) back into macros so they remain usable as an l-value. Numerous external C extension modules depend on being able to use Py_TYPE() and Py_SIZE() for assigning an object's type and size: `Py_TYPE(obj) = type;` and `Py_SIZE(obj) = size;`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

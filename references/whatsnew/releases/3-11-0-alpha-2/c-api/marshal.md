# Python 3.11.0 alpha 2 / c api / marshal

[bpo-45474](https://bugs.python.org/issue?@action=redirect&bpo=45474): Defining `Py_LIMITED_API` now hides the items below:

  - [`PyMarshal_WriteLongToFile()`](https://docs.python.org/3.14/c-api/marshal.html#c.PyMarshal_WriteLongToFile)

  - [`PyMarshal_WriteObjectToFile()`](https://docs.python.org/3.14/c-api/marshal.html#c.PyMarshal_WriteObjectToFile)

  - [`PyMarshal_ReadObjectFromString()`](https://docs.python.org/3.14/c-api/marshal.html#c.PyMarshal_ReadObjectFromString)

  - [`PyMarshal_WriteObjectToString()`](https://docs.python.org/3.14/c-api/marshal.html#c.PyMarshal_WriteObjectToString)

  - the `Py_MARSHAL_VERSION` macro

None of these belong to the [limited API](https://docs.python.org/3.14/c-api/stable.html#limited-api-list).

Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

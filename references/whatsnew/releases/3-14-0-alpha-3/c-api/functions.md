# Python 3.14.0 alpha 3 / c api / functions

[gh-102471](https://github.com/python/cpython/issues/102471): Introduce a fresh import-and-export API for Python [`int`](https://docs.python.org/3.14/library/functions.html#int) objects ([**PEP 757**](https://peps.python.org/pep-0757/)):

  - [`PyLong_GetNativeLayout()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_GetNativeLayout);

  - [`PyLong_Export()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_Export);

  - [`PyLong_FreeExport()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FreeExport);

  - [`PyLongWriter_Create()`](https://docs.python.org/3.14/c-api/long.html#c.PyLongWriter_Create);

  - [`PyLongWriter_Finish()`](https://docs.python.org/3.14/c-api/long.html#c.PyLongWriter_Finish);

  - [`PyLongWriter_Discard()`](https://docs.python.org/3.14/c-api/long.html#c.PyLongWriter_Discard).

Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

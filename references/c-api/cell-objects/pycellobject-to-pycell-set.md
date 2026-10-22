# cell objects C API: `PyCellObject`, `PyCell_Type`, `PyCell_Check()`, `PyCell_New()`, `PyCell_Get()`, `PyCell_GET()`, `PyCell_Set()`, `PyCell_SET()`

type PyCellObject

The C structure that underlies cell objects.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyCell_Type

The type object that goes with cell objects.

 int PyCell_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

Yield true when *ob* is a cell object; *ob* is required to be non-`NULL`. This call never fails.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCell_New([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

*Return value: New reference.*

Build and hand back a fresh cell object that holds the value *ob*. Passing `NULL` for the parameter is allowed.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCell_Get([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *cell)

*Return value: New reference.*

Give back what the cell *cell* holds, which may be `NULL`. Where *cell* is not a cell object, the result is `NULL` and an exception is set.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCell_GET([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *cell)

*Return value: Borrowed reference.*

Give back what the cell *cell* holds, yet skip verifying that *cell* is both non-`NULL` and an actual cell object.

 int PyCell_Set([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *cell, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value)

Store *value* as the contents of the cell object *cell*. Doing so drops the reference to whatever the cell currently holds. *value* is allowed to be `NULL`, while *cell* has to be non-`NULL`.

When it succeeds, `0` is returned. Where *cell* is not a cell object, an exception is set and `-1` comes back.

 void PyCell_SET([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *cell, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value)

Places *value* into the cell object *cell*. It touches no reference counts and performs no safety checks; *cell* has to be non-`NULL` as well as a genuine cell object.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](cell-objects.md)

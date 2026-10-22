# PyWideStringList

### PyWideStringList

 type PyWideStringList

A list holding `wchar_t*` strings.

When *length* isn't zero, *items* has to be non-`NULL`, and every string within has to be non-`NULL` too.

Methods:

 PyStatus PyWideStringList_Append(PyWideStringList *list, const wchar_t *item)

Tack *item* onto the end of *list*.

Calling this requires that Python already be preinitialized.

 PyStatus PyWideStringList_Insert(PyWideStringList *list, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) index, const wchar_t *item)

Place *item* into *list* at position *index*.

When *index* reaches or exceeds the length of *list*, *item* is appended to *list* instead.

A value of `0` or higher is required for *index*.

Calling this requires that Python already be preinitialized.

Structure fields:

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) length

The list's length.

 wchar_t **items

The list's items.

[Subject index](INDEX.md) · [Previous source contract](example.md) · [Following source contract](pystatus-to-pystatus-isexit.md)

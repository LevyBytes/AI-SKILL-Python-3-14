# tuple objects C API: `PyStructSequence_Desc`

type PyStructSequence_Desc

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) (including all members).*

Holds the meta information describing a struct sequence type that is to be created.

 const char *name

The type's fully qualified, null-terminated UTF-8 name. This name has to include the module portion.

 const char *doc

Pointer to docstring for the type or `NULL` to omit.

 PyStructSequence_Field *fields

Pointer to `NULL`-terminated array with field names of the new type.

 int n_in_sequence

Number of fields visible to the Python side (if used as tuple).

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytupleobject-to-pytuple-setitem.md) · [Owning C API section and shared conditions](pystructsequence-newtype-to-pystructsequence-inittype2.md) · [Following source contract](pystructsequence-field-to-pystructsequence-set-item.md)

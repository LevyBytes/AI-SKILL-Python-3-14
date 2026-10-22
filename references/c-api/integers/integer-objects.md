# integers C API: Integer conversion error-result conventions

### Integer Objects

Every integer is backed by a ?long? integer object whose size has no fixed upper bound.

When something goes wrong, the bulk of the `PyLong_As*` APIs hand back `(return type)-1`, a result indistinguishable from a legitimate value. Call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to tell the two apart.

[Subject index](INDEX.md) · [Following source contract](pylongobject-to-pylong-fromdouble.md)

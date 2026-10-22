# PyVarObject.ob_size

### PyVarObject Slots

[`PyVarObject.ob_size`](https://docs.python.org/3.14/c-api/structures.html#c.PyVarObject.ob_size)

>

With statically allocated type objects, set this to zero up front. With dynamically allocated type objects, the field takes on a special internal significance.

Reach this field through the [`Py_SIZE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_SIZE) macro.

**Inheritance:**

This field is not inherited by subtypes.

[Subject index](INDEX.md) · [Previous source contract](pyobject-ob-refcnt-to-pyobject-ob-type.md) · [Following source contract](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md)

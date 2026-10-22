# object.__delattr__(*self*, *name*)

object.__delattr__(*self*, *name*)

Like `__setattr__()` except for attribute deletion rather than assignment. This should be implemented only when `del obj.name` carries meaning for the object.

For certain sensitive attribute deletions, raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `object.__delattr__` with arguments `obj` and `name`.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-attribute-access.md) · [Previous source section](object-setattr.md) · [Following source section](object-dir.md)

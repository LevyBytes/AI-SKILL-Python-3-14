# object.__setattr__(*self*, *name*, *value*)

object.__setattr__(*self*, *name*, *value*)

Invoked once an attribute assignment is attempted. This fires instead of the usual mechanism (namely, keeping the value within the instance dictionary). Here *name* names the attribute, while *value* holds what should be assigned to it.

Should `__setattr__()` wish to assign to an instance attribute, it ought to invoke the base class method bearing the same name, for instance, `object.__setattr__(self, name, value)`.

For certain sensitive attribute assignments, raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `object.__setattr__` with arguments `obj`, `name`, `value`.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-attribute-access.md) · [Previous source section](object-getattribute.md) · [Following source section](object-delattr.md)

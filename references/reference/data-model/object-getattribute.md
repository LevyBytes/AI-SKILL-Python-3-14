# object.__getattribute__(*self*, *name*)

object.__getattribute__(*self*, *name*)

Invoked unconditionally to carry out attribute accesses for the class’s instances. Should the class additionally define `__getattr__()`, the latter goes uncalled unless `__getattribute__()` either invokes it outright or raises an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError). This method should give back the (computed) attribute value or raise an `AttributeError` exception. To steer clear of infinite recursion within this method, its implementation should always invoke the base class method bearing the same name to reach any attributes it requires, for instance, `object.__getattribute__(self, name)`.

Note

This method can still be circumvented when special methods are looked up as the upshot of implicit invocation through language syntax or built-in functions. Consult Special method lookup.

For certain sensitive attribute accesses, raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `object.__getattr__` with arguments `obj` and `name`.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-attribute-access.md) · [Previous source section](object-getattr.md) · [Following source section](object-setattr.md)

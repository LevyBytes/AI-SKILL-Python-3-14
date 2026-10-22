# object.__objclass__

object.__objclass__

The [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect) module reads the `__objclass__` attribute as naming the class where this object was defined (setting this suitably can aid runtime introspection of dynamic class attributes). For callables, it may indicate that the first positional argument is expected or required to be an instance of the named type (or a subclass) (for instance, CPython assigns this attribute on unbound methods that are implemented in C).

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-attribute-access.md) · [Owning language section](implementing-descriptors.md) · [Previous source section](object-delete.md) · [Following source section](invoking-descriptors.md)

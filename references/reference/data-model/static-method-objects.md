# 3.2.13.5. Static method objects

#### 3.2.13.5. Static method objects

Static method objects offer a means of bypassing the conversion of function objects into method objects described above. A static method object wraps some other object, typically a user-defined method object. Whenever a static method object is fetched from a class or from a class instance, what is genuinely handed back is the wrapped object, which undergoes no additional transformation. Static method objects can also be called. The built-in [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod) constructor produces static method objects.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](internal-types.md) · [Previous source section](slice-indices.md) · [Following source section](class-method-objects.md)

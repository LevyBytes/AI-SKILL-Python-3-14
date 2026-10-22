# 3.3.2.4. __slots__

#### 3.3.2.4. __slots__

*__slots__* let us declare data members explicitly (much like properties) and refuse the creation of `__dict__` and *__weakref__* (unless declared explicitly in *__slots__* or available in a parent.)

The space conserved over relying on `__dict__` can be considerable. Attribute lookup speed can be markedly improved too.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-attribute-access.md) · [Previous source section](invoking-descriptors.md) · [Following source section](object-slots.md)

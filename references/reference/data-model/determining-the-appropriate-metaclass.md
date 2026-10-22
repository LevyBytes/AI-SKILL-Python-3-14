# 3.3.3.3. Determining the appropriate metaclass

#### 3.3.3.3. Determining the appropriate metaclass

Picking the right metaclass for a class definition proceeds like this:

- if neither bases nor an explicit metaclass are supplied, then [`type()`](https://docs.python.org/3.14/library/functions.html#type) is used;

- if an explicit metaclass is supplied and it is *not* an instance of [`type()`](https://docs.python.org/3.14/library/functions.html#type), then that object serves directly as the metaclass;

- if either an instance of [`type()`](https://docs.python.org/3.14/library/functions.html#type) is supplied as the explicit metaclass or bases are present, then the most derived metaclass is used.

The most derived metaclass is chosen from among the explicitly named metaclass (when there is one) together with the metaclasses (that is, `type(cls)`) of every named base class. The most derived metaclass is the one that is a subtype of *all* of those candidate metaclasses. When no candidate metaclass satisfies that requirement, the class definition fails with `TypeError`.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-class-creation.md) · [Previous source section](object-mro-entries.md) · [Following source section](preparing-the-class-namespace.md)

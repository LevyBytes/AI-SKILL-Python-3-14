# 3.2.8.9. Class Instances

#### 3.2.8.9. Class Instances

Any class's instances can become callable once a `__call__()` method is defined within that class.

### 3.2.11. Class instances

Calling a class object (see above) produces a class instance. Each class instance carries a namespace backed by a dictionary, which is the first location consulted when attribute references are resolved. Should an attribute be absent there while the instance’s class possesses an attribute under that name, the search moves on to the class attributes. When the class attribute located is a user-defined function object, it gets turned into an instance method object whose `__self__` attribute equals the instance. Static method and class method objects undergo conversion too; refer above under "Classes". Consult the section Implementing Descriptors for a further way in which attributes of a class fetched by way of its instances can diverge from the objects actually kept in the class’s `__dict__`. Should no class attribute turn up while the object’s class defines a `__getattr__()` method, that method runs to fulfill the lookup.

Assignments to and deletions of attributes write into the instance’s dictionary, never into a class’s dictionary. Should the class define a `__setattr__()` or `__delattr__()` method, that runs in place of writing into the instance dictionary directly.

By providing methods with particular special names, class instances can masquerade as numbers, sequences, or mappings. Consult the section Special method names.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](callable-types.md) · [Previous source section](classes.md) · [Following source section](modules.md) · [Previous source section](type-subclasses.md) · [Following source section](object-class.md)

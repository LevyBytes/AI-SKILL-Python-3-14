# 3.3.2.2. Implementing Descriptors

#### 3.3.2.2. Implementing Descriptors

The methods below apply solely when an instance of the class holding the method (a so-called *descriptor* class) shows up in an *owner* class (the descriptor has to reside in either the owner’s class dictionary or in the class dictionary of one of its parents). Across the examples below, “the attribute” names the attribute whose name is the key of the property within the owner class’ `__dict__`. The [`object`](https://docs.python.org/3.14/library/functions.html#object) class itself implements none of these protocols.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-attribute-access.md) · [Previous source section](module-class.md) · [Following source section](object-get.md)

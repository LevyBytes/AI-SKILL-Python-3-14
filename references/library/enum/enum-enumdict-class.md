# enum: `enum.EnumDict`

*class *enum.EnumDict

A subclass of [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), *EnumDict* acts as the namespace in which enum classes get defined (refer to [Preparing the class namespace](https://docs.python.org/3.14/reference/datamodel.html#prepare)). It is made public so that authors can write `EnumType` subclasses with sophisticated behavior, for instance attaching several values to a single member. Hand it the name of whichever enum class you are constructing; skip that and private names plus internal classes end up mishandled.

Keep in mind the override touches only the [`MutableMapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.MutableMapping) interface — namely [`__setitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setitem__) and [`update()`](https://docs.python.org/3.14/library/stdtypes.html#dict.update). You might still slip past these guards by reaching for other `dict` operations such as [`|=`](https://docs.python.org/3.14/reference/datamodel.html#object.__ior__).

 member_names

The names of the members, given as a list.

Added in version 3.13.

---

[Subject index](INDEX.md) · [Previous](enum-flagboundary-keep-behavior-and-intflag-default.md) · [Continue](supported-dunder-names.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md) · [Owning module, declaration or section: Data types](enum-enumtype-class.md)

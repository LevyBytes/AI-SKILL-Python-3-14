# 3.2.10. Custom classes

### 3.2.10. Custom classes

Class definitions are the usual means of creating custom class types (consult the section [Class definitions](https://docs.python.org/3.14/reference/compound_stmts.html#class)). Each class carries a namespace backed by a dictionary object. References to class attributes map onto lookups within that dictionary; for example, `C.x` maps onto `C.__dict__["x"]` (though several hooks make alternative ways of finding attributes possible). Should the attribute name be absent there, the search for the attribute proceeds into the base classes. That search through the base classes relies on the C3 method resolution order, which works properly even when 'diamond' inheritance arrangements exist, with several inheritance routes converging back on a shared ancestor. Further information about the C3 MRO that Python employs is available at [The Python 2.3 Method Resolution Order](https://docs.python.org/3.14/howto/mro.html#python-2-3-mro).

Whenever a reference to a class attribute (on class `C`, say) would produce a class method object, it gets turned into an instance method object whose `__self__` attribute equals `C`. Whenever it would produce a [`staticmethod`](https://docs.python.org/3.14/library/functions.html#staticmethod) object, it gets turned into the object that the static method object wraps. Consult the section Implementing Descriptors for a further way in which attributes fetched from a class can diverge from those actually held within its `__dict__`.

Assignments to class attributes write into the class’s own dictionary, never into the dictionary belonging to a base class.

You can call a class object (see above) to produce a class instance (see below).

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Previous source section](module-dict.md) · [Following source section](special-attributes.md)

# weakref: `weakref.WeakValueDictionary`, `WeakValueDictionary.valuerefs()`

*class *weakref.WeakValueDictionary([*dict*])

A mapping class that holds its values weakly. An entry is dropped from the dictionary once no strong reference to its value survives.

Changed in version 3.9: Added the `|` and `|=` operators, following what [**PEP 584**](https://peps.python.org/pep-0584/) lays out.

A `WeakValueDictionary` object carries one extra method that shares the very caveats described for the `WeakKeyDictionary.keyrefs()` method.

 WeakValueDictionary.valuerefs()

Hand back an iterable of the weak references aimed at the values.

[Subject index](INDEX.md) · [Previous](weakref-weakkeydictionary-class-to-weakkeydictionary-keyrefs.md) · [Continue](weakref-weakset-class.md) · [Owning module, declaration or section: weakref](weakref-ref-class.md)

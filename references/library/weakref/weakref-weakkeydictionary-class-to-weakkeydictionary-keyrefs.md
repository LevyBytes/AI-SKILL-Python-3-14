# weakref: `weakref.WeakKeyDictionary`, `WeakKeyDictionary.keyrefs()`

*class *weakref.WeakKeyDictionary([*dict*])

A mapping class that holds its keys weakly. An entry is dropped from the dictionary once no strong reference to its key remains. This lets you bind extra data to an object that other parts of an application own, without piling attributes onto those objects — which is especially handy for objects that override attribute access.

Keep in mind that inserting a key whose value equals an existing key (yet whose identity differs) swaps out the value but leaves the existing key in place. Because of that, deleting the reference to the original key also wipes the dictionary entry:

```python
>>> class T(str): pass
...
>>> k1, k2 = T(), T()
>>> d = weakref.WeakKeyDictionary()
>>> d[k1] = 1   # d = {k1: 1}
>>> d[k2] = 2   # d = {k1: 2}
>>> del k1      # d = {}

```

One way around that is to delete the key before reassigning it:

```python
>>> class T(str): pass
...
>>> k1, k2 = T(), T()
>>> d = weakref.WeakKeyDictionary()
>>> d[k1] = 1   # d = {k1: 1}
>>> del d[k1]
>>> d[k2] = 2   # d = {k2: 2}
>>> del k1      # d = {k2: 2}

```

Changed in version 3.9: Gained support for the `|` and `|=` operators, per [**PEP 584**](https://peps.python.org/pep-0584/).

A `WeakKeyDictionary` object carries one extra method that surfaces the internal references straight away. Those references are not promised to be “live” when you reach for them, so check what calling a reference yields before relying on it. This serves to keep you from minting references that would make the garbage collector hold onto the keys longer than necessary.

 WeakKeyDictionary.keyrefs()

Hand back an iterable of the weak references aimed at the keys.

[Subject index](INDEX.md) · [Previous](weakref-proxy-to-weakref-getweakrefs.md) · [Continue](weak-value-dictionary-and-value-references.md) · [Owning module, declaration or section: weakref](weakref-ref-class.md)

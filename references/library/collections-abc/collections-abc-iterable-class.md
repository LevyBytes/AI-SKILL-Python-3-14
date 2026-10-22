# collections.abc: `collections.abc.Iterable`

*class *collections.abc.Iterable

ABC for classes that provide the [`__iter__()`](https://docs.python.org/3.14/library/stdtypes.html#container.__iter__) method.

A check of `isinstance(obj, Iterable)` recognizes classes registered as `Iterable` along with those carrying an [`__iter__()`](https://docs.python.org/3.14/library/stdtypes.html#container.__iter__) method, yet it overlooks classes that iterate by way of the [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) method. Calling `iter(obj)` is the sole dependable means of finding out whether an object is [iterable](https://docs.python.org/3.14/glossary.html#term-iterable).

[Subject index](INDEX.md) · [Previous](collections-abc-callable-class.md) · [Continue](collections-abc-collection-class.md) · [Owning module, declaration or section: collections.abc](collections-abc-abstract-base-classes-for-containers.md) · [Owning module, declaration or section: Collections Abstract Base Classes ??? Detailed Descriptions](collections-abc-container-class.md)

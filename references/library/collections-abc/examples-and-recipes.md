# collections.abc — Examples and Recipes

### Examples and Recipes

With ABCs we can interrogate classes or instances about whether they offer specific functionality, for example:

```python
size = None
if isinstance(myvar, collections.abc.Sized):
    size = len(myvar)

```

A number of the ABCs serve nicely as mixins too, simplifying the job of building classes that support container APIs. To take an example, building a class that supports the entire `Set` API requires supplying only the three foundational abstract methods: [`__contains__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__contains__), [`__iter__()`](https://docs.python.org/3.14/library/stdtypes.html#container.__iter__), and [`__len__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__len__). The ABC contributes the rest of the methods, such as `__and__()` and [`isdisjoint()`](https://docs.python.org/3.14/library/stdtypes.html#frozenset.isdisjoint):

```python
class ListBasedSet(collections.abc.Set):
    ''' Alternate set implementation favoring space over speed
        and not requiring the set elements to be hashable. '''
    def __init__(self, iterable):
        self.elements = lst = []
        for value in iterable:
            if value not in lst:
                lst.append(value)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, value):
        return value in self.elements

    def __len__(self):
        return len(self.elements)

s1 = ListBasedSet('abcdef')
s2 = ListBasedSet('defghi')
overlap = s1 & s2            # The __and__() method is supported automatically

```

Notes on using `Set` and `MutableSet` as a mixin:

1.

Because certain set operations build new sets, the default mixin methods require a means of creating new instances out of an [iterable](https://docs.python.org/3.14/glossary.html#term-iterable). The presumption is that the class constructor carries a signature shaped like `ClassName(iterable)`. That presumption gets factored out into an internal [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod) named `_from_iterable()`, which invokes `cls(iterable)` to yield a new set. Should the `Set` mixin be applied within a class whose constructor signature differs, you will have to override `_from_iterable()` using a classmethod or an ordinary method capable of constructing new instances from an iterable argument.

2.

To override the comparisons (presumably for speed, given that the semantics are fixed), redefine [`__le__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__le__) and [`__ge__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__ge__), after which the remaining operations will fall into line on their own.

3.

The `Set` mixin furnishes a `_hash()` method for computing a hash value over the set; nevertheless, [`__hash__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__) goes undefined, because not every set is [hashable](https://docs.python.org/3.14/glossary.html#term-hashable) or immutable. To give a set hashability through mixins, inherit from `Set` and `Hashable` both, then set `__hash__ = Set._hash`.

See also

- [OrderedSet recipe](https://code.activestate.com/recipes/576694/) for an example built on `MutableSet`.

- For more about ABCs, see the [`abc`](https://docs.python.org/3.14/library/abc.html#module-abc) module and [**PEP 3119**](https://peps.python.org/pep-3119/).

[Subject index](INDEX.md) · [Previous](collections-abc-buffer-class.md) · [Owning module, declaration or section: collections.abc](collections-abc-abstract-base-classes-for-containers.md)

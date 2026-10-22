# operator: `operator.itemgetter()`, `operator.methodcaller()`

`operator.itemgetter(*item*)`

 `operator.itemgetter(**items*)`

Produce a callable that retrieves *item* from its operand by way of that operand's [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) method. Name more than one item and a tuple of the looked-up values comes back. As an illustration:

- After `f = itemgetter(2)`, the call `f(r)` returns `r[2]`.

- After `g = itemgetter(2, 5, 3)`, the call `g(r)` returns `(r[2], r[5], r[3])`.

Equivalent to:

```python
def itemgetter(*items):
    if len(items) == 1:
        item = items[0]
        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)
    return g

```

Whatever type that operand's [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) method allows can serve as the items. A [hashable](https://docs.python.org/3.14/glossary.html#term-hashable) value of any kind works for dictionaries. With lists, tuples, and strings you supply either an index or a slice:

```python
>>> itemgetter(1)('ABCDEFG')
'B'
>>> itemgetter(1, 3, 5)('ABCDEFG')
('B', 'D', 'F')
>>> itemgetter(slice(2, None))('ABCDEFG')
'CDEFG'
>>> soldier = dict(rank='captain', name='dotterbart')
>>> itemgetter('rank')(soldier)
'captain'

```

Here's how `itemgetter()` can grab particular fields out of a tuple record:

```python
>>> inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
>>> getcount = itemgetter(1)
>>> list(map(getcount, inventory))
[3, 2, 5, 1]
>>> sorted(inventory, key=getcount)
[('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]

```

 `operator.methodcaller(*name*, */*, **args*, ***kwargs*)`

Produce a callable that invokes the method *name* on its operand. Should you supply extra positional and/or keyword arguments, those get passed along to the method too. As an illustration:

- After `f = methodcaller('name')`, the call `f(b)` returns `b.name()`.

- After `f = methodcaller('name', 'foo', bar=1)`, the call `f(b)` returns `b.name('foo', bar=1)`.

Equivalent to:

```python
def methodcaller(name, /, *args, **kwargs):
    def caller(obj):
        return getattr(obj, name)(*args, **kwargs)
    return caller

```

[Subject index](INDEX.md) · [Previous](operator-call-to-operator-attrgetter.md) · [Continue](mapping-operators-to-functions.md) · [Owning module, declaration or section: operator](operator-lt-to-operator-abs.md)

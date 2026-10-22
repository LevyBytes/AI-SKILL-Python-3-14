# collections / OrderedDict objects: `popitem()`, `move_to_end()`

popitem(*last=True*)

For ordered dictionaries, the `popitem()` method returns and removes a (key, value) pair. Those pairs come back in LIFO order when *last* is true or in FIFO order when false.

 move_to_end(*key*, *last=True*)

Shift an existing *key* over to either end of an ordered dictionary. The item lands at the right end when *last* is true (the default) or at the start when *last* is false. Raises [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) if the *key* does not exist:

```pycon
>>> d = OrderedDict.fromkeys('abcde')
>>> d.move_to_end('b')
>>> ''.join(d)
'acdeb'
>>> d.move_to_end('b', last=False)
>>> ''.join(d)
'bacde'

```

Added in version 3.2.

On top of the usual mapping methods, ordered dictionaries also handle reverse iteration through [`reversed()`](https://docs.python.org/3.14/library/functions.html#reversed).

Equality checks among `OrderedDict` objects honor order and amount roughly to `list(od1.items())==list(od2.items())`.

Equality checks between `OrderedDict` objects and other [`Mapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Mapping) objects ignore order, just like ordinary dictionaries do. That lets `OrderedDict` objects stand in anywhere a regular dictionary would be used.

Changed in version 3.5: For `OrderedDict`, its items, keys, and values [views](https://docs.python.org/3.14/glossary.html#term-dictionary-view) gained the ability to iterate in reverse via [`reversed()`](https://docs.python.org/3.14/library/functions.html#reversed).

Changed in version 3.6: Once [**PEP 468**](https://peps.python.org/pep-0468/) was adopted, ordering is preserved for keyword arguments handed to both the `OrderedDict` constructor and its [`update()`](https://docs.python.org/3.14/library/stdtypes.html#dict.update) method.

Changed in version 3.9: Added merge (`|`) and update (`|=`) operators, specified in [**PEP 584**](https://peps.python.org/pep-0584/).

[Subject index](INDEX.md) · [Previous](ordered-dictionary-class-contract.md) · [Continue](ordereddict-examples-and-recipes.md) · [Owning module, declaration or section: collections](collections-container-datatypes.md) · [Owning module, declaration or section: collections.OrderedDict; collections.OrderedDict; collections.OrderedDict](ordered-dictionary-class-contract.md) · [Owning module, declaration or section: `OrderedDict` objects](ordered-dictionary-class-contract.md)

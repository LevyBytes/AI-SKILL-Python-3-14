# types: `types.new_class()`, `types.prepare_class()`, `types.resolve_bases()`

### Dynamic Type Creation

 types.new_class(*name*, *bases=()*, *kwds=None*, *exec_body=None*)

Builds a class object dynamically by way of the suitable metaclass.

Its first three arguments amount to what a class definition header is built from: the class’s name, then the base classes given in order, then the keyword arguments (`metaclass` being one).

The *exec_body* argument is a callback tasked with filling in the newly built class namespace. It ought to take the class namespace as its only argument and write the class contents straight into that namespace. When no callback is given, the effect matches passing in `lambda ns: None`.

Added in version 3.3.

 types.prepare_class(*name*, *bases=()*, *kwds=None*)

Works out the suitable metaclass and builds the class namespace.

Its arguments amount to what a class definition header is built from: the class’s name, then the base classes given in order, then the keyword arguments (`metaclass` being one).

What it returns is a 3-tuple: `metaclass, namespace, kwds`

Here *metaclass* is the suitable metaclass, *namespace* is the prepared class namespace, and *kwds* is a refreshed copy of the *kwds* argument that was passed in, stripped of any `'metaclass'` entry. When no *kwds* argument is passed in, this comes out as an empty dict.

Added in version 3.3.

Changed in version 3.6: Within the tuple that comes back, the `namespace` element now defaults differently. Where the metaclass has no `__prepare__` method, a mapping that holds insertion order is what gets used.

See also

[Metaclasses](https://docs.python.org/3.14/reference/datamodel.html#metaclasses)

A complete account of the class creation process that these functions back

[**PEP 3115**](https://peps.python.org/pep-3115/) - Metaclasses in Python 3000

Brought in the `__prepare__` namespace hook

 types.resolve_bases(*bases*)

Resolve MRO entries dynamically following the specification in [**PEP 560**](https://peps.python.org/pep-0560/).

This function scans *bases* for items that are not instances of [`type`](https://docs.python.org/3.14/library/functions.html#type), and hands back a tuple in which every such object carrying an [`__mro_entries__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__mro_entries__) method is swapped for the unpacked result of invoking that method. Should a *bases* item be an instance of `type`, or lack an `__mro_entries__()` method, it carries over into the returned tuple untouched.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](types-dynamic-type-creation-and-names-for-built-in-types.md) · [Continue](types-get-original-bases.md) · [Owning module, declaration or section: types](types-dynamic-type-creation-and-names-for-built-in-types.md)

# stdtypes: `dict`

### Mapping Types — `dict`

A [mapping](https://docs.python.org/3.14/glossary.html#term-mapping) object pairs [hashable](https://docs.python.org/3.14/glossary.html#term-hashable) values with arbitrary objects. Mappings are mutable objects. As things stand there is just one standard mapping type, the *dictionary*. (Regarding other containers, consult the built-in `list`, `set`, and `tuple` classes along with the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module.)

The keys of a dictionary are *almost* any value at all. Values that are not [hashable](https://docs.python.org/3.14/glossary.html#term-hashable) — that is, values holding lists, dictionaries, or other mutable types (the kind compared by value rather than by object identity) — cannot serve as keys. Values that test equal (for instance `1`, `1.0`, and `True`) are interchangeable when indexing the same dictionary entry.

 *class *dict(***kwargs*)

 *class *dict(*mapping*, */*, ***kwargs*)

 *class *dict(*iterable*, */*, ***kwargs*)

Hand back a fresh dictionary set up from an optional positional argument plus a possibly empty collection of keyword arguments.

Dictionaries can be created by several means:

- Use a comma-separated list of `key: value` pairs within braces: `{'jack': 4098, 'sjoerd': 4127}` or `{4098: 'jack', 4127: 'sjoerd'}`

- Use a dict comprehension: `{}`, `{x: x ** 2 for x in range(10)}`

- Use the type constructor: `dict()`, `dict([('foo', 100), ('bar', 200)])`, `dict(foo=100, bar=200)`

When no positional argument is supplied, an empty dictionary results. When a positional argument is supplied and it provides a `keys()` method, a dictionary is built by invoking [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) on that argument for each key the method returns. Failing that, the positional argument must be an [iterable](https://docs.python.org/3.14/glossary.html#term-iterable) object. Each entry in the iterable must itself be an iterable holding exactly two elements. An entry's first element becomes a key in the new dictionary, while its second element becomes the matching value. Should a key show up more than once, the final value seen for that key becomes its value in the new dictionary.

When keyword arguments are supplied, those keyword arguments and their values get folded into the dictionary built from the positional argument. Should a key being added already exist, the keyword argument's value supplants the value drawn from the positional argument.

Dictionaries compare equal exactly when they hold the same `(key, value)` pairs (ordering aside). Order comparisons (‘<’, ‘<=’, ‘>=’, ‘>’) raise [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). To show dictionary creation alongside equality, every one of the examples below yields a dictionary equal to `{"one": 1, "two": 2, "three": 3}`:

[Subject index](INDEX.md) · [Previous](frozenset-copy-to-set-clear.md) · [Required continuation of the source contract](mapping-types-and-dict-construction.md)

# What’s New In Python 3.1 / PEP 372: Ordered Dictionaries — collections, configparser, json

### What’s New In Python 3.1

Author:

Raymond Hettinger

The features added in Python 3.1 relative to 3.0 are covered in this writeup. The 3.1 release shipped on June 27, 2009.

### PEP 372: Ordered Dictionaries

Ordinary Python dictionaries walk their key/value pairs in no particular order. Across several years, various authors built alternate versions that retain the sequence in which keys first arrived. Drawing on what those projects learned, the [`collections.OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict) class was added.

OrderedDict exposes essentially the same interface as an ordinary dict, yet it walks keys and values in a fixed sequence tied to when each key first arrived. Overwriting an existing entry with a fresh value keeps the original slot where it was. Removing an entry and then putting it back relocates it to the tail.

Several modules in the standard library can now take advantage of ordered dictionaries. By default, [`configparser`](https://docs.python.org/3.14/library/configparser.html#module-configparser) relies on them. As a result, config files may be loaded, edited, and saved again while keeping their original sequence. For [`collections.namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple), the *_asdict()* method hands back an ordered dictionary whose values follow the same order as the tuple positions behind them. Work on the [`json`](https://docs.python.org/3.14/library/json.html#module-json) module adds an *object_pairs_hook* so the decoder can assemble OrderedDicts. Third-party packages such as [PyYAML](https://pyyaml.org/) gained support too.

See also

[**PEP 372**](https://peps.python.org/pep-0372/) - Ordered Dictionaries

Armin Ronacher and Raymond Hettinger authored the PEP. Raymond Hettinger wrote the implementation.

Because an ordered dictionary keeps track of how entries were inserted, pairing it with a sort produces a sorted dictionary:

```python
>>> # regular unsorted dictionary
>>> d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}

>>> # dictionary sorted by key
>>> OrderedDict(sorted(d.items(), key=lambda t: t[0]))
OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

>>> # dictionary sorted by value
>>> OrderedDict(sorted(d.items(), key=lambda t: t[1]))
OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])

>>> # dictionary sorted by length of the key string
>>> OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])

```

These freshly sorted dictionaries hold onto their ordering as entries get removed. Adding fresh keys, however, tacks them onto the tail without preserving the sort.

[Subject index](INDEX.md) · [Next source section](pep-378-format-specifier-for-thousands-separator.md)

# What’s New in Python 2.7 / PEP 372: Adding an Ordered Dictionary to collections - json

The constructor of the [`json`](https://docs.python.org/3.14/library/json.html#module-json) module’s [`JSONDecoder`](https://docs.python.org/3.14/library/json.html#json.JSONDecoder) class picked up an *object_pairs_hook* parameter that lets the decoder build `OrderedDict` instances. Support was likewise added for third-party tools such as [PyYAML](https://pyyaml.org/).

See also

[**PEP 372**](https://peps.python.org/pep-0372/) - Adding an ordered dictionary to collections

PEP written by Armin Ronacher and Raymond Hettinger; implemented by Raymond Hettinger.

[Subject index](INDEX.md) · [Previous source section](pep-372-adding-an-ordered-dictionary-to-collections.md) · [Next source section](pep-378-format-specifier-for-thousands-separator.md) · [Release/subject declaration](the-future-for-python-2-x.md) · [Release/subject declaration](pep-372-adding-an-ordered-dictionary-to-collections.md)

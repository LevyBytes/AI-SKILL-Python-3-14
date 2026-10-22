# Containers and indexing

Open when checking Python definitions for containers and indexing.

## sequence

An iterable that allows efficient access to its elements via integer indices through the [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) special method and supplies a [`__len__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__len__) method giving back the sequence's length. A few built-in sequence types are [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple), and [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes). Observe that [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) likewise provides `__getitem__()` and `__len__()`, yet it counts as a mapping rather than a sequence, because its lookups rely on arbitrary hashable keys instead of integers.

The [`collections.abc.Sequence`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Sequence) abstract base class lays out a considerably fuller interface reaching past mere [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) and [`__len__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__len__), throwing in [`count()`](https://docs.python.org/3.14/library/stdtypes.html#sequence.count), [`index()`](https://docs.python.org/3.14/library/stdtypes.html#sequence.index), [`__contains__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__contains__), and [`__reversed__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__reversed__). Types fulfilling this broader interface can be registered outright via [`register()`](https://docs.python.org/3.14/library/abc.html#abc.ABCMeta.register). For fuller documentation on sequence methods in general, consult [Common Sequence Operations](https://docs.python.org/3.14/library/stdtypes.html#typesseq-common).

## list

One of Python's built-in sequences. Its name notwithstanding, it resembles an array from other languages more than a linked list, given that reaching elements is *O*(1).

## named tuple

The phrase “named tuple” covers any type or class that derives from tuple and whose indexable elements can additionally be reached through named attributes. That type or class might carry extra features besides.

A handful of built-in types are named tuples, among them the values handed back by [`time.localtime()`](https://docs.python.org/3.14/library/time.html#time.localtime) and [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat). One more example is [`sys.float_info`](https://docs.python.org/3.14/library/sys.html#sys.float_info):

```python
>>> sys.float_info[1]                   # indexed access
1024
>>> sys.float_info.max_exp              # named field access
1024
>>> isinstance(sys.float_info, tuple)   # kind of tuple
True

```

Certain named tuples are built-in types (like the examples just shown). On the other hand, a named tuple may come from an ordinary class definition that derives from [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) and that declares named fields. You can write such a class yourself, or obtain it by deriving from [`typing.NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple), or via the factory function [`collections.namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple). Those last approaches also tack on a few extra methods that hand-written or built-in named tuples might lack.

## mapping

A container object that allows arbitrary key lookups and provides the methods laid out in the [`collections.abc.Mapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Mapping) or [`collections.abc.MutableMapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.MutableMapping) [abstract base classes](https://docs.python.org/3.14/library/collections.abc.html#collections-abstract-base-classes). Some examples are [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), [`collections.defaultdict`](https://docs.python.org/3.14/library/collections.html#collections.defaultdict), [`collections.OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict) and [`collections.Counter`](https://docs.python.org/3.14/library/collections.html#collections.Counter).

## dictionary
An associative array, in which arbitrary keys map onto values. Any object furnishing [`__hash__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__) and [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__) methods may serve as a key. Perl refers to this structure as a hash.

## dictionary view

Whatever is returned by [`dict.keys()`](https://docs.python.org/3.14/library/stdtypes.html#dict.keys), [`dict.values()`](https://docs.python.org/3.14/library/stdtypes.html#dict.values), and [`dict.items()`](https://docs.python.org/3.14/library/stdtypes.html#dict.items) goes by the name dictionary views. Such a view stays dynamically tied to the dictionary's entries, so any change to the dictionary is mirrored in the view. Apply `list(dictview)` whenever you need the dictionary view turned into a complete list. See [Dictionary view objects](https://docs.python.org/3.14/library/stdtypes.html#dict-views).

## key

A value pinpointing an entry inside a mapping. See also subscript.

## index

A numeric value standing for an element's spot within a sequence.

Indexing in Python begins at zero. As an example, `things[0]` designates the *first* element of `things`; `things[1]` designates the second.

Under certain conditions Python permits negative indexes that count back from a sequence's end, as well as indexing by means of slices.

See also subscript.

## slice

An object of type [`slice`](https://docs.python.org/3.14/library/functions.html#slice), serving to denote a stretch of a sequence. A slice object comes into existence when you use the [slicing](https://docs.python.org/3.14/reference/expressions.html#slicings) form of [subscript notation](https://docs.python.org/3.14/reference/expressions.html#subscriptions), with colons set inside square brackets, as in `variable_name[1:3:5]`.

## subscript

The expression set inside the square brackets of a [subscription expression](https://docs.python.org/3.14/reference/expressions.html#subscriptions) - for example, the `3` in `items[3]`. It generally serves to pick out an element of a container. When a mapping is being subscripted it is also called a key, and when a sequence is being subscripted, an index.

[Glossary context index](INDEX.md).

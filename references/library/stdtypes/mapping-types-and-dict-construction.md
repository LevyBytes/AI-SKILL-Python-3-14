# Mapping Types and dict construction

```python
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> f = dict({'one': 1, 'three': 3}, two=2)
>>> a == b == c == d == e == f
True

```

Supplying keyword arguments the way the first line does is limited to keys that qualify as valid Python identifiers. For everything else, any valid key is acceptable.

Insertion order is retained by dictionaries. Be aware that reassigning a key leaves the ordering untouched. A key introduced after a deletion lands at the end.

```python
>>> d = {"one": 1, "two": 2, "three": 3, "four": 4}
>>> d
{'one': 1, 'two': 2, 'three': 3, 'four': 4}
>>> list(d)
['one', 'two', 'three', 'four']
>>> list(d.values())
[1, 2, 3, 4]
>>> d["one"] = 42
>>> d
{'one': 42, 'two': 2, 'three': 3, 'four': 4}
>>> del d["two"]
>>> d["two"] = None
>>> d
{'one': 42, 'three': 3, 'four': 4, 'two': None}

```

Changed in version 3.7: Insertion order for dictionaries is now a guarantee. CPython treated this as an implementation detail beginning with 3.6.

Dictionaries are [generic](https://docs.python.org/3.14/library/typing.html#generics) over a pair of types, denoting (in order) the types held by the dictionary's keys and its values.

The operations that follow are the ones dictionaries provide (and that custom mapping types should provide as well):

[Subject index](INDEX.md) · [Continue](dict-dict-dict-list-to-dict-dict-dict-pop.md) · [Owning module, declaration or section: Mapping Types and dict construction](dict-class-to-dict-class.md) · [Preceding source contract and version conditions](dict-class-to-dict-class.md)

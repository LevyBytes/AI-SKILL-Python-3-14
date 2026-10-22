# collections — `collections` — Container datatypes

### `collections` — Container datatypes

**Source code:** [Lib/collections/__init__.py](https://github.com/python/cpython/tree/3.14/Lib/collections/__init__.py)

---

The datatypes in this module are purpose-built containers that serve as alternatives to the general-purpose built-ins Python ships with, namely [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), and [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple).

| `namedtuple()` | factory function for creating tuple subclasses with named fields |
| --- | --- |
| `deque` | list-like container with fast appends and pops on either end |
| `ChainMap` | dict-like class for creating a single view of multiple mappings |
| `Counter` | dict subclass for counting hashable objects |
| `OrderedDict` | dict subclass that remembers the order entries were added |
| `defaultdict` | dict subclass that calls a factory function to supply missing values |
| `UserDict` | wrapper around dictionary objects for easier dict subclassing |
| `UserList` | wrapper around list objects for easier list subclassing |
| `UserString` | wrapper around string objects for easier string subclassing |

[Subject index](INDEX.md) · [Continue](collections-chainmap-class.md)

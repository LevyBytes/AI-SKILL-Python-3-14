# Thread safety for dict objects — Section introduction and initial examples

### Thread safety for dict objects

Building a dictionary by means of the [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) constructor is atomic where the argument is a `dict` or a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple). With the [`dict.fromkeys()`](https://docs.python.org/3.14/library/stdtypes.html#dict.fromkeys) method, the creation is atomic where the argument is a `dict`, `tuple`, [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) or [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset).

The operations and functions below are [lock-free](https://docs.python.org/3.14/glossary.html#term-lock-free) and [atomic](https://docs.python.org/3.14/glossary.html#term-atomic-operation).

```python
d[key]       # dict.__getitem__
d.get(key)   # dict.get
key in d     # dict.__contains__
len(d)       # dict.__len__

```

From this point onward, all remaining operations keep the [per-object lock](https://docs.python.org/3.14/glossary.html#term-per-object-lock) held.

Storing or deleting one item is fine to invoke across several threads and leaves the dictionary uncorrupted:

```python
d[key] = value        # write
del d[key]            # delete
d.pop(key)            # remove and return
d.popitem()           # remove and return last item
d.setdefault(key, v)  # insert if missing

```

These operations might compare keys through [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__), which is capable of running arbitrary Python code. While such a comparison runs, another thread may edit the dictionary. For built-in types such as [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`int`](https://docs.python.org/3.14/library/functions.html#int), and [`float`](https://docs.python.org/3.14/library/functions.html#float), which carry a `__eq__()` written in C, the underlying lock stays held throughout the comparison and so there is nothing to worry about.

The operations below build new objects and keep the [per-object lock](https://docs.python.org/3.14/glossary.html#term-per-object-lock) held for the whole operation:

```python
d.copy()      # returns a shallow copy of the dictionary
d | other     # merges two dicts into a new dict
d.keys()      # returns a new dict_keys view object
d.values()    # returns a new dict_values view object
d.items()     # returns a new dict_items view object

```

The [`clear()`](https://docs.python.org/3.14/library/stdtypes.html#dict.clear) method keeps the lock held throughout. No other thread can witness elements while they are being dropped.

The operations below lock the pair of dictionaries. With [`update()`](https://docs.python.org/3.14/library/stdtypes.html#dict.update) and `|=`, that is true only where the other operand is a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) using the standard dict iterator (yet not subclasses that replace iteration). For equality testing, it covers `dict` together with its subclasses:

```python
d.update(other_dict)  # both locked when other_dict is a dict
d |= other_dict       # both locked when other_dict is a dict
d == other_dict       # both locked for dict and subclasses

```

Every comparison operation also compares values through [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__), and so for non-built-in types the lock can be let go during the comparison.

[`fromkeys()`](https://docs.python.org/3.14/library/stdtypes.html#dict.fromkeys) locks both the fresh dictionary and the iterable where the iterable is exactly a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), or [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) (subclasses excluded):

```python
dict.fromkeys(a_dict)      # locks both
dict.fromkeys(a_set)       # locks both
dict.fromkeys(a_frozenset) # locks both

```

Where the update comes from a non-dict iterable, only the destination dictionary gets locked. Another thread can edit the iterable concurrently:

```python
d.update(iterable)        # iterable is not a dict: only d locked
d |= iterable             # iterable is not a dict: only d locked
dict.fromkeys(iterable)   # iterable is not a dict/set/frozenset: only result locked

```

Operations spanning multiple accesses, iteration included, are never atomic:

[Subject index](INDEX.md) · [Previous](thread-safety-for-list-objects.md) · [Continue](dictionary-nonatomic-operations.md)

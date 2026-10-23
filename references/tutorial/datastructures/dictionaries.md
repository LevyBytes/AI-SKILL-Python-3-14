# 5.5. Dictionaries

### 5.5. Dictionaries

The *dictionary* is one more handy data type baked into Python (refer to [Mapping Types - dict](https://docs.python.org/3.14/library/stdtypes.html#typesmapping)). Some other languages call dictionaries "associative memories" or "associative arrays". Whereas sequences get indexed by a span of numbers, dictionaries get indexed by *keys*, and a key may be any immutable type; strings and numbers always qualify as keys. Tuples qualify as keys provided they hold nothing but strings, numbers, or tuples; once a tuple holds any mutable object whether directly or by some nested path, it stops being usable as a key. Lists can't serve as keys, because a list can be altered in place via index assignments, slice assignments, or methods such as [`append()`](https://docs.python.org/3.14/library/stdtypes.html#list.append) and [`extend()`](https://docs.python.org/3.14/library/stdtypes.html#list.extend).

The cleanest mental picture of a dictionary is a collection of *key: value* pairs, carrying the rule that every key stays unique (inside a single dictionary). One pair of braces makes an empty dictionary: `{}`. Dropping a comma-separated run of key:value pairs between the braces seeds the dictionary with those initial key:value pairs; this matches the form in which dictionaries get printed on output.

A dictionary's chief operations are saving a value under some key and pulling the value back out given that key. Deleting a key:value pair with `del` is possible as well. Should you save under a key already taken, whatever old value that key held gets discarded.

Pulling a value for a key that doesn't exist by subscripting (`d[key]`) raises a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError). To sidestep this error while reaching for a key that may not exist, reach instead for the [`get()`](https://docs.python.org/3.14/library/stdtypes.html#dict.get) method, which hands back `None` (or some default value you name) whenever the key is absent from the dictionary.

Running `list(d)` over a dictionary yields a list of every key the dictionary uses, ordered by insertion (and should you want it sorted, simply switch to `sorted(d)`). To find out whether one particular key sits in the dictionary, use the [`in`](https://docs.python.org/3.14/reference/expressions.html#in) keyword.

A short example using a dictionary follows here:

```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> tel['irv']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'irv'
>>> print(tel.get('irv'))
None
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False

```

Straight from sequences of key-value pairs, the [`dict()`](https://docs.python.org/3.14/library/stdtypes.html#dict) constructor assembles dictionaries:

```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}

```

On top of that, dict comprehensions let you build dictionaries out of arbitrary key and value expressions:

```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}

```

Whenever the keys happen to be plain strings, supplying the pairs through keyword arguments can prove simpler:

```python
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}

```

[Subject index](INDEX.md) · [Previous source section](sets.md) · [Following source section](dictionary-enumerated-zipped-and-reversed-iteration.md)

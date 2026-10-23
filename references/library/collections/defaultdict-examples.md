# collections`defaultdict` Examples

### `defaultdict` Examples

By picking [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) as the `default_factory`, you can readily collect a stream of key-value pairs into a dictionary whose values are lists:

```python
>>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d = defaultdict(list)
>>> for k, v in s:
...     d[k].append(v)
...
>>> sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

```

The very first time a given key shows up, it has no entry in the mapping yet; so one is generated on the fly by calling the `default_factory` function, which yields an empty [`list`](https://docs.python.org/3.14/library/stdtypes.html#list). The [`list.append()`](https://docs.python.org/3.14/library/stdtypes.html#list.append) call then tacks the value onto that fresh list. On subsequent encounters of the same key, the lookup runs as usual (handing back that key’s list) and `list.append()` appends one more value to it. This approach is both shorter and quicker than the comparable one based on [`dict.setdefault()`](https://docs.python.org/3.14/library/stdtypes.html#dict.setdefault):

```python
>>> d = {}
>>> for k, v in s:
...     d.setdefault(k, []).append(v)
...
>>> sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

```

Choosing [`int`](https://docs.python.org/3.14/library/functions.html#int) as the `default_factory` turns the `defaultdict` into a handy counter (much like a bag or multiset elsewhere):

```python
>>> s = 'mississippi'
>>> d = defaultdict(int)
>>> for k in s:
...     d[k] += 1
...
>>> sorted(d.items())
[('i', 4), ('m', 1), ('p', 2), ('s', 4)]

```

The first time a letter appears, the mapping lacks it, so the `default_factory` function invokes [`int()`](https://docs.python.org/3.14/library/functions.html#int) to deliver an initial count of zero. Each following increment accumulates the tally for that letter.

The [`int()`](https://docs.python.org/3.14/library/functions.html#int) function, always yielding zero, is merely one instance of the broader category of constant functions. To produce constant functions more quickly and with greater flexibility, reach for a lambda function, which can return whatever constant you like (zero is just one option):

```python
>>> def constant_factory(value):
...     return lambda: value
...
>>> d = defaultdict(constant_factory('<missing>'))
>>> d.update(name='John', action='ran')
>>> '%(name)s %(action)s to %(object)s' % d
'John ran to <missing>'

```

Choosing [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) as the `default_factory` makes the `defaultdict` handy for assembling a dictionary whose values are sets:

```python
>>> s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
>>> d = defaultdict(set)
>>> for k, v in s:
...     d[k].add(v)
...
>>> sorted(d.items())
[('blue', {2, 4}), ('red', {1, 3})]

```

[Subject index](INDEX.md) · [Previous](collections-defaultdict-missing.md) · [Continue](collections-namedtuple.md) · [Owning module, declaration or section: collections](collections-container-datatypes.md)

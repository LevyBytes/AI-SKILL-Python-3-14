# How do I copy an object in Python?

### How do I copy an object in Python?

As a rule, reach for [`copy.copy()`](https://docs.python.org/3.14/library/copy.html#copy.copy) or [`copy.deepcopy()`](https://docs.python.org/3.14/library/copy.html#copy.deepcopy) in the general situation. Copying isn't possible for every object, but it works for most.

A handful of objects copy with less effort. Dictionaries provide a [`copy()`](https://docs.python.org/3.14/library/stdtypes.html#dict.copy) method:

```python
newdict = olddict.copy()

```

Sequences can be copied by slicing:

```python
new_l = l[:]

```

[Subject index](INDEX.md)

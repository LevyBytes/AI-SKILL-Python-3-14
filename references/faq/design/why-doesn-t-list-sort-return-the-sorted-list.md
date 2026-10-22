# Why doesn't list.sort() return the sorted list?

### Why doesn't list.sort() return the sorted list?

Where performance is a concern, copying the list merely to sort it would be wasteful. For that reason, [`list.sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort) sorts the list in place. To keep that fact in mind, it refrains from returning the sorted list. That way, you won't be tricked into accidentally overwriting a list when you actually want a sorted copy yet also need to retain the unsorted version.

When a fresh list is what you are after, reach for the built-in [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted) function instead. It accepts any iterable you supply, assembles a new list from it, orders that list, and hands it back. The snippet below, for instance, walks a dictionary’s keys in sorted order:

```python
for key in sorted(mydict):
    ...  # do whatever with mydict[key]...

```

[Subject index](INDEX.md)

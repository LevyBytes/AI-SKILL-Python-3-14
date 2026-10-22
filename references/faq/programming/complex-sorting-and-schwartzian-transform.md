# I want to do a complicated sort: can you do a Schwartzian Transform in Python?

### I want to do a complicated sort: can you do a Schwartzian Transform in Python?

This idiom, credited to Randal Schwartz from the Perl world, orders a list’s items according to a measure that pairs each item with its “sort value”. With Python, supply the `key` argument to the [`list.sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort) method:

```python
Isorted = L[:]
Isorted.sort(key=lambda s: int(s[10:15]))

```

[Subject index](INDEX.md)

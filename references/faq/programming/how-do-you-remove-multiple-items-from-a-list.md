# How do you remove multiple items from a list?

### How do you remove multiple items from a list?

Just as with stripping duplicates, explicitly iterating in reverse while applying a delete condition is one option. Even so, it is simpler and faster to rely on slice replacement together with an implicit or explicit forward iteration. Here are three variations:

```python
mylist[:] = filter(keep_function, mylist)
mylist[:] = (x for x in mylist if keep_condition)
mylist[:] = [x for x in mylist if keep_condition]

```

Of these, the list comprehension is likely the fastest.

[Subject index](INDEX.md)

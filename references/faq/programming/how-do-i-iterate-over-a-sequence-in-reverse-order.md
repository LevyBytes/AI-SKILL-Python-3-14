# How do I iterate over a sequence in reverse order?

### How do I iterate over a sequence in reverse order?

Reach for the [`reversed()`](https://docs.python.org/3.14/library/functions.html#reversed) built-in function:

```python
for x in reversed(sequence):
    ...  # do something with x ...

```

This leaves your original sequence alone, building instead a fresh copy in reversed order for you to iterate across.

[Subject index](INDEX.md)

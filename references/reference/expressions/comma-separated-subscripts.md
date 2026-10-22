# 6.3.2.2. Comma-separated subscripts

#### 6.3.2.2. Comma-separated subscripts

The subscript may instead be supplied as two or more expressions or slices set off by commas:

```python
# continuing with the SubscriptionDemo instance defined above:
>>> demo[1, 2, 3]
subscripted with: (1, 2, 3)
>>> demo[1:2, 3]
subscripted with: (slice(1, 2, None), 3)

```

This pattern is widely used alongside numerical libraries for slicing multi-dimensional data. Here the interpreter assembles a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) out of the outcomes of the expressions or slices, then passes that tuple to the [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) or [`__class_getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__class_getitem__) [special method](https://docs.python.org/3.14/glossary.html#term-special-method), exactly as above.

The subscript may furthermore be supplied as a lone expression or slice trailed by a comma, which designates a one-element tuple:

```python
>>> demo['spam',]
subscripted with: ('spam',)

```

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](primaries.md) · [Owning language section](subscriptions-and-slicings.md) · [Previous source section](slicings.md) · [Following source section](starred-subscriptions.md)

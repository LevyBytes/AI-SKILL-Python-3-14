# 6.3.2.3. ?Starred? subscriptions

#### 6.3.2.3. ?Starred? subscriptions

Added in version 3.11: Expressions in *tuple_slices* may be starred. See [**PEP 646**](https://peps.python.org/pep-0646/).

The subscript is also permitted to hold a starred expression. When it does, the interpreter unpacks the outcome into a tuple and passes that tuple to [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) or [`__class_getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__class_getitem__):

```python
# continuing with the SubscriptionDemo instance defined above:
>>> demo[*range(10)]
subscripted with: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

```

You can mix starred expressions together with slices and ordinary comma-separated expressions:

```python
>>> demo['a', 'b', *range(3), 'c']
subscripted with: ('a', 'b', 0, 1, 2, 'c')

```

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](primaries.md) · [Owning language section](subscriptions-and-slicings.md) · [Previous source section](comma-separated-subscripts.md) · [SubscriptionDemo class and demo instance setup](subscriptions-and-slicings.md) · [Following source section](formal-subscription-grammar.md)

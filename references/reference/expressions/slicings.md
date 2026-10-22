# 6.3.2.1. Slicings

#### 6.3.2.1. Slicings

A richer variant of subscription, called *slicing*, is frequently used to pull out a section of a [sequence](https://docs.python.org/3.14/reference/datamodel.html#datamodel-sequences). With this variant, the subscript is a [slice](https://docs.python.org/3.14/glossary.html#term-slice): as many as three expressions divided by colons. You may leave out any of those expressions, but every slice needs at least one colon:

```python
>>> number_names = ['zero', 'one', 'two', 'three', 'four', 'five']
>>> number_names[1:3]
['one', 'two']
>>> number_names[1:]
['one', 'two', 'three', 'four', 'five']
>>> number_names[:3]
['zero', 'one', 'two']
>>> number_names[:]
['zero', 'one', 'two', 'three', 'four', 'five']
>>> number_names[::2]
['zero', 'two', 'four']
>>> number_names[:-3]
['zero', 'one', 'two']
>>> del number_names[4:]
>>> number_names
['zero', 'one', 'two', 'three']

```

As a slice is evaluated, the interpreter builds a [`slice`](https://docs.python.org/3.14/library/functions.html#slice) object whose [`start`](https://docs.python.org/3.14/library/functions.html#slice.start), [`stop`](https://docs.python.org/3.14/library/functions.html#slice.stop) and [`step`](https://docs.python.org/3.14/library/functions.html#slice.step) attributes hold, in turn, the outcomes of the expressions sitting between the colons. Whichever expression is left out evaluates to [`None`](https://docs.python.org/3.14/library/constants.html#None). That `slice` object is then handed to the [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) or [`__class_getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__class_getitem__) [special method](https://docs.python.org/3.14/glossary.html#term-special-method), exactly as above.

```python
# continuing with the SubscriptionDemo instance defined above:
>>> demo[2:3]
subscripted with: slice(2, 3, None)
>>> demo[::'spam']
subscripted with: slice(None, None, 'spam')

```

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](primaries.md) · [Owning language section](subscriptions-and-slicings.md) · [Previous source section](subscriptions-and-slicings.md) · [Following source section](comma-separated-subscripts.md)

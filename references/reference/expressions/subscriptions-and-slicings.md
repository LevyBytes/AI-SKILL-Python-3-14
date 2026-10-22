# 6.3.2. Subscriptions and slicings

### 6.3.2. Subscriptions and slicings

You normally reach for the *subscription* syntax to pick one element out of a [container](https://docs.python.org/3.14/reference/datamodel.html#sequence-types) ? say, to pull a value out of a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict):

```python
>>> digits_by_name = {'one': 1, 'two': 2}
>>> digits_by_name['two']  # Subscripting a dictionary using the key 'two'
2

```

Within the subscription syntax, the object getting subscribed ? a primary ? is trailed by a *subscript* enclosed in square brackets. At its simplest, that subscript is just one expression.

The subscript goes by different names according to the type of the object being subscribed: a [key](https://docs.python.org/3.14/glossary.html#term-key) (for mappings), an [index](https://docs.python.org/3.14/glossary.html#term-index) (for sequences), or a *type argument* (for [generic types](https://docs.python.org/3.14/glossary.html#term-generic-type)). As far as syntax goes, all of these are interchangeable:

```python
>>> colors = ['red', 'blue', 'green', 'black']
>>> colors[3]  # Subscripting a list using the index 3
'black'

>>> list[str]  # Parameterizing the list type using the type argument str
list[str]

```

When the program runs, the interpreter evaluates both the primary and the subscript, then invokes the primary's [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) or [`__class_getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__class_getitem__) [special method](https://docs.python.org/3.14/glossary.html#term-special-method), handing the subscript across as the argument. For further detail on which one of those methods is invoked, refer to [__class_getitem__ versus __getitem__](https://docs.python.org/3.14/reference/datamodel.html#classgetitem-versus-getitem).

To demonstrate subscription in action, we can write a custom object that supplies [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) and prints the subscript's value:

```python
>>> class SubscriptionDemo:
...     def __getitem__(self, key):
...         print(f'subscripted with: {key!r}')
...
>>> demo = SubscriptionDemo()
>>> demo[1]
subscripted with: 1
>>> demo['a' * 3]
subscripted with: 'aaa'

```

Consult the [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) documentation to learn how the built-in types deal with subscription.

You can additionally use subscriptions as targets in [assignment](https://docs.python.org/3.14/reference/simple_stmts.html#assignment) or [deletion](https://docs.python.org/3.14/reference/simple_stmts.html#del) statements. When that happens, the interpreter invokes the subscripted object's [`__setitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setitem__) or [`__delitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__delitem__) [special method](https://docs.python.org/3.14/glossary.html#term-special-method), respectively, rather than [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__).

```python
>>> colors = ['red', 'blue', 'green', 'black']
>>> colors[3] = 'white'  # Setting item at index
>>> colors
['red', 'blue', 'green', 'white']
>>> del colors[3]  # Deleting item at index 3
>>> colors
['red', 'blue', 'green']

```

Each of the advanced *subscript* forms described in the sections below works for assignment and deletion as well.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](primaries.md) · [SubscriptionDemo subscription examples](starred-subscriptions.md) · [Previous source section](attribute-references.md) · [Following source section](slicings.md)

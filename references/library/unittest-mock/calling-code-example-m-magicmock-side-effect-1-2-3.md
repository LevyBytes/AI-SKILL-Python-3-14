# unittest.mock - Calling - Code example: >>> m = MagicMock(side_effect=[1, 2, 3])

```python
>>> m = MagicMock(side_effect=[1, 2, 3])
>>> m()
1
>>> m()
2
>>> m()
3
>>> m()
Traceback (most recent call last):
  ...
StopIteration

```

Whenever any items of the iterable happen to be exceptions, they get raised rather than returned:

```python
>>> iterable = (33, ValueError, 66)
>>> m = MagicMock(side_effect=iterable)
>>> m()
33
>>> m()
Traceback (most recent call last):
 ...
ValueError
>>> m()
66

```

[Subject index](INDEX.md) · [Previous](calling-section-introduction-and-initial-examples.md) · [Continue](deleting-attributes.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: Calling](calling-section-introduction-and-initial-examples.md)

# Sorted unique iteration and filtered copies

When you want to iterate over a sequence in sorted order, the [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted) function gives back a fresh sorted list without disturbing the original.

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear

```

Applying [`set()`](https://docs.python.org/3.14/library/stdtypes.html#set) to a sequence drops the duplicate elements. Pairing [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted) with `set()` over a sequence forms the idiomatic way to iterate across that sequence's unique elements in sorted order.

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear

```

The urge to mutate a list mid-iteration crops up now and then; even so, building a fresh list is frequently the simpler and safer route.

```python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]

```

[Subject index](INDEX.md) · [Previous source section](dictionary-enumerated-zipped-and-reversed-iteration.md) · [Following source section](more-on-conditions.md) · [Related tutorial example and explanation](dictionary-enumerated-zipped-and-reversed-iteration.md)

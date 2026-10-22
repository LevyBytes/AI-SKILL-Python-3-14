# enumerate positions and sorted output

[`enumerate(iter, start=0)`](https://docs.python.org/3.14/library/functions.html#enumerate) numbers off the entries in the iterable and hands back 2-tuples pairing the running count (beginning at *start*) with each entry.

```python
>>> for item in enumerate(['subject', 'verb', 'object']):
...     print(item)
(0, 'subject')
(1, 'verb')
(2, 'object')

```

A common application of [`enumerate()`](https://docs.python.org/3.14/library/functions.html#enumerate) is iterating over a list while noting the positions where particular conditions hold:

```python
f = open('data.txt', 'r')
for i, line in enumerate(f):
    if line.strip() == '':
        print('Blank line at line #%i' % i)

```

[`sorted(iterable, key=None, reverse=False)`](https://docs.python.org/3.14/library/functions.html#sorted) gathers every item from the iterable into a list, orders that list, and hands back the sorted outcome. The *key* and *reverse* parameters are forwarded straight to the [`sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort) method of the list it builds.

```python
>>> import random
>>> # Generate 8 random numbers between [0, 10000)
>>> rand_list = random.sample(range(10000), 8)
>>> rand_list
[769, 7953, 9828, 6431, 8442, 9878, 6213, 2207]
>>> sorted(rand_list)
[769, 2207, 6213, 6431, 7953, 8442, 9828, 9878]
>>> sorted(rand_list, reverse=True)
[9878, 9828, 8442, 7953, 6431, 6213, 2207, 769]

```

(If you want a fuller treatment of sorting, refer to the [Sorting Techniques](https://docs.python.org/3.14/howto/sorting.html#sortinghowto).)

[Subject index](INDEX.md) · [map and filter transformations](map-and-filter-transformations.md) · [any, all and zip consumption rules](any-all-and-zip-consumption-rules.md) · [Previous source context](map-and-filter-transformations.md) · [Following source context](any-all-and-zip-consumption-rules.md)

# heapq — Basic Examples

### Basic Examples

You can build a [heapsort](https://en.wikipedia.org/wiki/Heapsort) by pushing every value onto a heap and then popping the smallest values back off one by one:

```python
>>> def heapsort(iterable):
...     h = []
...     for value in iterable:
...         heappush(h, value)
...     return [heappop(h) for i in range(len(h))]
...
>>> heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```

This resembles `sorted(iterable)`, yet, in contrast to [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted), the present implementation is not stable.

A heap's elements may be tuples. That comes in handy when you want to attach comparison values (task priorities, say) to the main record you're keeping track of:

```python
>>> h = []
>>> heappush(h, (5, 'write code'))
>>> heappush(h, (7, 'release product'))
>>> heappush(h, (1, 'write spec'))
>>> heappush(h, (3, 'create tests'))
>>> heappop(h)
(1, 'write spec')

```

[Subject index](INDEX.md) · [Previous](heapq-heapreplace-max-to-heapq-nsmallest.md) · [Continue](other-applications.md) · [Owning module, declaration or section: heapq](heapq-heapify-to-heapq-heappushpop-max.md)

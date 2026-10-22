# heapq: `heapq.heapreplace_max()`, `heapq.merge()`, `heapq.nlargest()`, `heapq.nsmallest()`

heapq.heapreplace_max(*heap*, *item*)

Remove the largest entry from the max-heap *heap* and return it, while also adding the new *item*. The max-heap's size stays the same. An empty max-heap triggers [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError).

The returned value can be smaller than the *item* you supplied. See the matching `heapreplace()` function for fuller notes on usage.

Added in version 3.14.

Three more general-purpose functions built on heaps round out the module.

 heapq.merge(**iterables*, *key=None*, *reverse=False*)

Combine several already-sorted inputs into one sorted stream (for instance, interleaving timestamped records drawn from several log files). Hands back an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) over the sorted values.

It behaves like `sorted(itertools.chain(*iterables))`, except it yields an iterable, never loads everything into memory at once, and presumes each input stream is already in order (smallest to largest).

It accepts two optional arguments, both of which have to be passed as keyword arguments.

*key* names a [key function](https://docs.python.org/3.14/glossary.html#term-key-function) taking one argument, applied to pull a comparison key out of each input element. The default, `None`, compares the elements as they are.

*reverse* takes a boolean. With it set to `True`, the inputs are combined as though every comparison ran backwards. For results like `sorted(itertools.chain(*iterables), reverse=True)`, every iterable has to be ordered from largest down to smallest.

Changed in version 3.5: Added the optional *key* and *reverse* parameters.

 heapq.nlargest(*n*, *iterable*, *key=None*)

Hand back a list holding the *n* largest entries out of the dataset given by *iterable*. When supplied, *key* names a one-argument function applied to draw a comparison key from each element of *iterable* (for instance, `key=str.lower`). Equivalent to: `sorted(iterable, key=key, reverse=True)[:n]`.

 heapq.nsmallest(*n*, *iterable*, *key=None*)

Hand back a list holding the *n* smallest entries out of the dataset given by *iterable*. When supplied, *key* names a one-argument function applied to draw a comparison key from each element of *iterable* (for instance, `key=str.lower`). Equivalent to: `sorted(iterable, key=key)[:n]`.

Those last two functions work best when *n* is small. With larger *n*, the [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted) function is the more efficient choice. And for `n==1`, the built-in [`min()`](https://docs.python.org/3.14/library/functions.html#min) and [`max()`](https://docs.python.org/3.14/library/functions.html#max) functions do better still. When you expect to call these functions repeatedly, it pays to convert the iterable into a real heap first.

[Subject index](INDEX.md) · [Previous](heapq-heapify-to-heapq-heappushpop-max.md) · [Continue](basic-examples.md) · [Owning module, declaration or section: heapq](heapq-heapify-to-heapq-heappushpop-max.md)

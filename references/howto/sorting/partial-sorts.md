# Partial Sorts

### Partial Sorts

Certain programs only ever need a portion of the data put in order. For those cases the standard library offers several tools that spare you the cost of a complete sort:

- [`min()`](https://docs.python.org/3.14/library/functions.html#min) and [`max()`](https://docs.python.org/3.14/library/functions.html#max) hand back the smallest and the largest value in turn. Each sweeps through the input just once and uses next to no extra memory along the way.

- [`heapq.nsmallest()`](https://docs.python.org/3.14/library/heapq.html#heapq.nsmallest) and [`heapq.nlargest()`](https://docs.python.org/3.14/library/heapq.html#heapq.nlargest) deliver the *n* smallest and the *n* largest values respectively. They too pass over the data only once, holding just *n* items in memory at any moment. Whenever *n* stays small next to the count of inputs, they perform vastly fewer comparisons than a full sort would.

- [`heapq.heappush()`](https://docs.python.org/3.14/library/heapq.html#heapq.heappush) and [`heapq.heappop()`](https://docs.python.org/3.14/library/heapq.html#heapq.heappop) build and uphold a partly ordered data structure that always parks the smallest element at position `0`. They are well suited to building priority queues, the sort of structure routinely relied upon for scheduling tasks.

[Subject index](INDEX.md) · [Previous source context](odds-and-ends.md)

# heapq - Other Applications

### Other Applications

A [median](https://en.wikipedia.org/wiki/Median) measures the central tendency of a collection of numbers. Where outliers skew a distribution, the median holds up as a steadier estimate than the average (the arithmetic mean). A running median is an [online algorithm](https://en.wikipedia.org/wiki/Online_algorithm) that keeps updating as fresh data flows in.

You can implement a running median efficiently by keeping two heaps in balance — a max-heap holding values at or under the midpoint, and a min-heap holding values above it. While the two heaps are equal in size, the new median is the mean of the two heap tops; otherwise the median sits at the top of whichever heap is larger:

```python
def running_median(iterable):
    "Yields the cumulative median of values seen so far."

    lo = []  # max-heap
    hi = []  # min-heap (same size as or one smaller than lo)

    for x in iterable:
        if len(lo) == len(hi):
            heappush_max(lo, heappushpop(hi, x))
            yield lo[0]
        else:
            heappush(hi, heappushpop_max(lo, x))
            yield (lo[0] + hi[0]) / 2

```

For example:

```python
>>> list(running_median([5.0, 9.0, 4.0, 12.0, 8.0, 9.0]))
[5.0, 7.0, 5.0, 7.0, 8.0, 8.5]

```

[Subject index](INDEX.md) · [Previous](basic-examples.md) · [Continue](priority-queue-implementation-notes.md) · [Owning module, declaration or section: heapq](heapq-heapify-to-heapq-heappushpop-max.md)

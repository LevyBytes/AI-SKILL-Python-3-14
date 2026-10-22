# statistics: `statistics.median_grouped()`, `statistics.mode()`, `statistics.multimode()`

statistics.median_grouped(*data*, *interval=1.0*)

Estimates the median for numeric data that has been [grouped or binned](https://en.wikipedia.org/wiki/Data_binning) about the midpoints of back-to-back intervals of fixed width.

Here *data* can be any iterable of numeric data where each value sits exactly at a bin's midpoint. There has to be at least one value.

The *interval* is each bin's width.

To illustrate, demographic figures might be condensed into back-to-back ten-year age groups, each one represented by the intervals' 5-year midpoints:

```pycon
>>> from collections import Counter
>>> demographics = Counter({
...    25: 172,   # 20 to 30 years old
...    35: 484,   # 30 to 40 years old
...    45: 387,   # 40 to 50 years old
...    55:  22,   # 50 to 60 years old
...    65:   6,   # 60 to 70 years old
... })
...

```

Out of the 1071 member cohort, the 50th percentile (median) is the 536th person, who lands in the 30 to 40 year old age group.

Ordinary `median()` would treat everyone in the tricenarian age group as exactly 35 years old. It is more defensible to suppose those 484 members spread evenly across 30 to 40. To do that, we call `median_grouped()`:

```pycon
>>> data = list(demographics.elements())
>>> median(data)
35
>>> round(median_grouped(data, interval=10), 1)
37.5

```

Ensuring that the data points sit at exact multiples of *interval* apart is the caller's job. That spacing is critical to a correct result. The function performs no check of this precondition.

Inputs may be of any numeric type convertible to a float at the interpolation step.

 statistics.mode(*data*)

Return the single value occurring most often in discrete or nominal *data*. Where it exists, the mode is the most representative value and indicates central location.

When several modes share the top frequency, the first one met in the *data* comes back. To get the smallest or largest of them instead, use `min(multimode(data))` or `max(multimode(data))`. A `StatisticsError` is raised when the input *data* is empty.

`mode` presumes discrete data and hands back one value. That matches the conventional school treatment of the mode:

```pycon
>>> mode([1, 1, 2, 3, 3, 3, 3, 4])
3

```

What sets the mode apart is that it alone among this package's statistics also works on nominal (non-numeric) data:

```pycon
>>> mode(["red", "blue", "blue", "red", "green", "red", "red"])
'red'

```

Inputs are only supported if they are hashable. For type [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), think about casting to [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset). For type [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), think about casting to [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple). For mixed or nested inputs, you might use this slower quadratic algorithm, which leans only on equality tests: `max(data, key=data.count)`.

Changed in version 3.8: Now copes with multimodal datasets by handing back the first mode it meets. Previously, it raised `StatisticsError` whenever more than one mode turned up.

 statistics.multimode(*data*)

Return a list of the values that occur most often, ordered by where each was first met in the *data*. More than one result comes back when there are several modes, and an empty list comes back when the *data* is empty:

```pycon
>>> multimode('aabbbbccddddeeffffgg')
['b', 'd', 'f']
>>> multimode('')
[]

```

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](statistics-kde-random-to-statistics-median-high.md) · [Continue](statistics-pstdev-to-statistics-stdev.md) · [Owning module, declaration or section: statistics](statistics-mathematical-statistics-functions.md) · [Owning module, declaration or section: Function details](statistics-mean-to-statistics-geometric-mean.md)

# statistics: `statistics.kde_random()`, `statistics.median()`, `statistics.median_low()`, `statistics.median_high()`

statistics.kde_random(*data*, *h*, *kernel='normal'*, ***, *seed=None*)

Return a function that draws a random pick from the estimated probability density function that `kde(data, h, kernel)` produces.

Supplying a *seed* makes the picks reproducible. Going forward, the values could shift a little as sharper kernel inverse CDF estimates land. A seed can be an integer, float, str, or bytes.

A `StatisticsError` is raised whenever the *data* sequence is empty.

Picking up the `kde()` example, `kde_random()` lets us draw fresh random picks from an estimated probability density function:

```python
>>> data = [-2.1, -1.3, -0.4, 1.9, 5.1, 6.2]
>>> rand = kde_random(data, h=1.5, seed=8675309)
>>> new_selections = [rand() for i in range(10)]
>>> [round(x, 1) for x in new_selections]
[0.7, 6.2, 1.2, 6.9, 7.0, 1.8, 2.5, -0.5, -1.8, 5.6]

```

Added in version 3.13.

 statistics.median(*data*)

Return the median (middle value) of numeric data via the usual “mean of middle two” approach. A `StatisticsError` is raised when *data* is empty. Here *data* may be a sequence or iterable.

As a sturdy gauge of central location, the median is little swayed by outliers. With an odd count of data points, the central data point comes back:

```pycon
>>> median([1, 3, 5])
3

```

With an even count of data points, the median is interpolated by averaging the two central values:

```pycon
>>> median([1, 3, 5, 7])
4.0

```

This fits cases where your data is discrete and a median that may not be a real data point doesn't bother you.

Where the data is ordinal (it permits order operations) yet not numeric (it lacks addition), reach for `median_low()` or `median_high()` instead.

 statistics.median_low(*data*)

Return the low median of numeric data. A `StatisticsError` is raised when *data* is empty. Here *data* may be a sequence or iterable.

The low median always belongs to the data set. With an odd count of data points, the central value comes back. With an even count, the lesser of the two central values comes back.

```pycon
>>> median_low([1, 3, 5])
3
>>> median_low([1, 3, 5, 7])
3

```

Reach for the low median when your data are discrete and you want the median to be a real data point rather than an interpolated one.

 statistics.median_high(*data*)

Return the high median of data. A `StatisticsError` is raised when *data* is empty. Here *data* may be a sequence or iterable.

The high median always belongs to the data set. With an odd count of data points, the central value comes back. With an even count, the greater of the two central values comes back.

```pycon
>>> median_high([1, 3, 5])
3
>>> median_high([1, 3, 5, 7])
5

```

Reach for the high median when your data are discrete and you want the median to be a real data point rather than an interpolated one.

[Subject index](INDEX.md) · [Previous](statistics-harmonic-mean-to-statistics-kde.md) · [Continue](statistics-median-grouped-to-statistics-multimode.md) · [Owning module, declaration or section: statistics](statistics-mathematical-statistics-functions.md) · [Owning module, declaration or section: Function details](statistics-mean-to-statistics-geometric-mean.md)

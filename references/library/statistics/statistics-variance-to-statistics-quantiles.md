# statistics: `statistics.variance()`, `statistics.quantiles()`

statistics.variance(*data*, *xbar=None*)

Return the sample variance of *data*, an iterable holding at least two real-valued numbers. Variance — the second moment about the mean — measures how variable (spread out or dispersed) the data is. When variance is large the data is spread out; when it is small the data sits tightly clustered around the mean.

When the optional second argument *xbar* is supplied, it ought to be the *sample* mean of *data*. When it is absent or `None` (the default), the mean gets computed for you.

Use this function when your data is a sample drawn from a population. To find variance across the whole population, see `pvariance()`.

A `StatisticsError` is raised when *data* holds fewer than two values.

Examples:

```pycon
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> variance(data)
1.3720238095238095

```

Should you already have your data's sample mean, hand it in as the optional second argument *xbar* to skip recomputing it:

```pycon
>>> m = mean(data)
>>> variance(data, m)
1.3720238095238095

```

This function makes no effort to confirm that the value you supplied as *xbar* is the actual mean. Feeding arbitrary values for *xbar* may produce invalid or impossible results.

Decimal and Fraction values work too:

```pycon
>>> from decimal import Decimal as D
>>> variance([D("27.5"), D("30.25"), D("30.25"), D("34.5"), D("41.75")])
Decimal('31.01875')

>>> from fractions import Fraction as F
>>> variance([F(1, 6), F(1, 2), F(5, 3)])
Fraction(67, 108)

```

Note

This is the sample variance s² carrying Bessel’s correction, which also goes by variance with N-1 degrees of freedom. As long as the data points are representative — say, independent plus identically distributed — you can expect the result to estimate the genuine population variance without bias.

If by some means you know the actual population mean μ, you should hand it to the `pvariance()` function via the *mu* parameter to obtain a sample's variance.

 statistics.quantiles(*data*, ***, *n=4*, *method='exclusive'*)

Split *data* into *n* continuous intervals carrying equal probability. Returns a list of `n - 1` cut points that separate those intervals.

Use *n* of 4 for quartiles (the default). Use *n* of 10 for deciles. Use *n* of 100 for percentiles, which yields the 99 cut points dividing *data* into 100 groups of equal size. A `StatisticsError` is raised when *n* is not least 1.

Here *data* may be any iterable that holds sample data. To get meaningful results, *data* should contain more data points than *n*. A `StatisticsError` is raised when there is not at least one data point.

Each cut point is linearly interpolated between its two closest data points. For instance, when a cut point sits one-third of the way between the two sample values `100` and `112`, that cut-point comes out to `104`.

You can vary the *method* used to compute quantiles based on whether the *data* takes in or leaves out the population's lowest and highest possible values.

By default the *method* is “exclusive”, meant for data sampled from a population that may contain values more extreme than those seen in the samples. The fraction of the population sitting below the *i-th* of *m* sorted data points works out to `i / (m + 1)`. With nine sample values, the method orders them and hands out these percentiles: 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%.

Choosing the *method* “inclusive” serves to describe population data or samples known to take in the population's most extreme values. The smallest value in *data* counts as the 0th percentile and the largest counts as the 100th percentile. The fraction of the population sitting below the *i-th* of *m* sorted data points works out to `(i - 1) / (m - 1)`. With 11 sample values, the method orders them and hands out these percentiles: 0%, 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 100%.

```pycon
# Decile cut points for empirically sampled data
>>> data = [105, 129, 87, 86, 111, 111, 89, 81, 108, 92, 110,
...         100, 75, 105, 103, 109, 76, 119, 99, 91, 103, 129,
...         106, 101, 84, 111, 74, 87, 86, 103, 103, 106, 86,
...         111, 75, 87, 102, 121, 111, 88, 89, 101, 106, 95,
...         103, 107, 101, 81, 109, 104]
>>> [round(q, 1) for q in quantiles(data, n=10)]
[81.0, 86.2, 89.0, 99.4, 102.5, 103.6, 106.0, 109.8, 111.0]

```

Added in version 3.8.

Changed in version 3.13: An input that carries just a single data point no longer triggers an exception. This lets quantile estimates accrue one sample point at a time, sharpening little by little with each fresh data point.

[Subject index](INDEX.md) · [Previous](statistics-pstdev-to-statistics-stdev.md) · [Continue](statistics-covariance-to-statistics-correlation.md) · [Owning module, declaration or section: statistics](statistics-mathematical-statistics-functions.md) · [Owning module, declaration or section: Function details](statistics-mean-to-statistics-geometric-mean.md)

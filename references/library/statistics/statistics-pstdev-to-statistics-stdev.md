# statistics: `statistics.pstdev()`, `statistics.pvariance()`, `statistics.stdev()`

statistics.pstdev(*data*, *mu=None*)

Return the population standard deviation (the square root of the population variance). Consult `pvariance()` for the arguments and further specifics.

```pycon
>>> pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
0.986893273527251

```

 statistics.pvariance(*data*, *mu=None*)

Return the population variance of *data*, a non-empty sequence or iterable holding real-valued numbers. Variance — the second moment about the mean — measures how variable (spread out or dispersed) the data is. When variance is large the data is spread out; when it is small the data sits tightly clustered around the mean.

When the optional second argument *mu* is supplied, it ought to be the *population* mean of the *data*. It also lets you compute the second moment around some point other than the mean. When it is absent or `None` (the default), the arithmetic mean gets computed for you.

Use this function to find the variance across the whole population. When estimating variance from a sample, `variance()` is generally the better pick.

A `StatisticsError` is raised when *data* is empty.

Examples:

```pycon
>>> data = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25]
>>> pvariance(data)
1.25

```

Should you already have your data's mean, hand it in as the optional second argument *mu* to skip recomputing it:

```pycon
>>> mu = mean(data)
>>> pvariance(data, mu)
1.25

```

Decimals and Fractions work too:

```pycon
>>> from decimal import Decimal as D
>>> pvariance([D("27.5"), D("30.25"), D("30.25"), D("34.5"), D("41.75")])
Decimal('24.815')

>>> from fractions import Fraction as F
>>> pvariance([F(1, 4), F(5, 4), F(1, 2)])
Fraction(13, 72)

```

Note

Given the whole population, this returns the population variance σ². Given a sample instead, it returns the biased sample variance s², which also goes by variance with N degrees of freedom.

If by some means you know the true population mean μ, you can use this function to find a sample's variance by passing that known population mean as the second argument. As long as the data points form a random sample of the population, the result is an unbiased estimate of the population variance.

 statistics.stdev(*data*, *xbar=None*)

Return the sample standard deviation (the square root of the sample variance). Consult `variance()` for the arguments and further specifics.

```pycon
>>> stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
1.0810874155219827

```

[Subject index](INDEX.md) · [Previous](statistics-median-grouped-to-statistics-multimode.md) · [Continue](statistics-variance-to-statistics-quantiles.md) · [Owning module, declaration or section: statistics](statistics-mathematical-statistics-functions.md) · [Owning module, declaration or section: Function details](statistics-mean-to-statistics-geometric-mean.md)

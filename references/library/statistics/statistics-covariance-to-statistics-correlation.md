# statistics: `statistics.covariance()`, `statistics.correlation()`

statistics.covariance(*x*, *y*, */*)

Return the sample covariance of the two inputs *x* and *y*. Covariance gauges how jointly variable two inputs are.

Each input has to be the same length (no fewer than two); otherwise a `StatisticsError` is raised.

Examples:

```pycon
>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> y = [1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> covariance(x, y)
0.75
>>> z = [9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> covariance(x, z)
-7.5
>>> covariance(z, x)
-7.5

```

Added in version 3.10.

 statistics.correlation(*x*, *y*, */*, ***, *method='linear'*)

[Subject index](INDEX.md) · [Previous](statistics-variance-to-statistics-quantiles.md) · [Owning module, declaration or section: statistics](statistics-mathematical-statistics-functions.md) · [Owning module, declaration or section: Function details](statistics-mean-to-statistics-geometric-mean.md) · [Required continuation of the source contract](function-details.md)

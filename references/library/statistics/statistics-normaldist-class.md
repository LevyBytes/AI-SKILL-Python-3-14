# statistics: `statistics.NormalDist`

### `NormalDist` objects

`NormalDist` serves as an instrument for building and working with normal distributions of a [random variable](http://www.stat.yale.edu/Courses/1997-98/101/ranvar.htm). As a class, it bundles the mean together with the standard deviation of measured data into one object.

The [Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem) gives rise to normal distributions, which see broad use throughout statistics.

 *class *statistics.NormalDist(*mu=0.0*, *sigma=1.0*)

Produces a fresh *NormalDist* object in which *mu* stands for the [arithmetic mean](https://en.wikipedia.org/wiki/Arithmetic_mean) and *sigma* stands for the [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation).

A negative *sigma* triggers a `StatisticsError`.

[Subject index](INDEX.md) · [Previous](statistics-statisticserror.md) · [Continue](normal-distribution-samples-and-quantiles.md) · [Owning module, declaration or section: statistics](statistics-mathematical-statistics-functions.md)

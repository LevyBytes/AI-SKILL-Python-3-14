# statistics.NormalDist: `from_samples()`, `samples()`, `pdf()`, `cdf()`, `inv_cdf()`, `overlap()`, `quantiles()`

mean

A property, read-only, giving the [arithmetic mean](https://en.wikipedia.org/wiki/Arithmetic_mean) of the normal distribution.

 median

A property, read-only, giving the [median](https://en.wikipedia.org/wiki/Median) of the normal distribution.

 mode

A property, read-only, giving the [mode](https://en.wikipedia.org/wiki/Mode_(statistics)) of the normal distribution.

 stdev

A property, read-only, giving the [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) of the normal distribution.

 variance

A property, read-only, giving the [variance](https://en.wikipedia.org/wiki/Variance) of the normal distribution. It comes to the standard deviation squared.

 *classmethod *from_samples(*data*)

Builds a normal distribution instance whose *mu* and *sigma* parameters are derived from the *data* through `fmean()` and `stdev()`.

Any [iterable](https://docs.python.org/3.14/glossary.html#term-iterable) works as the *data*, provided its values can be coerced into the [`float`](https://docs.python.org/3.14/library/functions.html#float) type. Should *data* hold fewer than two elements, a `StatisticsError` is raised, since one point is enough to estimate a central value but estimating dispersion needs two.

 samples(*n*, ***, *seed=None*)

Produces *n* random draws for the given mean and standard deviation, handing back a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) of [`float`](https://docs.python.org/3.14/library/functions.html#float) values.

Supplying a *seed* spins up a fresh instance of the underlying random number generator. That helps when you want repeatable output, even amid multi-threading.

Changed in version 3.13.

Moved to a quicker algorithm. To recreate the samples that earlier releases produced, fall back on [`random.seed()`](https://docs.python.org/3.14/library/random.html#random.seed) together with [`random.gauss()`](https://docs.python.org/3.14/library/random.html#random.gauss).

 pdf(*x*)

By way of a [probability density function (pdf)](https://en.wikipedia.org/wiki/Probability_density_function), works out the relative likelihood of a random variable *X* landing close to the supplied value *x*. In formal terms, this is the limit of the ratio `P(x <= X < x+dx) / dx` as *dx* shrinks toward zero.

That relative likelihood comes from dividing the probability of a sample falling within a thin band by the band's width (which is why we say “density”). Because the figure is measured against other points, it can exceed `1.0`.

 cdf(*x*)

By way of a [cumulative distribution function (cdf)](https://en.wikipedia.org/wiki/Cumulative_distribution_function), works out the probability of a random variable *X* coming out at *x* or below. In formal notation, this reads `P(X <= x)`.

 inv_cdf(*p*)

Works out the inverse cumulative distribution function — the same thing as the [quantile function](https://en.wikipedia.org/wiki/Quantile_function) or the [percent-point](https://web.archive.org/web/20190203145224/https://www.statisticshowto.datasciencecentral.com/inverse-distribution-function/) function. In formal notation, this reads `x : P(X <= x) = p`.

Locates the value *x* of the random variable *X* for which the chance of the variable being at or under that value matches the supplied probability *p*.

 overlap(*other*)

Gauges how closely a pair of normal probability distributions agree. Hands back a number from 0.0 through 1.0 that reports [the overlapping area for the two probability density functions](https://www.rasch.org/rmt/rmt101r.htm).

 quantiles(*n=4*)

Splits the normal distribution into *n* adjacent intervals that each carry equal probability. Hands back a list holding the (n - 1) cut points that divide those intervals.

Use *n* equal to 4 for quartiles (that being the default), 10 for deciles, and 100 for percentiles, where the latter yields the 99 cut points that partition the normal distribution into 100 equally sized groups.

[Subject index](INDEX.md) · [Previous](statistics-normaldist-class.md) · [Continue](statistics-normaldist-zscore.md) · [Owning module, declaration or section: statistics](statistics-mathematical-statistics-functions.md) · [Owning module, declaration or section: statistics.NormalDist](statistics-normaldist-class.md) · [Owning module, declaration or section: `NormalDist` objects](statistics-normaldist-class.md)

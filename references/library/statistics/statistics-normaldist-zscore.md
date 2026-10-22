# statistics.NormalDist: `zscore()`

zscore(*x*)

Works out the [Standard Score](https://www.statisticshowto.com/probability-and-statistics/z-score/) that expresses *x* as a count of standard deviations sitting above or below the normal distribution's mean: `(x - mean) / stdev`.

Added in version 3.9.

A `NormalDist` instance permits being added to, subtracted from, multiplied, and divided by a constant. Such operations serve to translate and scale the distribution. Here is an example:

```pycon
>>> temperature_february = NormalDist(5, 2.5)             # Celsius
>>> temperature_february * (9/5) + 32                     # Fahrenheit
NormalDist(mu=41.0, sigma=4.5)

```

You cannot divide a constant by a `NormalDist` instance, since the outcome would not follow a normal distribution.

Because normal distributions emerge from the additive influence of independent variables, you may [add and subtract two independent normally distributed random variables](https://en.wikipedia.org/wiki/Sum_of_normally_distributed_random_variables) that are held as `NormalDist` instances. Here is an example:

```pycon
>>> birth_weights = NormalDist.from_samples([2.5, 3.1, 2.1, 2.4, 2.7, 3.5])
>>> drug_effects = NormalDist(0.4, 0.15)
>>> combined = birth_weights + drug_effects
>>> round(combined.mean, 1)
3.1
>>> round(combined.stdev, 1)
0.5

```

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](normal-distribution-samples-and-quantiles.md) · [Continue](classic-probability-problems.md) · [Owning module, declaration or section: statistics](statistics-mathematical-statistics-functions.md) · [Owning module, declaration or section: statistics.NormalDist](statistics-normaldist-class.md) · [Owning module, declaration or section: `NormalDist` objects](statistics-normaldist-class.md)

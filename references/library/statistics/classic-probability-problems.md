# statistics - Classic probability problems

### Examples and Recipes

### Classic probability problems

Classic probability problems yield easily to `NormalDist`.

Take, for instance, [historical data for SAT exams](https://nces.ed.gov/programs/digest/d17/tables/dt17_226.40.asp) indicating that scores follow a normal distribution with a mean of 1060 and a standard deviation of 195, work out (rounded to the nearest whole number) the share of students whose test scores land between 1100 and 1200, like so:

```pycon
>>> sat = NormalDist(1060, 195)
>>> fraction = sat.cdf(1200 + 0.5) - sat.cdf(1100 - 0.5)
>>> round(fraction * 100.0, 1)
18.4

```

Work out the [quartiles](https://en.wikipedia.org/wiki/Quartile) along with the [deciles](https://en.wikipedia.org/wiki/Decile) of the SAT scores:

```pycon
>>> list(map(round, sat.quantiles()))
[928, 1060, 1192]
>>> list(map(round, sat.quantiles(n=10)))
[810, 896, 958, 1011, 1060, 1109, 1162, 1224, 1310]

```

[Subject index](INDEX.md) · [Continue](monte-carlo-inputs-for-simulations.md) · [Owning module, declaration or section: statistics](statistics-mathematical-statistics-functions.md)

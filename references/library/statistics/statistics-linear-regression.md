# statistics: `statistics.linear_regression()`

statistics.linear_regression(*x*, *y*, */*, ***, *proportional=False*)

Hands back the slope plus intercept of [simple linear regression](https://en.wikipedia.org/wiki/Simple_linear_regression) parameters, fitted by ordinary least squares. Simple linear regression frames how an independent variable *x* ties to a dependent variable *y* via the following linear function:

>

`y = slope * x + intercept + noise`

in which `slope` and `intercept` are the regression parameters being fitted, while `noise` stands for the portion of the data's spread that the linear regression leaves unaccounted for (it equals the gap between the predicted and the actual values of the dependent variable).

The two inputs have to share a length (at least two values each), and the independent variable *x* must not be constant; if not, a `StatisticsError` is raised.

As an illustration, we can draw on the [release dates of the Monty Python films](https://en.wikipedia.org/wiki/Monty_Python#Films) to forecast how many Monty Python films would have accumulated by 2019 had the group sustained that rhythm.

```pycon
>>> year = [1971, 1975, 1979, 1982, 1983]
>>> films_total = [1, 2, 3, 4, 5]
>>> slope, intercept = linear_regression(year, films_total)
>>> round(slope * 2019 + intercept)
16

```

Setting *proportional* to true tells the function to treat the dependent variable *y* as directly proportional to the independent variable *x*. The fit then uses a line through the origin. Because the *intercept* is fixed at 0.0, the underlying linear function reduces to:

>

`y = slope * x + noise`

Picking up the example from `correlation()`, we check how well a model built on the major planets forecasts the orbital distances of dwarf planets:

```pycon
>>> model = linear_regression(period_squared, dist_cubed, proportional=True)
>>> slope = model.slope

>>> # Dwarf planets:   Pluto,  Eris,    Makemake, Haumea, Ceres
>>> orbital_periods = [90_560, 204_199, 111_845, 103_410, 1_680]  # days
>>> predicted_dist = [math.cbrt(slope * (p * p)) for p in orbital_periods]
>>> list(map(round, predicted_dist))
[5912, 10166, 6806, 6459, 414]

>>> [5_906, 10_152, 6_796, 6_450, 414]  # actual distance in million km
[5906, 10152, 6796, 6450, 414]

```

Added in version 3.10.

Changed in version 3.11: Added support for *proportional*.

[Subject index](INDEX.md) · [Previous](function-details.md) · [Continue](statistics-statisticserror.md) · [Owning module, declaration or section: statistics](statistics-mathematical-statistics-functions.md) · [Owning module, declaration or section: Function details](statistics-mean-to-statistics-geometric-mean.md)

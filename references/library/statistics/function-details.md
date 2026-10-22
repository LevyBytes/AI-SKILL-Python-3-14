# statistics: Pearson and ranked correlation behavior

Yields the [Pearson’s correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) computed from a pair of inputs. The Pearson’s correlation coefficient *r* falls somewhere from -1 up to +1. It captures both how strong a linear relationship is and which way that relationship points.

Should *method* be “ranked”, the function instead derives the [Spearman’s rank correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient) from a pair of inputs. Here each value gives way to its rank, with ties averaged so identical values land on one shared rank. The coefficient you get back gauges how strong a monotonic relationship is.

The Spearman’s correlation coefficient suits ordinal data, as well as continuous data that fails to satisfy the linear-proportion condition demanded by Pearson’s correlation coefficient.

The two inputs have to share a length (at least two values each) and must not be constant; if either rule breaks, `StatisticsError` is raised.

An illustration drawing on [Kepler’s laws of planetary motion](https://en.wikipedia.org/wiki/Kepler's_laws_of_planetary_motion):

```pycon
>>> # Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and  Neptune
>>> orbital_period = [88, 225, 365, 687, 4331, 10_756, 30_687, 60_190]    # days
>>> dist_from_sun = [58, 108, 150, 228, 778, 1_400, 2_900, 4_500] # million km

>>> # Show that a perfect monotonic relationship exists
>>> correlation(orbital_period, dist_from_sun, method='ranked')
1.0

>>> # Observe that a linear relationship is imperfect
>>> round(correlation(orbital_period, dist_from_sun), 4)
0.9882

>>> # Demonstrate Kepler's third law: There is a linear correlation
>>> # between the square of the orbital period and the cube of the
>>> # distance from the sun.
>>> period_squared = [p * p for p in orbital_period]
>>> dist_cubed = [d * d * d for d in dist_from_sun]
>>> round(correlation(period_squared, dist_cubed), 4)
1.0

```

Added in version 3.10.

Changed in version 3.12: The Spearman’s rank correlation coefficient became supported.

[Subject index](INDEX.md) · [Continue](statistics-linear-regression.md) · [Owning module, declaration or section: statistics](statistics-mathematical-statistics-functions.md) · [Owning module, declaration or section: Function details](statistics-mean-to-statistics-geometric-mean.md) · [Owning module, declaration or section: statistics.correlation](statistics-covariance-to-statistics-correlation.md) · [Preceding source contract and version conditions](statistics-covariance-to-statistics-correlation.md)

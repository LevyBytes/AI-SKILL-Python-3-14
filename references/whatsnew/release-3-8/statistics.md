# What’s New In Python 3.8 / statistics - statistics

### statistics

A new [`statistics.fmean()`](https://docs.python.org/3.14/library/statistics.html#statistics.fmean) arrived as a quicker, floating-point counterpart to [`statistics.mean()`](https://docs.python.org/3.14/library/statistics.html#statistics.mean). (Contributed by Raymond Hettinger and Steven D’Aprano in [bpo-35904](https://bugs.python.org/issue?@action=redirect&bpo=35904).)

A new [`statistics.geometric_mean()`](https://docs.python.org/3.14/library/statistics.html#statistics.geometric_mean) arrived (Contributed by Raymond Hettinger in [bpo-27181](https://bugs.python.org/issue?@action=redirect&bpo=27181).)

A new [`statistics.multimode()`](https://docs.python.org/3.14/library/statistics.html#statistics.multimode) arrived, yielding a list holding the values that occur most often. (Contributed by Raymond Hettinger in [bpo-35892](https://bugs.python.org/issue?@action=redirect&bpo=35892).)

A new [`statistics.quantiles()`](https://docs.python.org/3.14/library/statistics.html#statistics.quantiles) arrived, splitting data or a distribution into equiprobable intervals (for instance quartiles, deciles, or percentiles). (Contributed by Raymond Hettinger in [bpo-36546](https://bugs.python.org/issue?@action=redirect&bpo=36546).)

A new [`statistics.NormalDist`](https://docs.python.org/3.14/library/statistics.html#statistics.NormalDist) arrived, a utility for building and working with normal distributions of a random variable. (Contributed by Raymond Hettinger in [bpo-36018](https://bugs.python.org/issue?@action=redirect&bpo=36018).)

```python
>>> temperature_feb = NormalDist.from_samples([4, 12, -3, 2, 7, 14])
>>> temperature_feb.mean
6.0
>>> temperature_feb.stdev
6.356099432828281

>>> temperature_feb.cdf(3)            # Chance of being under 3 degrees
0.3184678262814532
>>> # Relative chance of being 7 degrees versus 10 degrees
>>> temperature_feb.pdf(7) / temperature_feb.pdf(10)
1.2039930378537762

>>> el_niño = NormalDist(4, 2.5)
>>> temperature_feb += el_niño        # Add in a climate effect
>>> temperature_feb
NormalDist(mu=10.0, sigma=6.830080526611674)

>>> temperature_feb * (9/5) + 32      # Convert to Fahrenheit
NormalDist(mu=50.0, sigma=12.294144947901014)
>>> temperature_feb.samples(3)        # Generate random samples
[7.672102882379219, 12.000027119750287, 4.647488369766392]

```

[Subject index](INDEX.md) · [Previous source section](ssl.md) · [Next source section](sys.md) · [Release/subject declaration](assignment-expressions.md)

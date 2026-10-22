# statistics — Approximating binomial distributions

### Approximating binomial distributions

A normal distribution can stand in for a [Binomial distributions](https://mathworld.wolfram.com/BinomialDistribution.html) whenever the sample is large and a single trial succeeds with a probability close to 50%.

Picture, say, an open source conference drawing 750 attendees, with two rooms that each hold 500 people. One room hosts a Python talk and the other a Ruby talk. At earlier conferences, 65% of those attending favored the Python sessions. If the crowd's preferences hold steady, how likely is it that the Python room stays under its capacity?

```pycon
>>> n = 750             # Sample size
>>> p = 0.65            # Preference for Python
>>> q = 1.0 - p         # Preference for Ruby
>>> k = 500             # Room capacity

>>> # Approximation using the cumulative normal distribution
>>> from math import sqrt
>>> round(NormalDist(mu=n*p, sigma=sqrt(n*p*q)).cdf(k + 0.5), 4)
0.8402

>>> # Exact solution using the cumulative binomial distribution
>>> from math import comb, fsum
>>> round(fsum(comb(n, r) * p**r * q**(n-r) for r in range(k+1)), 4)
0.8402

>>> # Approximation using a simulation
>>> from random import seed, binomialvariate
>>> seed(8675309)
>>> mean(binomialvariate(n, p) <= k for i in range(10_000))
0.8406

```

[Subject index](INDEX.md) · [Previous](monte-carlo-inputs-for-simulations.md) · [Continue](naive-bayesian-classifier.md) · [Owning module, declaration or section: statistics](statistics-mathematical-statistics-functions.md)

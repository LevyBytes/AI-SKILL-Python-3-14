# random — Examples — Section introduction and initial examples

### Examples

Basic examples:

```python
>>> random()                          # Random float:  0.0 <= x < 1.0
0.37444887175646646

>>> uniform(2.5, 10.0)                # Random float:  2.5 <= x <= 10.0
3.1800146073117523

>>> expovariate(1 / 5)                # Interval between arrivals averaging 5 seconds
5.148957571865031

>>> randrange(10)                     # Integer from 0 to 9 inclusive
7

>>> randrange(0, 101, 2)              # Even integer from 0 to 100 inclusive
26

>>> choice(['win', 'lose', 'draw'])   # Single random element from a sequence
'draw'

>>> deck = 'ace two three four'.split()
>>> shuffle(deck)                     # Shuffle a list
>>> deck
['four', 'two', 'ace', 'three']

>>> sample([10, 20, 30, 40, 50], k=4) # Four samples without replacement
[40, 10, 50, 30]

```

Simulations:

```python
>>> # Six roulette wheel spins (weighted sampling with replacement)
>>> choices(['red', 'black', 'green'], [18, 18, 2], k=6)
['red', 'green', 'black', 'black', 'red', 'black']

>>> # Deal 20 cards without replacement from a deck
>>> # of 52 playing cards, and determine the proportion of cards
>>> # with a ten-value:  ten, jack, queen, or king.
>>> deal = sample(['tens', 'low cards'], counts=[16, 36], k=20)
>>> deal.count('tens') / 20
0.15

>>> # Estimate the probability of getting 5 or more heads from 7 spins
>>> # of a biased coin that settles on heads 60% of the time.
>>> sum(binomialvariate(n=7, p=0.6) >= 5 for i in range(10_000)) / 10_000
0.4169

>>> # Probability of the median of 5 samples being in middle two quartiles
>>> def trial():
...     return 2_500 <= sorted(choices(range(10_000), k=5))[2] < 7_500
...
>>> sum(trial() for i in range(10_000)) / 10_000
0.7958

```

An illustration of [statistical bootstrapping](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)) that resamples with replacement so as to gauge a confidence interval around a sample's mean:

```python
# https://www.thoughtco.com/example-of-bootstrapping-3126155
from statistics import fmean as mean
from random import choices

data = [41, 50, 29, 37, 81, 30, 73, 63, 20, 35, 68, 22, 60, 31, 95]
means = sorted(mean(choices(data, k=len(data))) for i in range(100))
print(f'The sample mean of {mean(data):.1f} has a 90% confidence '
      f'interval from {means[5]:.1f} to {means[94]:.1f}')

```

An illustration of a [resampling permutation test](https://en.wikipedia.org/wiki/Resampling_(statistics)#Permutation_tests) used to gauge the statistical significance, or [p-value](https://en.wikipedia.org/wiki/P-value), of a measured gap between how a drug and a placebo perform:

[Subject index](INDEX.md) · [Previous](notes-on-reproducibility.md) · [Continue](examples-code-example-from-statistics-import-fmean-as-mean.md) · [Owning module, declaration or section: random](random-generate-pseudo-random-numbers.md)

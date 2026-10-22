# random — Functions for sequences

### Functions for sequences

 random.choice(*seq*)

Hand back a random member of the non-empty sequence *seq*. When *seq* holds nothing, [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) is raised.

 random.choices(*population*, *weights=None*, ***, *cum_weights=None*, *k=1*)

Hand back a list of length *k* whose elements are drawn from the *population* with replacement. When the *population* is empty, this raises [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError).

When you pass a *weights* sequence, the picks follow the relative weights. As an alternative, when you provide a *cum_weights* sequence, the picks follow the cumulative weights (which you might compute with [`itertools.accumulate()`](https://docs.python.org/3.14/library/itertools.html#itertools.accumulate)). To illustrate, the relative weights `[10, 5, 30, 5]` correspond to the cumulative weights `[10, 15, 45, 50]`. Under the hood, relative weights become cumulative weights before any pick is made, so passing the cumulative weights directly avoids that step.

When you give neither *weights* nor *cum_weights*, picks happen with equal probability. When a weights sequence is provided, its length must equal the length of the *population* sequence. Passing both *weights* and *cum_weights* is a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

Any numeric type that works alongside the [`float`](https://docs.python.org/3.14/library/functions.html#float) values from `random()` is acceptable for *weights* or *cum_weights* (so integers, floats, and fractions qualify, but decimals do not). Weights are taken to be non-negative and finite. Should every weight be zero, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) results.

Given the same seed, calling `choices()` with uniform weighting will generally yield a sequence unlike one built from repeated `choice()` calls. For internal consistency and speed, `choices()` relies on floating-point arithmetic. By contrast, `choice()` falls back on integer arithmetic across repeated picks so that round-off error does not introduce minor biases.

Added in version 3.6.

Changed in version 3.9: A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised when every weight equals zero.

 random.shuffle(*x*)

Shuffle the sequence *x* in place.

When you need to shuffle an immutable sequence and get back a fresh shuffled list, reach for `sample(x, k=len(x))` instead.

Bear in mind that even when `len(x)` is small, the count of permutations of *x* can soon exceed the period of most random number generators. The consequence is that the bulk of permutations of a lengthy sequence are unreachable. As an example, the longest sequence that stays inside the period of the Mersenne Twister random number generator has length 2080.

Changed in version 3.11: The optional *random* parameter was dropped.

 random.sample(*population*, *k*, ***, *counts=None*)

Hand back a list of length *k* containing distinct elements picked from the population sequence. This serves random sampling without replacement.

The call yields a fresh list holding elements of the population while the original population stays untouched. Because the returned list follows selection order, every sub-slice is itself a valid random sample as well. That property lets the raffle winners (the sample) be split into a grand prize winner and runners-up (the subslices).

The population's members are not required to be [hashable](https://docs.python.org/3.14/glossary.html#term-hashable) or distinct. When the population includes duplicates, each appearance can be picked separately in the sample.

You can list duplicate elements individually or use the optional keyword-only *counts* parameter. As an example, `sample(['red', 'blue'], counts=[4, 2], k=5)` is equivalent to `sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)`.

When you want a sample taken from a span of integers, pass a [`range()`](https://docs.python.org/3.14/library/stdtypes.html#range) object as the argument. Sampling from a sizable population this way is exceptionally fast and frugal with space: `sample(range(10000000), k=60)`.

When the requested sample size exceeds the population size, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

Changed in version 3.9: The *counts* parameter was introduced.

Changed in version 3.11: The *population* is now required to be a sequence. Sets are no longer turned into lists for you.

[Subject index](INDEX.md) · [Previous](random-randrange-to-random-getrandbits.md) · [Continue](random-binomialvariate.md) · [Owning module, declaration or section: random](random-generate-pseudo-random-numbers.md)

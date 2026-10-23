# What's New In Python 3.2 / itertools - itertools, random

### itertools

- A fresh [`accumulate()`](https://docs.python.org/3.14/library/itertools.html#itertools.accumulate) function, patterned after APL's *scan* operator together with Numpy's *accumulate* function, now lives in the [`itertools`](https://docs.python.org/3.14/library/itertools.html#module-itertools) module:

```python
>>> from itertools import accumulate
>>> list(accumulate([8, 2, 50]))
[8, 10, 60]

```

```python
>>> prob_dist = [0.1, 0.4, 0.2, 0.3]
>>> list(accumulate(prob_dist))      # cumulative probability distribution
[0.1, 0.5, 0.7, 1.0]

```

To see [`accumulate()`](https://docs.python.org/3.14/library/itertools.html#itertools.accumulate) put to work, look at the [examples for the random module](https://docs.python.org/3.14/library/random.html#random-examples).

(Contributed by Raymond Hettinger and incorporating design suggestions from Mark Dickinson.)

[Subject index](INDEX.md) · [Previous source section](functools.md) · [Next source section](collections.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)

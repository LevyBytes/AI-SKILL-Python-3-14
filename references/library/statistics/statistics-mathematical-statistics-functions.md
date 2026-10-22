# statistics — `statistics` — Mathematical statistics functions

### `statistics` — Mathematical statistics functions

Added in version 3.4.

**Source code:** [Lib/statistics.py](https://github.com/python/cpython/tree/3.14/Lib/statistics.py)

---

The functions in this module compute mathematical statistics over numeric ([`Real`](https://docs.python.org/3.14/library/numbers.html#numbers.Real)-valued) datasets.

This module does not try to rival third-party libraries like [NumPy](https://numpy.org) or [SciPy](https://scipy.org/), nor commercial, full-featured statistics suites built for working statisticians such as Minitab, SAS and Matlab. Its target is roughly the capability of graphing and scientific calculators.

Except where stated otherwise, these functions accept [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) and [`Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction). How they behave with other types — inside the numeric tower or not — is currently unsupported. Likewise, a collection mixing several types yields undefined, implementation-dependent results. When your input mixes types, one workaround is [`map()`](https://docs.python.org/3.14/library/functions.html#map) to normalize everything, as in: `map(float, input_data)`.

Certain datasets encode missing entries as `NaN` (not a number) values. Because NaNs follow odd comparison rules, they trigger surprising or undefined behavior in any statistics function that orders the data or tallies how often values appear. The impacted functions are `median()`, `median_low()`, `median_high()`, `median_grouped()`, `mode()`, `multimode()`, and `quantiles()`. Remove the `NaN` values first, before you invoke these functions:

```python
>>> from statistics import median
>>> from math import isnan
>>> from itertools import filterfalse

>>> data = [20.7, float('NaN'),19.2, 18.3, float('NaN'), 14.4]
>>> sorted(data)  # This has surprising behavior
[20.7, nan, 14.4, 18.3, 19.2, nan]
>>> median(data)  # This result is unexpected
16.35

>>> sum(map(isnan, data))    # Number of missing values
2
>>> clean = list(filterfalse(isnan, data))  # Strip NaN values
>>> clean
[20.7, 19.2, 18.3, 14.4]
>>> sorted(clean)  # Sorting now works as expected
[14.4, 18.3, 19.2, 20.7]
>>> median(clean)       # This result is now well defined
18.75

```

[Subject index](INDEX.md) · [Continue](averages-and-measures-of-central-location.md)

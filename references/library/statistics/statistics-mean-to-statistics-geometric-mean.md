# statistics: `statistics.mean()`, `statistics.fmean()`, `statistics.geometric_mean()`

### Function details

Note: There is no requirement that the supplied data already be sorted. Even so, for easier reading most examples here use sorted sequences.

 statistics.mean(*data*)

Return the sample arithmetic mean of *data*, which may be a sequence or an iterable.

To get the arithmetic mean, divide the total of the data by how many data points there are. Although people routinely call it “the average”, it is just one among many mathematical averages. It indicates where the data is centrally located.

When *data* is empty, a `StatisticsError` is raised.

A few usage examples:

```pycon
>>> mean([1, 2, 3, 4, 4])
2.8
>>> mean([-1.0, 2.5, 3.25, 5.75])
2.625

>>> from fractions import Fraction as F
>>> mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])
Fraction(13, 21)

>>> from decimal import Decimal as D
>>> mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
Decimal('0.5625')

```

Note

[Outliers](https://en.wikipedia.org/wiki/Outlier) heavily influence the mean, which therefore need not represent a typical data point. When you want a sturdier — if less efficient — gauge of [central tendency](https://en.wikipedia.org/wiki/Central_tendency), turn to `median()`.

Because the sample mean is an unbiased estimator of the genuine population mean, averaging `mean(sample)` across every possible sample converges on the whole population's true mean. Should *data* stand for the full population instead of a sample, `mean(data)` amounts to computing the true population mean μ.

 statistics.fmean(*data*, *weights=None*)

Cast *data* to floats and return their arithmetic mean.

It is quicker than the `mean()` function and consistently yields a [`float`](https://docs.python.org/3.14/library/functions.html#float). Here *data* may be a sequence or iterable. When the supplied dataset is empty, a `StatisticsError` is raised.

```pycon
>>> fmean([3.5, 4.0, 5.25])
4.25

```

You can optionally apply weights. Consider a professor who grades a course by weighting quizzes 20%, homework 20%, a midterm exam 30%, and a final exam 30%:

```pycon
>>> grades = [85, 92, 83, 91]
>>> weights = [0.20, 0.20, 0.30, 0.30]
>>> fmean(grades, weights)
87.6

```

When *weights* is provided, its length must match that of the *data*; otherwise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

Added in version 3.8.

Changed in version 3.11: Added support for *weights*.

 statistics.geometric_mean(*data*)

Cast *data* to floats and return their geometric mean.

By relying on the product of the values rather than their sum (which is what the arithmetic mean uses), the geometric mean conveys the central tendency or representative value of the *data*.

A `StatisticsError` is raised when the supplied dataset is empty, holds a zero, or holds a negative value. Here *data* may be a sequence or iterable.

There is no particular attempt to deliver exact results. (That said, this could change later on.)

```pycon
>>> round(geometric_mean([54, 24, 36]), 1)
36.0

```

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](statistics-for-relations-between-two-inputs.md) · [Continue](statistics-harmonic-mean-to-statistics-kde.md) · [Owning module, declaration or section: statistics](statistics-mathematical-statistics-functions.md)

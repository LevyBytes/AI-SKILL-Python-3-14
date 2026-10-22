# statistics: `statistics.harmonic_mean()`, `statistics.kde()`

statistics.harmonic_mean(*data*, *weights=None*)

Return the harmonic mean of *data*, a sequence or iterable holding real-valued numbers. When *weights* is left out or set to `None`, equal weighting applies.

You obtain the harmonic mean by taking the reciprocal of the arithmetic `mean()` of the data's reciprocals. As an illustration, the harmonic mean of the three values *a*, *b* and *c* equals `3/(1/a + 1/b + 1/c)`. Should any value be zero, the outcome is zero.

A kind of average, the harmonic mean measures where the data is centrally located. It tends to fit best when you average ratios or rates — speeds, say.

Imagine a car covers 10 km at 40 km/hr and then a further 10 km at 60 km/hr. What is the average speed?

```pycon
>>> harmonic_mean([40, 60])
48.0

```

Imagine a car holds 40 km/hr over 5 km and then, once traffic eases, accelerates to 60 km/hr across the trip's remaining 30 km. What is the average speed?

```pycon
>>> harmonic_mean([40, 60], weights=[5, 30])
56.0

```

A `StatisticsError` is raised when *data* is empty, when any element is below zero, or when the weighted sum fails to be positive.

As it stands, the algorithm bails out as soon as it meets a zero in the input. As a result, the inputs that follow go unchecked for validity. (Later versions may behave differently.)

Added in version 3.6.

Changed in version 3.10: Added support for *weights*.

 statistics.kde(*data*, *h*, *kernel='normal'*, ***, *cumulative=False*)

[Kernel Density Estimation (KDE)](https://www.itm-conferences.org/articles/itmconf/pdf/2018/08/itmconf_sam2018_00037.pdf): Build a continuous probability density function or cumulative distribution function out of discrete samples.

At its core, the technique smooths the data with [a kernel function](https://en.wikipedia.org/wiki/Kernel_(statistics)). so that you can infer something about a population from a sample.

How strong the smoothing is depends on the scaling parameter *h*, known as the bandwidth. Lower values bring out local detail, while higher ones yield smoother output.

Which *kernel* you pick fixes the relative weighting of the sample data points. As a rule, the kernel's shape matters far less than the more decisive bandwidth smoothing parameter.

Among the kernels that assign some weight to every sample point are *normal* (*gauss*), *logistic*, and *sigmoid*.

Among the kernels that assign weight only to sample points inside the bandwidth are *rectangular* (*uniform*), *triangular*, *parabolic* (*epanechnikov*), *quartic* (*biweight*), *triweight*, and *cosine*.

When *cumulative* is true, a cumulative distribution function is returned.

A `StatisticsError` is raised whenever the *data* sequence is empty.

[Wikipedia has an example](https://en.wikipedia.org/wiki/Kernel_density_estimation#Example) in which `kde()` builds and plots a probability density function estimated from a modest sample:

```pycon
>>> sample = [-2.1, -1.3, -0.4, 1.9, 5.1, 6.2]
>>> f_hat = kde(sample, h=1.5)
>>> xarr = [i/100 for i in range(-750, 1100)]
>>> yarr = [f_hat(x) for x in xarr]

```

With the points in `xarr` and `yarr`, you can draw a PDF plot:

 (Figure: Scatter plot of the estimated probability density function.)

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](statistics-mean-to-statistics-geometric-mean.md) · [Continue](statistics-kde-random-to-statistics-median-high.md) · [Owning module, declaration or section: statistics](statistics-mathematical-statistics-functions.md) · [Owning module, declaration or section: Function details](statistics-mean-to-statistics-geometric-mean.md)

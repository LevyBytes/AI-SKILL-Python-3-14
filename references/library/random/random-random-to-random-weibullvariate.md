# random — Real-valued distributions

### Real-valued distributions

The functions below produce particular real-valued distributions. Their parameters carry the names of the matching variables in each distribution's equation, following standard mathematical usage; nearly all of those equations appear in any statistics textbook.

 random.random()

Return the next random floating-point number in the range `0.0 <= X < 1.0`

 random.uniform(*a*, *b*)

Return a random floating-point number *N* such that `a <= N <= b` for `a <= b` and `b <= N <= a` for `b < a`.

Whether the end-point value `b` lands inside the range hinges on floating-point rounding within the expression `a + (b-a) * random()`.

 random.triangular(*low*, *high*, *mode*)

Hand back a random floating-point number *N* satisfying `low <= N <= high`, with the named *mode* sitting between those limits. The *low* and *high* limits default to zero and one. When *mode* is omitted it defaults to the point halfway between the limits, producing a symmetric distribution.

 random.betavariate(*alpha*, *beta*)

Beta distribution. The parameter conditions are `alpha > 0` and `beta > 0`. The values returned fall between 0 and 1.

 random.expovariate(*lambd=1.0*)

Exponential distribution. *lambd* equals 1.0 divided by the mean you want. It must not be zero. (The natural name would be “lambda”, but Python reserves that word.) The values returned span 0 up to positive infinity when *lambd* is positive, and negative infinity up to 0 when *lambd* is negative.

Changed in version 3.12: A default value for `lambd` was added.

 random.gammavariate(*alpha*, *beta*)

Gamma distribution. (This is *not* the gamma function!) The shape and scale parameters, *alpha* and *beta*, are required to be positive. (Conventions differ, and certain sources treat ‘beta’ as the reciprocal of the scale).

The probability distribution function is:

```python
          x ** (alpha - 1) * math.exp(-x / beta)
pdf(x) =  --------------------------------------
            math.gamma(alpha) * beta ** alpha

```

 random.gauss(*mu=0.0*, *sigma=1.0*)

Normal distribution, which also goes by the name Gaussian distribution. Here *mu* gives the mean and *sigma* gives the standard deviation. It runs a touch quicker than the `normalvariate()` function described further down.

Multithreading note: Should two threads invoke this function at the same moment, they may both come away with the identical return value. Three approaches avoid this. 1) Give each thread its own instance of the random number generator. 2) Wrap every call in locks. 3) Switch to the slower yet thread-safe `normalvariate()` function.

Changed in version 3.11: Default arguments are now provided for *mu* and *sigma*.

 random.lognormvariate(*mu*, *sigma*)

Log normal distribution. Taking the natural logarithm of this distribution produces a normal distribution whose mean is *mu* and whose standard deviation is *sigma*. *mu* may take on any value, while *sigma* has to exceed zero.

 random.normalvariate(*mu=0.0*, *sigma=1.0*)

Normal distribution. Here *mu* denotes the mean and *sigma* denotes the standard deviation.

Changed in version 3.11: Default arguments are now provided for *mu* and *sigma*.

 random.vonmisesvariate(*mu*, *kappa*)

*mu* is the mean angle, given in radians between 0 and 2**pi*, while *kappa* is the concentration parameter, which has to be at least zero. When *kappa* equals zero, the distribution collapses to a uniform random angle spanning 0 to 2**pi*.

 random.paretovariate(*alpha*)

Pareto distribution. *alpha* is the shape parameter.

 random.weibullvariate(*alpha*, *beta*)

Weibull distribution. Here *alpha* serves as the scale parameter while *beta* serves as the shape parameter.

[Subject index](INDEX.md) · [Previous](random-binomialvariate.md) · [Continue](random-random-class.md) · [Owning module, declaration or section: random](random-generate-pseudo-random-numbers.md)
